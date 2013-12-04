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

I'll give you one piece of advice now: Don't just read. Do. If you just read a book or tutorial, but don't engage yourself and write (and then fix) your own programs, you're not going to get the full experience, and you will likely just forget what you learned. Don't be afraid to experiment -- that's what it's all about!

What technology should I pick?
==============================

This question, or one of its variants ("What programming language should I use?") is probably the most common out there. There are many factors in deciding which tech to use out there, and it depends wholly on your goals.

I will separate at the high level two different kinds of programmers: those who want to learn for **education** (i.e., "This is interesting, I want to know more!"), or for **monetary gain** (i.e., "Wow, this is a lucrative business, I want to get in on this!").

Those leaning more towards the educational benefit might be more interested in learning the foundations of programming well before moving on to tackling large code frameworks and making world-class applications with them. It is very valuable to have a good grasp on these fundamentals as it will make many things easier for you.

Those more for business will probably tend to go for the more applicative side, wanting to dive into learning how to make applications that people can use right away.

Thankfully there is not much difference between these two in terms of technologies used, and you should know that **it does not matter where you start**: across your programming career you will learn many technologies, the paths of the businessman and the hobbyist will always intersect at some point. The end goal is the achievable "I can write, maintain and understand software".

There is a lot of confusion surrounding what programming language to pick when learning. Some parties might recommend using [C++](http://en.wikipedia.org/wiki/C++), some [C#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)), or some something else entirely. Again, it does not matter where you start, however some programming languages are easier to get started *learning how to program*. You want to strike a balance between these.

Programming Languages: Beginner Summary
==============================

If you're just starting off, here's a list of great and popular languages for beginners and experienced programmers alike. If you're just starting off, I recommend skipping the next sections (don't worry, they're just filled with [technobabble](http://en.wikipedia.org/wiki/Technobabble) rambling) and jumping to the conclusion, then diving into your language of choice! Pick one that sounds the most fun to you.

I recommend you steer clear of pay sites that offer you courses to learn. You can get by just fine (if not better) using only free resources. Some of these sites give a very superficial overview and I cannot recommend them.

Now, on to the list:

[**Python**](http://en.wikipedia.org/wiki/Python_(programming_language)) is an amazing general-purpose language that will let you go far and wide. It's easy to pick up, beginner-friendly, powerful, robust, well-designed, and comes batteries-included with tons of libraries for you to play with and make cool things. I recommend it as a first language and to anyone else.

You can start learning it now using [Learn Python The Hard Way](http://learnpythonthehardway.org/). You can skip installing it at first if you want to and try it in your browser with [repl.it](http://repl.it/).

As an example of what Python looks like, observe the following program:

    nums = raw_input("Enter a list of numbers: ").split(" ")
    print(sum(int(num) for num in nums))

Can you figure out what it does? I'll give you a spoiler: It asks the user on the command line for a list of numbers, separated by spaces, and then returns their sum. Python can read very much like English, for example, the above could also be written more verbosely:

    total = 0
    inputs = raw_input("Enter a list of numbers: ").split(" ")
    for number in inputs:
        total = total + int(number)
    print(total)

For some cool libraries (code written by others that you can use to build things), check out the following:

  - [**Flask**](http://flask.pocoo.org/) for building websites
  - [**pygame**](http://www.pygame.org/news.html) for building video games and other graphical applications
  - [**Ren'Py**](http://www.renpy.org/) for building [Visual Novel](http://en.wikipedia.org/wiki/Visual_novel) games
  - [**numpy**](http://www.numpy.org/) for numerical processing


[**Ruby**](http://en.wikipedia.org/wiki/Ruby_(programming_language)) is another good general-purpose language, and is very similar to Python. An example of it:

    total = 0
    print "Enter a list of numbers: "
    gets.split(/ /).each do |input|
    total = total + input.to_i
    end
    puts total

It's quite a bit different, but close nonetheless.

To get started learning Ruby, try out the [Poignant Guide to Ruby](http://www.rubyinside.com/media/poignant-guide.pdf), possibly with [tryruby](http://tryruby.org/levels/1/challenges/0).

For some cool stuff to use to build your programs:

  - [**Sinatra**](http://www.sinatrarb.com/) for building websites

[**C#**](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)) is a good general-purpose language as well; this time diverging from Python or Ruby by being *statically typed* -- meaning you need to tell the computer what *type* (such as number, text, date, etc) a value is. Here's what our example program looks like in C#:

    using System;

    class Program
    {
        static void Main()
        {
            int total = 0;
            string[] inputs = Console.ReadLine().Split(' ');
            foreach(string input in inputs) {
                total = total + int.Parse(input);
            }
            Console.WriteLine(total);
        }
    }

Don't be scared by its relative size -- 4 lines of that is usually generated by your [Integrated Development Environment](http://en.wikipedia.org/wiki/Integrated_development_environment), or IDE. The rest is mostly due to giving it the types of *variables* such as total, inputs, and input. This lets you make sure that you're not accidentally adding text such as `"quack"` to a number such as `5`.

C# is also great for building graphical ([GUI](http://en.wikipedia.org/wiki/Graphical_user_interface)) applications, most IDEs featuring a powerful drag-and-drop designer.

To get started learning C#, I recommend getting an IDE:

- [Visual C# Express Edition](http://www.visualstudio.com/en-US/products/visual-studio-express-vs) is a free, official IDE for C# from Microsoft. Windows only.
- [SharpDevelop](http://www.icsharpcode.net/opensource/sd/) is a free third-party IDE for Windows.  
- [MonoDevelop](http://monodevelop.com/) is a free, [open source](http://en.wikipedia.org/wiki/Open_source) IDE for Windows, Linux, Mac OS X, and other more obscure platforms. It also comes shipped with [Unity3D](http://unity3d.com/).

If you're on a non-Windows platform, you'll probably want to grab MonoDevelop and a copy of the [Mono](http://www.mono-project.com/Main_Page) compiler.

To get started learning C#, check around your favorite search engine for some tutorials that fit you, or maybe try out the book [Head First C#](http://www.amazon.com/Head-First-C-Jennifer-Greene/dp/1449343503).

For some cool stuff to use to build programs using C#:

  - [MonoTouch](http://xamarin.com/ios) to create iOS and Android apps
  - [MonoGame](http://monogame.codeplex.com/) for video games supporting Windows, Linux, OS X, iOS, Android, and other platforms. Replaces the [Microsoft XNA](http://en.wikipedia.org/wiki/Microsoft_XNA) framework and is generally compatible with it. Indie game developers love this.

The [Unity3D](http://unity3d.com/) video game engine lets you use C# with it as well.


Now get to it!

Programming Languages and Libraries: Long Version
=====================

Now that you know some parlance, let's tackle some common technologies and their uses:

Some sects, such as **video game programmers**, often use [C++](http://en.wikipedia.org/wiki/C++) and [C#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)).
C++ is a notoriously massive and arduous language, with historical artifacts from C. Modern ([C++11](http://en.wikipedia.org/wiki/C++11) and soon to be [C++14](http://en.wikipedia.org/wiki/C%2B%2B14)) C++ is often written at a higher level (using features such as iterators, smart pointers, references, etc.) than more archaic C++ (which often use C remnants such as unwrapped arrays, raw pointers, et cetera.)

[**C++**](http://en.wikipedia.org/wiki/C++) is not necessarily a bad place to end up, but it might not be the best for beginning. Should you ever choose it, however, [C++ Primer](http://www.amazon.com/Primer-5th-Edition-Stanley-Lippman/dp/0321714113) (not to be confused with C++ Primer Plus) is a good place to start.
[C++ Reference](http://en.cppreference.com/w/) is a great reference site to use as well.
C++ is good for low-level systems programming (such as operating systems, or video games) that require high performance. It does sacrifice quite a lot of [type safety]() to achieve that, compilation times can be slow, and the process of compilation is often tedious.

[**C#**](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)) is not a bad place to start. It is a statically-typed object-oriented language in the style of *Java*. Visual C# (Microsoft's IDE) and [SharpDevelop](http://www.icsharpcode.net/opensource/sd/) (a third-party one) provide an easy but powerful drag-and-drop interface for creating graphical (GUI) applications. [Mono](http://www.mono-project.com/Main_Page) (and [MonoGame](http://monogame.codeplex.com/) for video games) is a good framework for building applications and deploying them to PC, Mac, iOS, Android, and other platforms.

[**Python**](http://en.wikipedia.org/wiki/Python_(programming_language)) is an dynamically-typed object-oriented/functional interpreted language. It is a great beginner language, but not just for them - it is extremely capable and great for small and mid-sized tasks.
It offers high-level features, such as first-class functions, object orientation, modules to cleanly separate source code, and operations for easily working with text, lists, sets, mappings, etc. Being dynamically typed means it will not be able to catch type errors (such as adding a string to a number) at compile-time (i.e. when you first launch the program), but only at run-time (i.e., when the faulty expression is evaluated.) With proper practice this is usually not much of an issue.

A good resource for learning Python is [Learn Python The Hard Way](http://learnpythonthehardway.org/).

For Web development, Python has some good libraries: [**Flask**](http://flask.pocoo.org/) for building from the foundation up, and [**Django**](https://www.djangoproject.com/) for re-using parts made by other people. There is also Pyramid, Pylons, etc.
For video games, [**Pygame**](http://www.pygame.org/news.html) is a nice framework, as well as [Pyglet](http://www.pyglet.org/) and [Cocos2D](http://cocos2d.org/). There are some 3D engines like [Panda3D](https://www.panda3d.org/) used by, for example, Disney Interactive.
Scientists often use Python as well for numerical calculations, with [numpy](http://www.numpy.org/) and [scipy](http://www.scipy.org/).

[**Ruby**](http://en.wikipedia.org/wiki/Ruby_(programming_language)) is also a dynamic interpreted language like Python, but with more loose, expression-based syntax. It borrows a lot of concepts from good ol' [Smalltalk](http://en.wikipedia.org/wiki/Smalltalk).

A good resource for learning Ruby is [The Poignant Guide to Ruby](http://www.rubyinside.com/media/poignant-guide.pdf) or one of the other [good resources](https://www.ruby-lang.org/en/documentation/) available.

For Web development, [**Sinatra**](http://www.sinatrarb.com/) is a good and elegant microframework, and [**Rails**](http://rubyonrails.org/) is a **very** popular heavier framework.

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
