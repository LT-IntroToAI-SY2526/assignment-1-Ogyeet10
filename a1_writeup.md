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

After completing your problems, reflect on:

1. **What was your initial experience with Python?** How did it compare to other programming languages you've used?
   Coming from JavaScript and TypeScript, Python felt concise and readable. Indentation-as-syntax took a minute to adjust to compared to braces, but less boilerplate made it faster to experiment. Dynamic typing let me prototype quickly, while optional type hints gave me some of the safety I'm used to from TypeScript.

2. **How did you use AI effectively?** Give specific examples of good prompts you used and what you learned from the responses.
   I prompted the AI to generate 5 problems that increased in difficulty and covered specific topics (conditionals, loops, strings, lists, and a small algorithm). I asked for example inputs/outputs to clarify behavior. I then implemented solutions and added asserts. When designing `compress_string`, the AI’s suggestion to handle single-character runs without a number made the output cleaner.

3. **What concepts were most challenging?** How did AI help you understand them?
   Edge-case handling was the trickiest. Like empty inputs, zero divisors in `sum_of_multiples`, and lists with too few unique values for `second_largest`. The AI nudged me to think about guards (skip zero divisors) and to raise a `ValueError` when inputs are insufficient.

4. **What did you learn about collaborating with AI?** What strategies worked best for learning rather than just getting answers?
   I found that asking specific questions while coding helped me understand the problems better. When I got stuck on edge cases, I'd ask the AI "what should happen if the list is empty?" or "how do I handle when there aren't enough unique numbers?" This helped me think through the logic myself rather than just copying solutions.
