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

### ls

We talked about `ls` versus `ls -l` and the `t` and `r` flags.

## Permissions

`ls -l` shows you the permissions at the start of each line of output:

```sh
$ ls -l
total 8
-rw-rw-r--   1 terry  staff  259 Oct 19 14:50 README.md
drwxrwxr-x   5 terry  staff  160 Oct 19 11:32 admin
drwxrwxr-x  10 terry  staff  320 Oct 19 15:17 day-1
drwxrwxr-x   5 terry  staff  160 Oct 19 15:51 day-2
```

## Conveniently run your Python scripts

Three steps:

1) Make your Python files executable:

```sh
$ chmod +x *.py
```

Use `a` (or nothing) for all, `u` for the user/owner of the file (`terry`
above), `g` for group (`staff` above), or `o` for others (the public).

2) Add `#!/usr/bin/env python` as the first line of your Python scripts.

3) Make sure you have `.` in your shell `PATH` environment variable (you
only need to do this once). This will be discussed on day three.

## File

There is a command called `file` which can tell you (or guess) the type of
the contents of a file.

## Homework

This is based on the most common word Python program.

* Only print words that have more than e.g., 500 occurrences.
* Print out how many words there are in total.
* Convert all words to lower case. Hint: strings have a method called
  `lower()`.
* Print out all the words with the highest count (there may be many). Hint:
  use a `set` to keep track of the most common words. I.e., detect draws.
