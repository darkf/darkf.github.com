---
layout: post
title: "DarkFO Devlog Part VI: Worldmap and Random Encounters"
date: 2014-08-15
---

*Fallout 2* is a wonderful and fascinating game... But sometimes you forget just how intricate it is. This is one of those times for me.

The past week has been dedicated almost solely to the World Map and Random Encounters. I'll try to touch a little bit on both of these subjects.

World Map
=========

*Fallout 2* does not entirely take place in an actual environment. A non-negligible amount of time is actually spent in an overworld-type screen: the World Map.

<a href="{{ "/assets/darkfo-worldmap.png" | absolute_url }}"><img src="{{ "/assets/darkfo-worldmap.png" | absolute_url }}" alt="DarkFO Worldmap" width="800" height="570"></a>

(*What the World Map looks like currently in DarkFO*)

The World Map is a 2D map divided into tiles (actually 20 of them) and then further divided squares (840 of them, to be precise.)

At first, it is almost entirely obscured by a fog of war: only the starting area, Arroyo, has been discovered. (After all, you've lived there your entire life, not venturing far outside of the village.) 

But as the time comes for you to leave the village, you realize that the world is big, massive even: there are many places (squares!) to explore.
Some squares even contain areas: usually cities or other special places to discover, big or small.


So, the premise is simple: You can click anywhere on the World Map to set a target on where you want to go. Your party then walks (or rides in a car, if you have one) to the target.

It's not that simple, though. You may randomly encounter foes, ...or even friends. But more on that later.

The Data
============

The World Map is not so much interesting as is the way it's put together. `WORLDMAP.TXT` is actually a `.ini`-style data file chock-full of information about terrain types (and speeds! Mountains are more difficult to traverse), encounter types (oceanic squares have more seafood-related encounters), and encounter chances.

It's laid out somewhat like this (but actually in reverse order):

- Tiles are defined (0 through 19) with their sub-tiles (squares)
- Squares define properties like terrain type, encounter table, and encounter rate† (none, rare, uncommon, common, forced).
- Encounter tables (e.g. `Arro_M` for "Arroyo Mountain", presumably) define a set of parameters for a specific group of encounters.
  They provide a set of randomly-chosen maps (e.g. `Mountain Encounter` 1 through 5),
  and a list of encounters.
- Encounters consist of a set of chances, encounter groups with parameters, and an optional condition -- which is specified in a domain-specific mini-language.
  For example, the condition: `If(Global(1) > 1) And If(Player(Level) > 12) And If(Player(Level) < 19)`
  would evaluate to true if the GVAR 1 is above 1, and if the player's level is in the range 13 to 18.
- Encounter groups are groups of critters that inhabit random encounters. There may be multiple groups in one encounter, even fighting one-another (and/or the player).
  They are just a set of critters.
- Encounter critters are composed of a PID, a Script ID, an optional set of items (which have an optional randomly-chosen amount range, and may be designated as wielded), and an optional condition (in the same format as encounters' conditions.)
  If you thought this wasn't advanced enough for a '90s CRPG that is already so massive, encounter groups are also given a formation: surrounding, huddled, etc. along with a spacing between them.

Even with just this toolset, it's possible to create random encounters with fairly rich environments and variety.


† It actually provides an encounter rate for each time-of-day (morning, noon, evening), but they're all the same in practice.

Random Encounters
=================

So, how do these work, in the context of the engine?

Well, first the game has to check whether or not a random encounter has occurred.
Every so often (I'm not currently sure exactly *how* often -- the original game is reportedly CPU-dependent for this; Sfall, a mod providing a set of engine patches, corrects this by adding in a time delay on the world map.)

The first thing to do is to randomly roll against the encounter rate in the current square. Then the roll is checked, chances adjusted for game difficulty setting (Easy and Hard difficulties make it less or more likely). Then we know if an encounter has occurred.

Now that it *has*, we need to figure out what *kind* of encounter has occurred. We use the encounter table (see previous section) of the current square to do this look-up.

Now, the encounter picking algorithm works like this:

- All of the encounters in the encounter list are tried: ones with a successfully evaluated condition are marked. A sum of the separate encounter chances is kept.
- A roll is made. The roll goes from 0% to (the sum of successfully conditioned encounter chances) + (Player's Luck stat - 5), plus relevant perks (Scout and Ranger give +1%, Explorer gives +2%).
- We go over the set of successfully conditioned encounters, continually decreasing our roll value by the chance of the encounter. If we reach an encounter after our roll has run out, we've found our match. If our roll went all the way, the last encounter in the list is chosen.

Now we know which encounter to use. Awesome. Now how do we set it up?

We actually take the relevant encounter groups (remember, there can be more than one, and with a randomly chosen number of occupants within a range) and set them up: evaluating critter conditions, constructing them, setting their state (they can be spawned dead), evaluating and constructing their items, etc.

The real trouble is in the formation and spacing. A set of 5 different algorithms is used to generate the formations used in the game. Those are set up for each critter, and we're done.

Conclusion
==========

The past week has been pretty boring in terms of actual work. Most of it was spent in a disassembler reverse engineering x86 assembly generated by the Watcom DOS compiler in the '90s. Not very fun at all. But it's interesting to discover how a game (especially an old one) ticks. That's really what these projects are (or should be!) about. Curiosity.

Thank you for reading.