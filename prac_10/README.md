# Practical 10
# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

The initial estimates were not very accurate: simple tasks were always underestimated, 
while complex tasks were overestimated. Most tasks actually took 10% to 30% more time than I guessed.

### How did your estimate accuracy improve or change during the course of the subject?

After doing a lot of exercises, you will break down tasks into small steps instead of guessing the overall time.
You will also refer to the time taken for similar tasks before. For example, if you remember that it took 30 minutes to write a loop function before,
you will guess that a new one will take about the same amount of time.

### What did you learn from doing these estimates?

Estimation is not just about calculating time; it also involves clearly understanding the requirements and considering risks in advance. 
It is necessary to set aside time for debugging. This has helped me avoid last-minute rushes and prioritize tasks when dealing with multiple ones.

## Code Reviews

### What have you learned from being reviewed by other people?

Having others review my code made me realize that it's not enough for code to just run; it also needs to be easy to understand and maintain. 
They can spot the syntax errors I missed and point out simpler ways of writing, and I've learned quite a few Python tips.

### What have you learned from doing code reviews of other people?

Reviewing others' code makes me more aware of coding standards. During the process of reading others' code, I discovered many common mistakes 
(such as not handling null values), and I will avoid them when writing my own code.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

https://github.com/Stephen-Keith-Lubega/cp1404practicals/pull/4

### Explanation

I provided useful and specific suggestions: the author did not validate the user input, 
so I told him that he could add a try-except block to help him clarify his thoughts. 
I also praised him for writing the loop clearly, and my tone was not blunt.

### Good Code Review 2

https://github.com/Stephen-Keith-Lubega/cp1404practicals/pull/4

### Explanation

In fact, I only received this review request, so I will continue to analyze and summarize based on the content of this request.
The author used redundant loops to filter the list. I suggested using list comprehensions and also wrote a code example, 
telling him that this method is more concise and faster. I also praised him for his clear comments.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

Some actual tasks are relatively long and require completing multiple small pieces of code. These long tasks can be split into small, 
short tasks and completed in sequence to prevent everyone from rushing to finish at the end.

### What did you do really well for practicals in this subject?

I'm good at breaking down tasks into small steps. After writing a function, I run a test immediately.
Finding bugs early saves time. In addition, I write comments for the code and take simple study notes, 
which can be useful later when reviewing or working on other tasks.