Welcome back to the newest installment of *DarkFO Devlog*! It's been a while, hasn't it? Sorry about that -- I took a break from developing the engine for a while. I decided it was time to take a look at it again, though, and perhaps give it a small overhaul. And that I did. Let's look at how.

Mirror Into The Past
====================

DarkFO was in a bit of a messy state. It was written predominately in vanilla JavaScript which, as you *should* know, is incredibly -- masochistically, even -- error prone.
As it were, it is incredibly difficult to develop and maintain large applications in pure JavaScript. I was not even a fan of it in the first place.

The way I structured the code initially was awful: there were ad-hoc structures everywhere. Game objects were little more than wishful thinking that an object given to you had the properties as you expect them.
Objects created dynamically by their PID and loaded from the map were treated very differently. Each type of object had extra properties that were constantly being tested against. Game objects and even certain critters even had special temporary mutable variables for things like animation and would be tested against sometimes.


That had to change, quickly.

I had been a small fan for a while of [TypeScript](http://www.typescriptlang.org/), which augments vanilla JavaScript with a stronger, static type system and provides at least basic guarentees about your code's structure and types. This is something I consider the absolute bare minimum for a language and is something JavaScript lacks entirely.

TypeScript also adds a class-based OOP system; which, while I'm not the biggest fan of, suffices. Indeed, it makes my otherwise messy code much nicer: I can refactor these nasty, ad-hoc structures into modules and hierarchies of types and get basic static guarentees that I am using their interfaces correctly. It's a win/win, even considering that we need to refactor a bunch of code to make use of it.

Porting
=======

After I'd decided on the change, the next step was to enact it.

I updated my TypeScript compiler, cloned a fresh copy of the DarkFO repository, set it up, and began converting all of the `*.js` files to `*.ts`.

Now, while TypeScript retains a lot of the semantics of JavaScript (for better or worse), it is also *much* stricter about them: you cannot simply rename your files and expect it to compile. 

Instead, you must annotate some of your code with types -- the types that the compiler cannot infer, or infers incorrectly. At the very least, the quick fix for some of these is to annotate values with the `any` type -- which should need no explanation. JavaScript is basically the subset of TypeScript where every value is of type `any`.

External libraries are a bit of a pain because you need type definition information from them. If you're lucky, there already exists one (a `.d.ts` file), but otherwise you will either need to create one or stub your library as `any`.

You also need to convert the module pattern:

    var mod = (function() {
        return {foo: ...};
    })();

into a more explicit module:

    module mod {
        export var foo = ...;
    }

in order for it to work correctly. (It's also much nicer.)

So, the porting itself was fairly straightforward. There were only around 256 errors to start with, and it even caught some invalid code along the way (mostly related to function arity mismatches in some function calls.)
It took about an hour and a half, so all things considered (it's < 9,000 source lines of code) it was not a huge pain.

That was just the beginning of the fun, though.

Refactoring
===========

Now that we've got our shiny new compiler set up and our codebase ported enough to start working with it, it's time to get started on some of those refactorings we promised ourselves.

The first order of business was cleaning up the handling of game objects.

Before, the map loader would create a lightweight object, filling it in with the PID and such, and then hand it over to `initObjects` or `initCritters` (both accepting a list for some reason.) These functions were not robust in any sense. The control flow was whacky and there were a few divulging codepaths where you may or may not get certain properties on the resulting game object. Bad, bad stuff. (Also, it was in the main, catch-all `.html` file for some reason.)

I started refactoring this into a TypeScript class. I had to specify an interface for game objects: what properties do they have. Concretely. No "this object may *possibly* in some circumstances contain property X", just "this object always has property X."

That was surprisingly tricky when your objects were already so ad-hoc that you didn't even know *what properties objects could have*. But that's what the type system is for! Once you start annotating other functions and variables as being of type `Obj` (our game object class), the compiler will start telling you what is wrong or missing. You can gradually work through the errors and correct your definitions until you are satisfied that it is correct enough.

Since we're moving objects into classes now, the initialization logic also had to go in. Since objects can be loaded either dynamically from a PID or from a lightweight map object, I leave the initialization to some static factory methods. The constructor just constructs an object of default values.
We then rewrite `initObject` and add it as a method of our nice new class.

So, now we need to handle critters. Well, critters are *also* game objects; they just behave differently sometimes. As is tradition, we add a `Critter` subclass inheriting from `Obj`, and providing its own initialization logic inheriting from `Obj`'s. Fantastic.

Aside: Instantiation
-----

As an aside here, there is now a problem with the types. If you write the type of, say, `fromPID` in `Obj` as: `static fromPID(pid: number): Obj` and extend this in `Critter` with:

    static fromPID(pid: number): Critter {
        var obj: Critter = <Critter>super.fromPID(pid); // NOTE: <T>u is a type cast
		...;
		return obj;
	}

then, while your type annotation says you return a Critter (and you do), you are actually returning an `Obj` because it was instantiated as an `Obj` in `Obj.fromPID`. It will not go through `Critter`'s constructor.

To rectify this I simply made `fromPID`, etc., polymorphic and inverted the control such that subclasses are the ones who instantiate the basic object, of any type deriving `Obj`, instead of `Obj` doing that with only one type.

This ends up looking rather silly, but effective:

	static fromPID<T extends Obj>(obj: T, pid: number): T {
		...;
	}

And now our code is both type-safe (hooray!) and we have our properly instantiated objects with runtime type information.

Result
------

So now we have nice `Obj`, `Critter`, `Item`, etc. classes, each with their own subtype-specific properties and logic. Perfect. Now we no longer need to make guesses and pray over holy incense that our objects be as we expect. Now we just *know*, as is the power of a decent language with a strong type system.

This instantly makes the code a *lot* cleaner, especially as we begin moving what were procedures into class methods and cleaning them up or refactoring, being sure to take further advantage of subtype polymorphism to reduce ugly and unsafe conditions in our logic.

All in all, it's infinitely better, and it feels less fragile. Now it's not as if you would shatter the entire thing if you made one seemingly simple change. Now loading and logic are unified into one place, not only reducing the code but also lowering the complexity substantially. It has already cut down the bugs by a significant amount. A+ 11/10, would recommend.

Mistakes
========

So, while this was an amazing win for the project's source code, after a few nights of porting and refactoring, I realized I had made one very grave error: I was on the wrong git branch. Shock, horror, gasp.

The branch I *meant* to be on was not merged into `master`, as it represented more experimental changes. Although those changes were mostly stable. Things like, say, the entirety of the world map and random encounter functionality.

Since these changes were extensive, and my codebase had changed so drastically (files were renamed, files were rewritten, split, merged, moved...) it had no chance of being automatically mergable. Even the merge conflicts showed that git was as confused as I was.

After a couple of days of messing around, trying to find a tool that would ease merging it, I eventually just gave in and did what I probably just had to do: install TortoiseMerge, `git format-patch master..working_branch`, and **manually edit and merge 52 patches** over the course of two or three hours. Whew. (TortoiseMerge's UI is nothing to admire, either. It's pretty horrible with conflicts.)

Thankfully, that is done now, and I was able to port the Worldmap and Random Encounters functionality to our home here with TypeScript. All is well.

Features!
=========

I know you're just begging, "What about the features?! Surely you didn't spend all of this time working on invisible code voodoo!"

Well, yes and no. Most of the time was spent tracking down and fixing either existing bugs or bugs added with the large refactoring (or just adding type annotations), but there is one fix/feature I can talk about.

Slots!
------

*Fallout 2*, like any decent game, has mini-games involving gambling. You have a Gambling skill which directly affects how well you do at said games.

<a href="darkfo-slots.png"><img src="darkfo-slots.png" alt="DarkFO Slots" width="800" height="570"></a>

There is a problem with them, though: in DarkFo, they did not work. You would always lose, but more strikingly, in the console you would note that it triggers the sound for "winner" and "looser" [sic] at the same time, one after the other. That is clearly not supposed to happen!

Well, it turns out that specific problem was caused by yet another error in my script parser. The unary negation (`-`) operator had too high of a precedence, so that:

	-3 + 2

was being parsed as `-(3 + 2)` and not `(-3) + 2`! Oh no! Thankfully, a quick fix, and with it that problem goes away.

However, slots still did not let you win, no matter if you gambled away an infinite amount of money in the span of five minutes.

This was because of my confusion in my own scripting stubs: the function for rolling a 1d100 die against a particular skill (in this case Gambling) was stubbed to always return `1` (supposed to indicate success) in DarkFO. This is fine, but that `1` was being passed to `is_success`, which was logged to the console in a display of "`is_success: 1`". Now, I would think that meant `is_success` *returned* `1` (a success), but in fact it was returning `0` (failure). Alas, we always lost our infinite pool of money.

I spent the rest of the day on reverse engineering `roll_vs_skill` only to find out it behaves like combat rolls do, in that it does a 1d100 roll vs your skill level (plus any modifiers), and then rolls a 1d10 vs the first roll / 10 for a critical success or critical failure roll.

I thought the slots themselves were interesting, though: there are three tiers of them. There are Normal slots, High Roller slots, and Jackpot slots. They each have varying payoffs: their minimum and maximum bets increase as well as what they give you.
In additions, Jackpot slots have a chance at gaining you quite a bit of caps, up to $2500 I believe. Unfortunately, after you jackpot, they simply break into a terminal of "Out Of Service". Probably after you've already spent $2500 on the damn machine, but I digress.

Conclusion
==========

That, folks, was porting, refactoring, and gambling in DarkFO.

Hope you enjoyed.