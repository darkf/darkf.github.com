---
layout: post
title: "DarkFO Devlog Part IV"
date: 2014-07-08
---

This installment covers some changes (major and minor) from the last few weeks.

Animation
=========

Partial support for partial animations (*heh*) is done.

If you need a refresher, partial animations are names for sub-animations for models. Things like walk and run animations are sequences of several partial animations over each tile.

Now that it plays these, walking and running looks more correct now (even for varying critters such as ghouls, whose walk animations take longer and over less time.)

Some objects animate forever, using the script `ANIMFRVR`. This works now, along with other static animations (such as opening and closing doors/containers), and FPS is also taken into account.

Gameplay
========

Gameplay has improved quite a bit. Map loading has been improved majorly -- you can load in separate maps in the same session. The player starts at the correct starting point in the map. Exit grids and stairs now work (sans animation for the latter, for now.)
The camera now scrolls when you move your mouse to the edges of the viewport.

These changes alone make it feel more like an actual game, so it's great to see some improvement there.

Some minor work on object usage (such as opening and closing doors) has been done. There's still no object mouse picking, so you can't simply click on them.

Combat
======

More correct hit chance and also critical hits have been implemented by a friend. Combatants can now miss their shot, or obtain critical hits that deal more damage.

(A weird thing about this is that the critical hit tables are [hardcoded in the game executable](http://falloutmods.wikia.com/wiki/Critical_hit_tables). Yes, really.)

Scripting: General
=========

Again, most of the work seems to have fallen on scripting, which drives most of the game.
In the last post, I noted a few solutions to a particular problem of simulating blocking calls (as the game scripts expect) in asynchronous code (transpiled JavaScript). I ended up with some fairly unideal solutions: using experimental and unportable language features, or writing an implementation of the bytecode VM. For now, I don't want to bother with the latter, because emulating them at a high-level gives a few benefits:

- Game objects are represented as plain JavaScript objects (references to the actual engine objects, rather than an integral pointer.) This results in a much nicer implemented API.

- Scripts are still *somewhat* human-readable (they lose most of their intuition but retain their semantics and structure, at least.)

- They're easier to debug. I can easily modify the scripts without recompiling to insert plain JavaScript code; I can easily read potential logic problems and inspect values.

- You can just write new scripts in (saner than the compiled) JavaScript without any special infrastructure in place.

So, for now, I will try to get as far as I can (up to and including "mostly compatible") with high-level emulating these.

For a few days I worked on how I am currently solving the problem, which just involves transforming the script program to yield whenever the dialogue end (this will probably be extended to a few more later on) procedure is called.

The scripting engine is then trivially extended to support this, resuming execution of the script after the dialogue has ended after it actually has. This lets us support things like moving inventory back to its proper place after bartering.

This approach does have a few limitations, but it can be extended. So far it's worked for quite a few of the cases I've tested, so that's a great sign.

Scripting: Language
===================

I finally bothered to compile all of the scripts that pass the preprocessing stage (many don't, due to errors. Watcom from the 90's was a really... questionable compiler.)

What I found was that my parser could not handle 96 of them. So I set out to work, discovering some things about the language:

There are variable declaration blocks:
 
     variable begin
         foo := 0;
         bar; /* equivalent */
     end

Which is not all that useful, actually.

There are float literals! The question still remains whether operations such as division work differently on values of different "types" (floats or integers) or whether they always result in a float.

Procedures have parameters! This isn't really a surprise, but it is kind of a surprise to see scripts actually use it.

With all of this stuff done, we're down to *9* scripts not compiling! Two of those you can count off, actually, because they're just empty scripts.


Scripting: Engine
=================

So, back to the meat of it: implementing the parts directly accessible to the scripts.

Scripts have a callback procedure for combat, which is fairly limited in scope (it's only used for checking game/combatant status during turns, or performing special logic during hits/misses, etc.)
These are just called on combat events, so it's pretty easy to do. The only thing I've encountered that uses it so far is the Arroyo Temple Villain (`ACTEMVIL`), who is the first human enemy you (should) encounter. He's at the beginning of the game, where you have the option of dueling him unarmed to pass your trial.

Whenever he drops below half of his maximum health, he will disengage combat, give you back your equipment (placed in a footlocker, of course) and then run across some waypoints to the end of the map, then turns himself invisible.

After this, you're able to progress onto the real first open world map, the village of Arroyo.

With all scripts loaded, the village now comes to life -- tribals and brahmin alike now animate to walk around. Except there's a problem: some tribals are being possessed and walking to their assured death in the void. The void being the origin `(0, 0)`.
That's just because I didn't bother initializing scripts with the `start` procedure. Now all is well again. (And *technically*, brahmin can wonder out of their pen, but has anyone really *seen* that?)

The rest are mainly just minor improvements to things like stat or flag getters, or things related to animation, or miscellaneous procedures.

Conclusion
==========

By the way, guess how inventory is removed from a critter? What's the most logical thing to do?
Well, now that you answered "by calling something like `rm_inven(obj)`, throw that out the window because that's not what happens at all.

The game spawns a footlocker *specifically to immediately move the inventory contents into it and then destroy it*. What a great design decision, especially for an engine so built on low-level optimizations, and it would be very simple for them to implement an `rm_inven` and `swap_inven`, but hey. Fallout 2, folks! 