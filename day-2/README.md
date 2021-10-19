# This is the stuff we did on day 2

* Learned about redirection of standard input, output, and error
* We learned about [git](https://en.wikipedia.org/wiki/Git).
* Point number three for Lara

## For loop in a list

```python
ages = [45, 22, 19, 10]

total = 0

for age in ages:
    print('The current age is', age)
    total = total + age
    print('The total is now', total)
The current age is 45
The total is now 45
The current age is 22
The total is now 67
The current age is 19
The total is now 86
The current age is 10
The total is now 96
```

## Homework

This is based on the most common word Python program.

* Only print words that have more than e.g., 500 occurrences.
* Print out how many words there are in total.
* Convert all words to lower case. Hint: strings have a method called
  `lower()`.
* Print out all the words with the highest count (there may be many). Hint:
  use a `set` to keep track of the most common words. I.e., detect draws.
