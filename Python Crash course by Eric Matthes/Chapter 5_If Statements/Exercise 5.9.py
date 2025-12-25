usernames = ['admin', 'john', 'sarah', 'mike', 'anna']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, Welcome back!.")

else:
    print("\nWe need to find some users!")


for username in usernames:
    usernames.clear()

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, Welcome back!.")

else:
    print("\nWe need to find some users!")



"""
## What’s going wrong (core issue)

❌ You are **modifying a list while iterating over it**

```python
for username in usernames:
    usernames.remove(username)
```

When you remove items from a list **while looping over it**, 
Python’s internal index moves forward and **skips elements**.

---

## Step-by-step what actually happens

Initial list:

```python
['admin', 'john', 'sarah', 'mike', 'anna']
```

### Iteration 1

* `username = 'admin'`
* Remove `'admin'`
* List becomes:

```python
['john', 'sarah', 'mike', 'anna']
```

### Iteration 2

* Loop moves to the **next index**
* `'john'` is **skipped**
* `username = 'sarah'`
* Remove `'sarah'`
* List becomes:

```python
['john', 'mike', 'anna']
```

### Iteration 3

* Next element → `'anna'`
* Remove `'anna'`
* List becomes:

```python
['john', 'mike']
```

Loop ends.

---

## Final list after the loop

```python
['john', 'mike']
```

So this condition:

```python
if usernames:
```

evaluates to **True**, because the list is **not empty**.

Therefore, the `else` block **never runs**.

### ✔️ Option 1: Clear the list (best)
usernames.clear()
"""