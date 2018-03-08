---
layout: post
title: "How I Write Code"
date: 2013-03-10
---

I woke up today and thought, "I should document the method I use to write code, even if it's not useful to anyone!" So, here I go.


I like to think of writing code as a bit like how an artist might workflow a drawing. With some idea of what they want to create, they begin work on the skeleton - blocking out the rough shapes and outlines. Once that has taken shape, they refine edges, erase blocks, and fill them in with detailed curves and lines. After all this is done, they start polishing and painting, until they arrive at the mostly final piece - a canvas of art that is hopefully pretty to look at!


Let's see how we can apply this workflow to programming.


## Skeleton ##

There are different ways to approach this that professional programmers use. Perhaps the  most commonly known is Test-Driven Development, where programmers write unit tests to describe how their program should behave before even implementing it.


I prefer to define just the *interface* of the program first. By interface I mean a rough block-out of functions or methods and of data members - not implementing anything, just defining a loose structure.

As an example, say we're making a banking application (boring, I know!) where accounts hold a balance, can withdrawl and deposit currency. Let's define a Java interface for this:

    public class Account {
        private double balance = 0; /** The amount of currency the account holder currently has. */
        
        /** Get the account balance */
        private double getBalance() {
        }
        
        /** Set the account balance */
        private void setBalance(double newBalance) {
        }
        
        /** Withdrawl currency from the account */
        private void withdrawl(double amount) {
        }
        
        /** Deposit currency to the account */
        private void deposit(double amount) {
        }
        
        /** Is the user overdrawn? */
        private bool isOverdrawn() {
        }
    }

Of course, you wouldn't use a `double` for real-world financial code, but that's the beauty of examples!
If you find that something doesn't work, it is very easy to change things at this stage. Once you're *done* (hint: you're never *really* done) you have a nice specification. What's left is basic implementation!


## Minimal Implementation ##

Programming is an incremental process. Instead of just implementing all of the features and then testing it, why don't we write the most fundamental features first, and then test those? Let's roghly block in the implementation of our account. Overdrawing functionality isn't crucial right now, so let's do the rest and stub `isOverdrawn`:

    public class Account {
        private double balance = 0; /** The amount of currency the account holder currently has. */
        
        /** Get the account balance */
        private double getBalance() {
            return balance;
        }
        
        /** Set the account balance */
        private void setBalance(double newBalance) {
            balance = newBalance;
        }
        
        /** Withdrawl currency from the account */
        private void withdrawl(double amount) {
            balance -= amount;
        }
        
        /** Deposit currency to the account */
        private void deposit(double amount) {
            balance += amount;
        }
        
        /** Is the user overdrawn? */
        private bool isOverdrawn() throws Exception {
            throw new Exception("Not implemented");
        }
    }
    
    
There! That was easy. We just went through and implemented what functionality we needed, and left the rest to do afterwards. You might ask why we don't just return some dummy value like `false` in `isOverdrawn` - what if we forget that it's not implemented? We might use it thinking that it works, and we'd be scratching our heads. Instead, a clear error such as this indicates that you need to fill in some more code!

## Final Touches ##

For completeness we'll implement the remaining method:

        /** Is the user overdrawn? */
        private bool isOverdrawn() {
            return balance < 0;
        }
        
And now any code that uses ours *should* work! We might want to add tests afterwards to verify, but it works! We have a program, built incrementally from a few basic steps.


## Conclusion ##

Unfortunately, you can't pull something out of nothing. What you can do is take things, transform them, and use them as building blocks to something. Programming is just a puzzle - given some things in your toolbox (loops, recursion, conditionals, etc), how do you combine those things to make a coherent program that does what you want?

Things are as simple as you want to make them. You shouldn't worry too much about *how* you do things as long as it works for you. If you're going to drink kool-aid, drink yours, not others' for the sake of it!

Happy Hacking.