favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

"""
When you know you’ll need more than one line to
define a dictionary, press ENTER after the opening brace.
Then indent the next line one level (four spaces) and write
the first key-value pair, followed by a comma. From this
point forward when you press ENTER, your text editor
should automatically indent all subsequent key-value pairs
to match the first key-value pair

Once you’ve finished defining the dictionary, add a closing
brace on a new line after the last key-value pair, and indent
it one level so it aligns with the keys in the dictionary. It’s
good practice to include a comma after the last key-value
pair as well, so you’re ready to add a new key-value pair on
the next line.

Most editors have some functionality that helps you
format extended lists and dictionaries in a similar
manner to this example. Other acceptable ways to
format long dictionaries are available as well, so you
may see slightly different formatting in your editor, or
in other sources.
"""

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")



taken_poll =[]
for name in favorite_languages:
    taken_poll.append(name)

if 'erin' not in taken_poll:
    print("Erin, please take our poll!")

"""
The keys() method isn’t just for looping: it actually returns
a sequence of all the keys
"""

"""
**Short answer:**
❌ **Fewer lines does NOT automatically mean more efficient.**

---

## What “efficient” actually means

Efficiency can mean different things:

1. **Runtime performance (speed)**
2. **Memory usage**
3. **Code clarity & maintainability**
4. **Pythonic / idiomatic style**

Line count alone measures **none** of these reliably.

---

## Comparing your two examples

### ✅ Version 1 (Direct check)

```python
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
```

### ❌ Version 2 (Indirect check)

```python
taken_poll = []
for name in favorite_languages.keys():
    taken_poll.append(name)

if 'erin' not in taken_poll:
    print("Erin, please take our poll!")
```

---

## Efficiency breakdown

### 🔹 Runtime (Big-O)

Both are **O(n)** in the worst case, but:

* Version 1 performs **one membership check**
* Version 2:

  * Loops through all keys
  * Builds a new list
  * Then performs another membership check

➡️ **Version 1 is faster**

---

### 🔹 Memory usage

* Version 1: **No extra memory**
* Version 2: Creates a new list (`taken_poll`)

➡️ **Version 1 uses less memory**

---

### 🔹 Readability & correctness

* Version 1:

  * Clear intent
  * Idiomatic Python
* Version 2:

  * More code
  * More places for bugs
  * Redundant logic

➡️ **Version 1 is better**

---

## Important Python detail (key insight)

This part:

```python
favorite_languages.keys()
```

is **unnecessary**.

The most efficient and Pythonic version is:

```python
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")
```

Why?

* Dictionaries check **keys by default**
* `.keys()` is implied

---

## Final verdict

| Criterion      | Fewer lines = better? |
| -------------- | --------------------- |
| Speed          | ❌ Not always          |
| Memory         | ❌ Not always          |
| Readability    | ❌ Sometimes           |
| Pythonic style | ❌ Sometimes           |

### ✅ In this case:

* Fewer lines **are** more efficient
* But the real reason is **less work**, not fewer lines

---

## One-sentence takeaway

> **Efficiency comes from doing less work, not from writing fewer lines of code.**
"""



"""
Looping through a dictionary returns the items in the same
order they were inserted. Sometimes, though, you’ll want to
loop through a dictionary in a different order.
One way to do this is to sort the keys as they’re returned
in the for loop. You can use the sorted() function to get a
copy of the keys in order
"""

for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


"""
 To see
each language chosen without repetition, we can use a set.
A set is a collection in which each item must be unique:
You can build a set directly using braces and
separating the elements with commas:

It’s easy to mistake sets for dictionaries because
they’re both wrapped in braces. When you see braces
but no key-value pairs, you’re probably looking at a
set. Unlike lists and dictionaries, sets do not retain
items in any specific order.
"""
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())