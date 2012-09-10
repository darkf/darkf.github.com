Lately I've seen a lot of posts titled `<Some Application> in X bytes of code!`. This must stop.


Text can be encoded in many different ways. Historically, characters were stored as bytes (such as in an ASCII 7-bit format or one of its many derivatives), but in the modern world there are many different *character encodings* we must deal with. The modern Web commonly uses UTF-8, which stores characters as octets (8 bits). Due to many programs' reliance on the ASCII encoding, it was designed to be backwards compatible with it. Tangent aside, this post is to demonstrate that the number of bytes in your code means *absolutely nothing*.


Let's start by looking at [some common encodings](http://en.wikipedia.org/wiki/Comparison_of_Unicode_encodings) and how much space they use to store one character:

* ASCII - 7 bits
* UTF-8 - 1 octet
* UTF-16 - 2 octets
* UTF-32 - 4 octets

That's right. An ambigous claim like `10 bytes of code` can mean many different things. It can mean 10 characters (UTF-8), 2 characters (UTF-32), or something else entirely - 1 byte is not guarenteed to be 8 bits!



I beg you, please use the term "characters" next time you want to brag about how small your code is.


**tl;dr** use "characters", not "bytes", when referring to units of text.