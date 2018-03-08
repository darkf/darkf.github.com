---
layout: post
title: "VNC and RFB at a Glance"
date: 2016-11-26
---

VNC and RFB at a Glance
==============================

VNC (Virtual Network Computing) is one of the oldest and most popular systems for screen sharing a computer over a network. It was borne out of Cambridge as a research project, circa ~1998. After their research lab was closed, the development team founded a company to further its development. The result of that is RealVNC, which continues to evolve it.

Their software has since been used very successfully for several decades, typically in business and IT settings where one can remotely troubleshoot a malfunctioning PC or offer remote assistance. Its legacy has spawned many implementations, clones, and competitors since.

However, in the age of 2016 -- and quickly coming on 2017 -- it's an interesting exercise to take a look at what makes VNC tick, and where it could be improved. Is it a reasonable and efficient protocol for the modern age?

Protocol
---------

The VNC system uses a protocol named [RFB](https://en.wikipedia.org/wiki/RFB_protocol) -- the Remote Framebuffer Protocol -- to communicate over the network. RFB is a fairly simple binary octet-based protocol, designed to be served over reliable stream-oriented transports, almost always being TCP/IP in practice.
For extra security, it is sometimes served in another layer over [SSH](https://en.wikipedia.org/wiki/Secure_Shell).

Clients are given the most control in RFB: the server must only send data in formats the client has acknowledged and requested.

The protocol is described in [RFC 6143](https://tools.ietf.org/html/rfc6143), the latest current version (version 3.8 of the protocol) dating from March 2011.
The versions are not vastly different, only really differing in their handshakes.

In RFB, the server sends a version string (in ASCII). The client then responds with its own version string, which must be lower than or equal to the server's version.
Servers are expected to maintain some sort of backwards compatibility between versions.

After the version is negotiated, next comes security. RFB has 2 standard authentication methods: none (anyone is free to connect), and a passcode-based authentication.

The latter is cryptographically weak: the client just DES-encrypts a 16-byte challenge text with their passcode key. [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) is now considered broken. For this reason, and that the stream is not obfuscated or immutable to anyone listening in, one sometimes wishes to tunnel RFB over a more secure transport.

The versions of the protocol differ in how they handle negotiating the response: In 3.8, the server is the first to offer a list of security types, and the client responds, followed by the server finalizing it. In 3.3, for a "none" authentication type, nothing more is said; only for "VNC Authentication" is a result sent.

The client then sends a flag indicating if the server should drop all other clients or not. (This is a bit odd: why place this in the hands of the client, and not the server configuration?)

The server then sends information about the framebuffer: its size, the pixel format, and the name of the server.

Pixel Format
------------


The server tells us how it intends to encode pixel values. In this message, we're given the bits per pixel (bpp), color depth (*effective* bits per pixel -- how many bits actually encode color), and some masks and shift offsets which effectively tell us *where* and *how large* each color component is, in the overall *bpp* bit pixel value.

There is some other ancillary information, such as if the color is a *true color* value (meaning that RGB values are stored), or if it is paletted (a set of 8-bit palette indices). It also indicates whether the pixel value is big endian, should *bpp* be larger than 8.

This is where we start to see some oddness. We note in the spec:

>Currently bits-per-pixel must be 8, 16, or 32.
    
You'll note that `24` is curiously missing. Why is this? It is common to represent RGB values as `R8G8B8` -- that is, 8 bits per component, or a total of 3 bytes.

This arbitrary restriction means that we're wasting one byte per pixel if we're storing a color depth of 24 bits (which we are, on modern PCs) in the Raw encoding. It also makes it slightly harder for me to decode in my educational client. :-)

I'm not very enthused that this restriction has no visible rationale behind it.

Anyway: "True color" pixel values are typically 32-bit integers for 24-bit color depth, either in big or little endian format. To get the RGB values from this, we use the data we got from the server:

    r = (pixel_value >> red_shift) & red_max
    
And so on, for the other color components. This format is convenient because it is fairly easy to write a decoder for, and it gives us the flexibility to have color components take any number of bits (up to the total bits per pixel, of course).

Messages
--------

Now that the handshake is done, asynchronous messages can start flowing. The server is not allowed to send unsolicited messages, so the client controls almost everything here.

Every message begins with a 1-byte message type (overloaded for Client-to-Server and Server-to-Client messages), followed by a format dependent on the message type.

The client will send `FramebufferUpdateRequest` messages to grab the new state of the framebuffer. Initially this will be a non-incremental (that is, full) update; after that, the client may request incremental (diff) updates.

The server responds with a set of one or more rectangles consisting of a position, size, and the pixel data in a varying -- but agreed-upon a priori -- encoding.

The specification specifies a few standard encoding types:

| ID   | Name                        | Description                                          | Status   |
|------|-----------------------------|------------------------------------------------------|----------|
| 0    | Raw                         | Raw, uncompressed pixel data                         | Required |
| 1    | CopyRect                    | Copies a rectangle from elsewhere in the framebuffer |          |
| 2    | RRE                         | Rise-and-Run-length Encoding -- 2D RLE of tiles      | Obsolete |
| 5    | Hextile                     |                                                      | Obsolete |
| 15   | TRLE                        | Tiled Run-Length Encoding                            | Active   |
| 16   | ZRLE                        | Zlib Run-Length,Encoding                             | Active   |
| -239 | Cursor pseudo-encoding      | Encodes cursor image data                            |          |
| -223 | DesktopSize pseudo-encoding | Encodes a size change in the framebuffer             |          |

(I suspect the IDs are so sparse for historical reasons. RFB is intended to be an extensible protocol. Negative IDs are likely reserved for pseudo-encodings.)

The only encoding *required* by the client is the Raw encoding, which is the most primitive. Raw encoding simply gives a list of pixels (each *bpp* bits long) in the pixel format given earlier by the server.

Interestingly, TRLE and ZRLE use the "CPIXEL" type, which is like the normal "PIXEL" type but with a special case when the *bpp* is 32 and the color depth is 24 and the color components fit sequentially in the upper or lower parts of the word -- i.e., most modern cases.

CPIXEL pixels encode "true color" in 3 bytes instead of 4. (In my opinion, this is silly, since there's no reason for this to be a special type, but I digress.)

ZRLE is pretty much just TRLE over a [Zlib](https://en.wikipedia.org/wiki/Zlib) compressed stream. This is another point
where I'd argue it's limited: Zlib is good at compression, but it's not very time-efficient. Nowadays we have projects like [miniLZO](http://www.oberhumer.com/opensource/lzo/), which compresses faster than Zlib, at the expense of a slightly worse compression ratio. For real-time applications, I can't see it being bad to trade off performance for size in this case unless the network is *very* slow. There is also [Brotli](https://en.wikipedia.org/wiki/Brotli), which is around the same speed as Zlib, but with a slightly better compression ratio.

If you're interested in how the other encodings work, please refer to the RFC.

Auxillary Functions
-------------------

RFB allows the client to send keyboard presses and mouse clicks, as well as manipulate the system's clipboard. A caveat, however:

>There is no way to transfer text outside the Latin-1 character set.
    
All text, including the server name and clipboard contents, is assumed to be in the Latin-1 ([ISO 8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1)) character encoding.
This means that it only accepts Latin-based/English text, and not the larger Unicode character set. This is an unfortunate historical artifact: most of the modern Web [uses UTF-8](http://utf8everywhere.org/), which is both backwards-compatible with ASCII and supports the entire space of Unicode characters. Think of the non-English symbols!

(I find it odd that there is no way to negotiate another character encoding, like you can pixel formats or security types. It seems like an oversight in the protocol.)

The server may also send a "bell" notification (such as when your terminal beeps.)
How it's implemented is up to the client.

Concluding Thoughts
-------------------

VNC has really stood the test of time, however it's not as robust as it could be. Newer protocols based on modern video codecs -- such as h.264 or VP8 -- are coming around and pushing the envelope for real-time screen sharing. Modern video codecs are really good at [motion estimation](https://en.wikipedia.org/wiki/Motion_estimation) and [motion compensation](https://en.wikipedia.org/wiki/Motion_compensation), making them a good choice for incrementally changing images -- such as scrolling on a desktop. They're also a good choice for encoding streaming video, obviously -- if your desktop happens to be playing something, you might prefer it to the choppier incremental updates that VNC has. These codecs, however, are lossy and geared more towards offline encoding, so at the very least tuning and adjustments must be made.

The VNC ecosystem is still evolving (remember, it's extensible!) with RealVNC and open source projects. There are even [attempts at placing a h.264 encoder](http://www.turbovnc.org/About/H264) onto it. RFB proves a reliable and extensible foundation for trying new methods of encoding desktop framebuffers.

I suggest to anyone who is interested that they read through the RFC and take a day or two to implement a VNC client. It's an interesting exercise, it's relatively simple, and you get a fun show-off project out of it. :-)