"""
A single Python dictionary can contain just a few key-value
pairs or millions of pairs. Because a dictionary can contain
large amounts of data, Python lets you loop through a
dictionary. Dictionaries can be used to store information in a
variety of ways; therefore, several different ways exist to
loop through them. You can loop through all of a dictionary’s
key-value pairs, through its keys, or through its values.
"""

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")



"""
**Straight to the point:**

### 1️⃣ `for key in dict_name:`

* Iterates over **keys only**
* This is the **default behavior** when looping through a dictionary

```python
for key in my_dict:
    print(key)
```

Equivalent to:

```python
for key in my_dict.keys():
    print(key)
```

---

### 2️⃣ `for key, value in dict_name.items():`

* Iterates over **both keys and values at the same time**
* Use this when you need **access to the value** inside the loop

```python
for key, value in my_dict.items():
    print(key, value)
```

---

### ❌ What does **not** work

```python
for key, value in dict_name:
```

This is **invalid** because looping over a dict directly yields 
**only keys**, not `(key, value)` pairs.

---

### ✅ When to use which

| Use case                | Correct loop                           |
| ----------------------- | -------------------------------------- |
| Only need keys          | `for key in dict_name:`                |
| Need both key and value | `for key, value in dict_name.items():` |
| Only values             | `for value in dict_name.values():`     |

---

### 🧠 One-line takeaway

> **Dictionaries iterate over keys by default; use `.items()` 
when you want both keys and values.**

"""