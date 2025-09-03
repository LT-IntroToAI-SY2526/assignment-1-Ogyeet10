# Assignment 1 - Write UP

## Description

This is the portion of the assignment that will be graded. I will be looking at your other files, and specifically either `a1.py` or `a1_practice_problems.py`. I will be looking to see that you completed the problems or used a generative AI to help you come up with and complete some challenge questions. This document will help guide you through that process.

## What You Need to Submit

1. **Complete the `a1_practice_problems.py` in class**. Mr. Berg will push solutions to github
2. **Complete the `a1.py` file** with your AI-generated problems and solutions
3. **Complete the reflection questions** in `a1_writeup.md`
4. **Push your changes to GitHub**

Mr. Berg will look at all your files to determine what you have completed. If there are any questions for this assignment, Mr. Berg will ask in class after he grades them.

## Reflection Questions

After completing my problems, here are my reflections:

1. **What was your initial experience with Python?**
   I found Python syntax straightforward compared to Java. Indentation-based blocks and no type declarations for local variables made writing small functions fast. The tradeoff is that I had to be disciplined with tests and clear naming to avoid silent type issues. The REPL-style feedback and simple list operations felt very productive.

2. **How did you use AI effectively?**
   I started with a focused prompt to generate a balanced set of 6 problems touching variables, conditionals, loops, functions, and list operations. When implementing, I asked for conceptual guidance rather than finished code, like: “Explain the approach for FizzBuzz without giving full code,” and “What’s a clean way to reverse words while normalizing spaces?” This kept me in control of the implementation while still leveraging AI for strategy and edge cases.

3. **What concepts were most challenging?**
   The trickiest parts were handling edge cases (e.g., empty lists for `max_in_list`, normalizing whitespace for `reverse_words`) and ensuring consistent return types (like float for `median` in even-length lists in the practice file). AI helped by suggesting guard clauses, clarifying Python idioms (`split()` behavior on whitespace), and reminding me to raise `ValueError` for invalid inputs.

4. **What did you learn about collaborating with AI?**
   The best strategy was to iterate: write a first pass, then ask targeted questions about specific decisions or potential pitfalls. Asking for “hints,” “edge cases to consider,” and “explanations of why an approach works” led to understanding rather than copy-paste solutions. I also verified AI suggestions by writing asserts and running tests, which caught mistakes early.
