Many people each day face the following problem: "I want to learn how to code. How do I get started?"

As it turns out, it's not such an easy question: there are many answers, and the best option depends on the individual and their goals. I hope to put together a small guide to help these people assess their needs and get them started on the long journey to programming.

(Please note that some content may be solely my opinion. You should always decide for yourself what you want to do, and double-check any facts presented as such. I try to provide hyperlinks wherever possible for further reading.)

Introduction
===========

First, you want to ask, "What *is* programming?"

Programming is, first and foremost, problem solving. Like mathematics, you use both the act and the thought processes of programming to solve puzzles. Puzzles might range from simple, such as "How do I get these series of words onto the screen?" to more complex, such as "Given these specific circumstances and constraints, how can I best design this architecture and build this program?"

Throughout your programming career, you will naturally learn through experience and thought how to solve these kinds of problems, which will allow you to craft elegant software to solve real-world problems.

Programming is also an art and a craft. You may start out using Play-Doh to create simple solid-colored blobs, but through experience you will build up your skill to craft fine ice sculptures.

This is not necessarily a quick or painless task. Indeed, Google Research Director [Peter Norvig](http://en.wikipedia.org/wiki/Peter_Norvig) suggests that [becoming a programmer is a long process](http://norvig.com/21-days.html). A skilled artist takes many years to hone their skills; the same applies to programming. But much in the same way, anyone may learn to paint or draw, but it takes time to become excellent at it.

Don't let this deter you from learning - it is an enjoyable process and you will learn *much* on the way.

What technology should I pick?
==============================

This question, or one of its variants ("What programming language should I use?") is probably the most common out there. There are many factors in deciding which tech to use out there, and it depends wholly on your goals.

I will separate at the high level two different kinds of programmers: those who want to learn for **education** (i.e., "This is interesting, I want to know more!"), or for **monetary gain** (i.e., "Wow, this is a lucrative business, I want to get in on this!").

Those learning more towards the educational benefit might be more interested in learning the foundations of programming well before moving on to tackling large code frameworks and making world-class applications with them. It is very valuable to have a good grasp on these fundamentals as it will make many things easier for you.

Those more for business will probably tend to go for the more applicative side, wanting to dive into learning how to make applications that people can use right away.

Thankfully there is not much difference between these two in terms of technologies used, and you should know that **it does not matter where you start**: across your programming career you will learn many technologies, the paths of the businessman and the hobbyist will always intersect at some point. The end goal is the achievable "I can write, maintain and understand software".

There is a lot of confusion surrounding what programming language to pick when learning. Some parties recommend using [C++](http://en.wikipedia.org/wiki/C++), some [C#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)), or some something else entirely. Again, it does not matter where you start, however some programming languages are easier to get started *learning how to program*. You want to strike a balance between these.

Programming Paradigms
=====================

Now, different conceptual styles in programming languages are often separated into [**paradigms**](http://en.wikipedia.org/wiki/Programming_paradigm).

Programming languages can either take these to extremes (single-paradigm languages) or take a hybrid approach (multi-paradigm languages). The differences are important because the concepts can differ wildly across them. Many languages, however, are multi-paradigm and mix some freely.

**Assembly** languages are among the lowest-level text-based languages. They accept CPU-specific commands and execute them without much interpretation. Usually you don't use these except when building operating systems or low-level micro-optimizing higher level code.

Control flow (i.e., "Where the execution goes") in Assembly is linear - it keeps executing lines of code until you tell it to **jump** (sometimes known as **GO TO** in other languages) to another line.   

**Structural** languages add higher-level control flow. You get constructs like **if**...**then**...**else** for conditional execution, **while...do** constructs for conditional looping, etc. These make patterns more obvious and explicit.

Most high-level languages support at least if-then-else, if not also imperative loops like while...do, do...while, for loops, etc.

**Procedural** languages add **procedures**, often basically synonymous with **functions**, into the mix. Code is separated by functions which often do one computation -- such as sum a list of integers -- by accepting an input, doing some work, and then returning a result.

**Object-Oriented** (OOP) languages add **objects** (basically containers of data and operations; they're specific instances of classes), and **classes** (types of objects, such as **Animal**)

The the main architectural focus in OOP is creating classes that represent re-usable computations and instances of those classes that work together to build up your program.
It is said to increase the modularity of programs.

**Imperative** languages consist of imperative **statements** that instruct the computer how to do something, instead of *what* to do. This is a very common paradigm and used in many languages such as Python, C, Java, etc.

Say you want to write a function to sum a list of integers. In imperative Python this might look like:

    def sum(lst):
        total = 0
        for number in lst:
            total = total + number
        return total

Instead of telling the program what it *is* you want to do, you are just telling it what to do.

**Functional** languages make functions (usually more in the mathematical sense) the prime method of separating and composing computations. Recursion (calling the same function from the function itself) of functions is usually used for looping as well. In the functional paradigm, you are often programming **declaratively** -- saying *what* something is rather than *how* it is done.

**Pure functional** languages are often more strict about this, while non-purely functional languages are typically more multi-paradigm, with imperative, OO, or both styles.
Examples of purely functional languages would be Haskell, and to some extends Erlang (altough Erlang includes globally mutable state, which is usually off-limits to purely functional languages).

Examples of non-pure functional languages include F#, OCaml, Scala, and also Python, Ruby, etc.

If you want to write a sum function in a functional style, you can do it several ways: you can build on top of an existing function (like `foldl` or `reduce`), or write it explicitly using recursion. Here are a few examples in Python:

Using `reduce`:
    import operator
    def sum(lst):
        return reduce(operator.add, 0, lst)

A sum of a list is a [fold](http://en.wikipedia.org/wiki/Fold_(higher-order_function)) pattern, and `reduce` allows you to make this explicit by passing in a function to be used with it. In this case, we use `operator.add` (the `+` addition operator), using `0` as a base value (we use `0` because it is the identity of addition -- `x + 0` is `x`.) We are saying *what* sum is.

Using recursion to write out the fold:

    def sum(lst):
        if lst == []: # If our list is empty, we've recursed all the way down,
                      # or were passed an empty list. Return our base value.
            return 0
        else: # Otherwise, our list isn't empty
            return lst[0] + sum(lst[1:]) # So return the first element plus
                                         # the sum of the rest of the elements

Program Execution
==================

There are a few main ways implementations of programming languages execute programs:

  - **Compiled** languages often take source code files and output an executable binary (such as a `.exe` file), or a bytecode file (which can then be run by an interpreter) ahead-of-time.

    C++ compilers often output executable binaries, while Java compilers often output bytecode (`.class` files, which are then run by the `java` interpreter.)

  - **Interpreted** languages often just take source code and execute it directly, skipping the ahead-of-time compilation step. These let you instantly run and test your programs, but at an increased start-up time, since the interpreter needs to parse your source code to understand it. Examples of this sort would be Python, Ruby, PHP, Perl, et cetera.

  - **JIT** implementations offer a hybrid approach -- they compile code (either source code or bytecode) **on-the-fly** when required to, possibly offering runtime code optimizations to speed up performance.
    Examples of this sort would be C#, Java, and some implementations of Python (pypy) and Ruby (Rubinius).

Don't be afraid if you don't understand any of this, it's not really important.

There are also different ways to edit source code. Don't be roped in by pointless debates or opinions, do what you're most comfortable with. In text-based programming languages, you can use just a text editor (I recommend Sublime Text 2, but you can use Notepad++, `vim` or `emacs`, or something else.) It is sometimes preferable (especially in more tedious and verbose languages like *Java*) to use an Integrated Development Environment, or IDE. These combine the functionality of text editors with special treatment of source code, and usually provide some way to easily build and run your code.

Programming Languages (and Libraries)
=====================

Now that you know some parlance, let's tackle some common technologies and their uses:

Some sects, such as **video game programmers**, often use [C++](http://en.wikipedia.org/wiki/C++) and [C#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)).
C++ is a notoriously massive and arduous language, with historical artifacts from C. Modern ([C++11](http://en.wikipedia.org/wiki/C++11) and soon to be [C++14](http://en.wikipedia.org/wiki/C%2B%2B14)) C++ is often written at a higher level (using features such as iterators, smart pointers, references, etc.) than more archaic C++ (which often use C remnants such as unwrapped arrays, raw pointers, et cetera.)

[**C++**](http://en.wikipedia.org/wiki/C++) is not necessarily a bad place to end up, but it might not be the best for beginning. Should you ever choose it, however, [C++ Primer](http://www.amazon.com/Primer-5th-Edition-Stanley-Lippman/dp/0321714113) (not to be confused with C++ Primer Plus) is a good place to start.
[C++ Reference](http://en.cppreference.com/w/) is a great reference site to use as well.
C++ is good for low-level systems programming (such as operating systems, or video games) that require high performance. It does sacrifice quite a lot of [type safety]() to achieve that, compilation times can be slow, and the process of compilation is often tedious.

[**C#**](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)) is not a bad place to start. It is a statically-typed object-oriented language in the style of *Java*. Visual C# (Microsoft's IDE) and SharpDevelop (a third-party one) provide an easy but powerful drag-and-drop interface for creating graphical (GUI) applications. Mono (and MonoGame for video games) is a good framework for building applications and deploying them to PC, Mac, iOS, Android, and other platforms.

[**Python**](http://en.wikipedia.org/wiki/Python_(programming_language)) is an dynamically-typed object-oriented/functional interpreted language. It is a great beginner language, but not just for them - it is extremely capable and great for small and mid-sized tasks.
It offers high-level features, such as first-class functions, object orientation, modules to cleanly separate source code, and operations for easily working with text, lists, sets, mappings, etc. Being dynamically typed means it will not be able to catch type errors (such as adding a string to a number) at compile-time (i.e. when you first launch the program), but only at runtime (i.e., when the faulty expression is evaluated.) With proper practice this is usually not much of an issue.

A good resource for learning Python is [Learn Python The Hard Way](http://learnpythonthehardway.org/).

For Web development, Python has some good libraries: [**Flask**](http://flask.pocoo.org/) for building from the foundation up, and [**Django**](https://www.djangoproject.com/) for re-using parts made by other people. There is also Pyramid, Pylons, etc.
For video games, [**Pygame**](http://www.pygame.org/news.html) is a nice framework, as well as [Pyglet](http://www.pyglet.org/) and [Cocos2D](http://cocos2d.org/). There are some 3D engines like [Panda3D](https://www.panda3d.org/) used by, for example, Disney Interactive.
Scientists often use Python as well for numerical calculations, with [numpy](http://www.numpy.org/) and [scipy](http://www.scipy.org/).

[**Ruby**](http://en.wikipedia.org/wiki/Ruby_(programming_language)) is also a dynamic interpreted language like Python, but with more loose, expression-based syntax. It borrows a lot of concepts from good ol' [Smalltalk](http://en.wikipedia.org/wiki/Smalltalk).

A good resource for learning Ruby is [The Poignant Guide to Ruby](http://www.rubyinside.com/media/poignant-guide.pdf) or one of the other [good resources](https://www.ruby-lang.org/en/documentation/) available.

For Web development, [**Sinatra**]()http://www.sinatrarb.com/ is a good and elegant microframework, and [**Rails**](http://rubyonrails.org/) is a **very** popular heavier framework.

[**PHP**](http://en.wikipedia.org/wiki/PHP) is another dynamic language. It is almost solely used for Web development, but it is often [considered poorly designed](http://me.veekun.com/blog/2012/04/09/php-a-fractal-of-bad-design/), and it is easy to introduce hard-to-find bugs. If you are looking to get into the PHP industry, go for it. If not, you might save yourself a headache or few. Laravel is a good Web framework.

[**JavaScript**](http://en.wikipedia.org/wiki/JavaScript) is (surprise) another OO dynamic language. Gee, these sure are popular, aren't they? Especially this one. JavaScript is used all over the Web for client-side scripting and interactivity, and sometimes on the back-end as well (usually in the form of [Node.js](http://nodejs.org/)). JavaScript has a more interesting take on OOP, borrowing [prototypal inheritance](http://en.wikipedia.org/wiki/Prototype-based_programming) from the [Self language](http://en.wikipedia.org/wiki/Self_(programming_language)). Other than that, it is your generic C-like language, besides some *interesting* design features like super weak typing that make it very easy for errors to pass unnoticed in your code, often being hard to debug. For that reason alone I will not recommend it as a beginners language, but if you are getting into the Web industry you might be interested.

There are quite a few languages that compile down to JS, most notably [CoffeeScript](http://coffeescript.org/). These are often used in lieu of just plain JS.

A good resource to learn JavaScript might be [JavaScript: The Good Parts](http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742).

[**Haxe**](http://en.wikipedia.org/wiki/Haxe) is a statically-typed object-oriented language. Its main novelty is the ability to use the same code-base across many different platforms, compiling to JavaScript, C++, C#, `.swf` (Flash), or the Neko VM. It is particularly well-suited (and indeed used much for) for 2D cross-platform video games with libraries such as [HaxeFlixel](http://haxeflixel.com/), [HaxePunk](http://haxepunk.com/), and [OpenFL](http://www.openfl.org/), all of them working cross-platform.

[**Scheme**](http://en.wikipedia.org/wiki/Scheme_(programming_language)) and [**Racket**](http://racket-lang.org/) are derivations of the ages-old [LISP](http://en.wikipedia.org/wiki/Lisp_(programming_language)) programming language. This family is known for its ridiculous extensibility. If you feel like you're lacking something from the language, it's trivial to just add it! LISP code *is data* -- code is just lists. You can modify these lists and thus modify code *at runtime* as well. Its extensive macro systems provide more flexibility for metaprogramming as well.

They also use *prefix* (or *Polish*) notation. That is, instead of writing operations infix, such as `1 + 2`, you write them prefix, such as `+ 1 2` (or using LISP's S-expressions, `(+ 1 2)`.)

Racket is a great highly-extendable family of languages (which include Scheme) for programming in LISP, and I can recommend it for beginners or otherwise. It is batteries-included, meaning it comes shipped with a lot of useful libraries.

A good place for learning these are the free books [How to Design Programs](http://htdp.org/) and also [Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/), both very well-regarded.

Conclusion
==========

Congratulations, you have read, skimmed or skipped past all of this text. I hope you've found it useful, as it took quite a while to write and annotate with hyperlinks and such. Let me know. If you find a problem, regardless of how small, please feel free to [send a pull request on GitHub](https://github.com/darkf/darkf.github.com) or file an issue about it.

Programming is not a difficult thing to learn, it just requires time and patience. I believe anyone can learn it with the right mindset, and I hope you find it as enjoyable as I do.

If there's one piece of advice I'd like to leave you with, it's "Don't follow other people blindly." Many people will try to tell you, "This is the right way to do this!" or "You should be using this!" Programming is not a "there is only one way to do this" craft - it's an "anything goes" one. It is up to you to decide the best course of action, and that's half the fun!

Good luck and always have fun learning.
