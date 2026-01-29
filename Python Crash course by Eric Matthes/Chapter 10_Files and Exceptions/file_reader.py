from pathlib import Path

path = Path('pi_digits.txt') 
contents = path.read_text() 
print(contents)

r"""
### What’s actually going wrong

python
path = Path('pi_digits.txt')


This **does NOT mean** “the folder where `file_reader.py` lives”.

It means:

> “Look for `pi_digits.txt` in the **current working directory** (CWD) 
from which Python was launched.”

From your terminal output 👇

text
PS C:\Users\HP\OneDrive\Documents\python_work>

That is your **current working directory**.

But your script is actually here:

text
C:\Users\HP\OneDrive\Documents\python_work\
Python Crash course by Eric Matthes\
Chapter 10_Files and Exceptions\
file_reader.py

So Python is searching for:
text
C:\Users\HP\OneDrive\Documents\python_work\pi_digits.txt

…and the file is **not there**, hence:


FileNotFoundError: No such file or directory: 'pi_digits.txt'

## 🔍 Quick way to debug this yourself

Add this temporarily:

python
from pathlib import Path
print(Path.cwd())


That prints the exact directory Python is using to look for files.

---

## ⚠️ Common beginner pitfall (you did nothing wrong)

Many beginners think:

> “Same folder as the file”

Python thinks:

> “Same folder as where the command was run”

You just learned an important real-world Python rule 👌

---

## ✅ Alternative quick fixes (less ideal)

### Option 1: Run Python from the script’s folder

powershell
cd "Python Crash course by Eric Matthes\Chapter 10_Files and Exceptions"
python file_reader.py


### Option 2: Use absolute path (not recommended long-term)

python
Path(r"C:\Users\HP\OneDrive\Documents\python_work\...\pi_digits.txt")


---

## 🔑 Takeaway (remember this forever)

> **Relative paths are relative to the current working directory, NOT the script file.**
> Use `Path(__file__).parent` when you want “same folder as this script”.

"""