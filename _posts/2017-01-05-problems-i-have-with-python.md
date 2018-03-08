---
layout: post
title: "Problems I Have With Python"
date: 2017-01-05
---

I've been using Python for about 10 years now. I love the language as much as I can any, and for the most part I enjoy writing in it -- and reading it.

However, despite its qualities it also shares quite a few massive flaws that slow me down and make me groan and sigh while attempting to solve problems in it. These are obvious flaws in design, in my opinion, that warrant re-looking at, but to which no real improvements are being made for some reason. (Incompetence? Politics? Both? Who knows.)

There are some languages (such as [Coconut](http://coconut-lang.org/)) which transpile to Python, but I argue that I should not *have* to build a better language on top of an already decent one.

Why can't Python accept some fairly sane changes and improve its experience throughout? Things other languages have and are well-received? Remove inconsistencies, and add useful features? Is that not what a growing languages aspires to -- or should?

With that in mind, here are some of the common issues I have with Python. Remember that it's a matter of opinion, although they stem from experience. Without further ado:

- The standard interpreter bring rather slow; PyPy is nice, but its Python 3 support is very immature.

- Parallelism is very bad on CPython and PyPy; threads are subject to the Global Interpreter Lock (GIL),
    and one must use `multiprocessing` (which comes with its own bag of oddities) to get real parallelism.

- `asyncio` does not seem very well integrated, and does not seem as useful as libraries like `eventlet`.
    They seem to have wanted to reinvent Twisted, but did so half-assed and did not include useful protocols
    (Twisted has line-based protocols, HTTP, etc. built in and easily subclassable.)

- Quite a few legacy projects are written in Python 2, and it *can* take some work to port them.
    This is particularly a pain for libraries where I expect to `pip install` them and have them "Just Work".

    There is an official tool `2to3` which does not work in all cases.

- The standard library is sometimes inconsistent
    For example, the `str` type has a `split` method but `list` does not. Even weirder, `str` and `list` both have `find`, but `list` does not have `index` (a related method).

    Naming is sometimes inconsistent, despite Python 3's attempt at standardizing it.

- Inadequate support for high-level functional programming

    The BDFL himself, Guido van Rossum, has infamously declared that he does not like functional programming
    (odd, considering the language is built around FP concepts), and that `map`/`reduce`/`filter` should not be
    in the language. Well -- in my opinion that is a grave mistake, but more importantly the language suffers.

    `reduce` is now tucked away inside the `functools` module (as of Python 3), even though it is the only one
    of `map`/`filter` that is *not* replaceable by list/set/dict comprehensions! Yet `map` and `filter` are still
    in the base global environment. What sense does that make?

    `itertools` is useful, but duplicates quite a bit and does not include many useful functions standard in a lot of FP language standard libraries.
    It's also not too clear how some of them maybe use: I often find myself reimplementing `flatten` as `flatten = lambda xs: itertools.chain.from_iterable(*xs)` (what a mouthful), as if I were supposed to figure this out on my own, instead of just providing a `flatten` (and `flatmap`) function.

    For that matter -- flattening is something that should be so common that it were given a place in the global function set, but there is not even a way to do it in syntax.

    Early in [PEP 0448](https://www.python.org/dev/peps/pep-0448/#variations) was a proposed syntax for flattening in comprehensions:

        >>> ranges = [range(i) for i in range(5)]
        >>> [*item for item in ranges]
        [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]

    This would have been very useful and allow flattening inline in comprehensions, but "this was met with a mix of strong concerns about readability and mild support." Sigh. (Nothing about that looks "unreadable" to me.)

    The lack of tail call optimization in most implementations makes writing tail recursive algorithms rather pointless, unfortunately, even when they may be more legible than their iterative counterparts.

    There is no standard way (even in `functools`) to compose functions. There is partial application via `functools.partial`, at least...

- Lambda is awful

    BDFL again stated that it was a mistake approving it, although again I disagree -- even in its abysmal state. Without it, I would not even use Python any longer.

    Quite to the point, lambdas (anonymous closures) in Python are gimped. They are single-expression functions,
    which means *no statements*, even `global`/`nonlocal` qualifiers. Prior to Python 3, this meant you couldn't even use `print` (then a statement) in them! What nonsense.

    I imagine that attempts at making lambda not suck are met with "But that would require braces / funky indentation!" Well... what's worse, having a slightly goofy looking inline "def", or having a gimped language?
    Guido seems to add a lot of other dubious garbage, why not something useful? For the sake of some perceived "clarity"? Come on.

- Inadequate data modelling facilities

    Python classes are useful, but it is a *ton* of boilerplate to write variant classes such as:

        class Node: pass
        class FooNode(Node):
            def __init__(self, x, y):
                self.x = x
                self.y = y
        class BarNode(Node): pass

    Which is not even very useful, as there are no distinguishable `__str__`/`__repr__` methods on it, no comparisons between them other than identity equality, etc.

    Named tuples (`collections.namedtuple`) would better solve this, but unfortunately they're immutable (like normal Python tuples) and thus make bad "bag of mutable data" objects.

    Enums are also quite awful: your choices are using plain old strings or integers, or using the `enum` library which is not very widely used and has its own little quirks.

    My propsal would be the addition of algebraic data types (aka "discriminated unions"), similar to how [Coconut](http://coconut-lang.org/) does it, and how many functional programming languages do it.

- Lack of `switch` (or `match`)

    No, dicts with lambdas (see above) are not a replacement. No, long if-else chains are not a replacement.
    I want a nice way to match on data (preferably richly -- as with ADTs, ranges, ...) and associate matches
    with logic.

    Please do not suggest awful hacks to do this, and fix your language instead.