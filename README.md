# WORDIS

A command-line Wordle-style word guessing game built in Python.

## What it does
- Picks a random word from a word list (`Testwords.txt`)
- Player guesses words of the same length
- Shows correct letters in place, and tracks misplaced/incorrect letters separately
- Ends on a correct guess or after 6 turns

## Requirements
- Python 3
- No external dependencies (only built-in `random` module)

## How to run it
```bash
git clone https://github.com/Dextro111/WORDIS.git
cd Wordis
python3 main.py
```
Make sure `Testwords.txt` is in the same directory as `main.py` — it needs one word per line.

## Example
<img width="1599" height="868" alt="wordis_Output" src="https://github.com/user-attachments/assets/839f83fb-03d5-4f58-a01f-0306243e100b" />


## What Can Be learned
- Comparing guesses letter-by-letter using index tracking
- Handling input validation (length check, alpha-only check)
- Using lists to track misplaced vs incorrect letters across turns
- Reading a word list from a text file into a list

