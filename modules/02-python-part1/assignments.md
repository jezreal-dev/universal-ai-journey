# Assignment 1 – Python Coding, Part 1

📅 Completed — May 2026  
🎓 MIT Open Learning via 3MTT  

---

## Overview
Welcome to Assignment 1!  

In this notebook, you will build a small program that:
- Sets up an input string of physical exercises to do, separated by commas  
- Chooses a random exercise from a list  
- Picks a random number of reps  
- Waits for the user to do the exercise and press Enter to get another exercise  
- If the user types `"done"`, the program quits  
- Tracks stats per exercise (the total reps done for each exercise)  

**Lectures covered in this assignment:**
- Lecture 1: What Computers Do For You  
- Lecture 2: Logic and Decisions  
- Lecture 3: Repeating Actions  
- Lecture 4: Working with Data  
- Lecture 5: Putting Together Larger Programs  

**Logistics:**
- Each code cell defines one function.  
- Every time you make a change to a function in a cell, you must run the cell again for the change to save.  
- Each function will have some fill‑in‑the‑blanks code pieces represented by small `# TODO:` markers.  
- After you complete the function, test it with the provided test cases.  
- The last cell defines `run_session(...)` which calls the others.  

---

## Sample Output
```
Finished loading 5 exercises.
<<<< USER HIT ENTER KEY HERE >>>>>
Picking a random exercise
Generating a random number of reps...
Ready?
Set....
Do 9 plank!
<<<< USER HIT ENTER KEY HERE >>>>>
Picking a random exercise
Generating a random number of reps...
Ready?
Set....
Do 10 lunges!
<<<< USER HIT ENTER KEY HERE >>>>>
Picking a random exercise
Generating a random number of reps...
Ready?
Set....
Do 7 jumping-jacks!
<<<< USER HIT ENTER KEY HERE >>>>>
Picking a random exercise
Generating a random number of reps...
Ready?
Set....
Do 8 lunges!
<<<< USER TYPED "done" HERE >>>>>

Session summary:
push-ups - total reps: 0
squats - total reps: 0
plank - total reps: 9
jumping-jacks - total reps: 7
lunges - total reps: 18
```

---

## Part 1 – Quiz Questions

**Question 1**  
Given the input string `"squats,lunges"`, which of the following are true after calling `load_exercise_list`?  
- The returned list has length 2 ✅  
- The first element is `"squats"` ✅  
- The second element is `" lunges"` (with a space)  
- The function raises an error  
- The function prints *Finished loading 2 exercises.* ✅  

---

**Question 2**  
Which of the following statements about the variable `totals` inside `initialize_stats` are true?  
- It starts as an empty list  
- It grows by appending values inside a loop  
- It contains one element per exercise name ✅  
- It may contain non‑zero values  
- It is returned at the end of the function ✅  

---

**Question 3**  
Which of the following statements about randomness in `pick_random_exercise_index` are true?  
- It uses Python’s random library ✅  
- It selects a random integer using `randint` ✅  
- The randomness is removed by the `time.sleep` call  
- The result is deterministic for the same input  
- The upper bound (right endpoint) is included in the random selection ✅  

---

**Question 4**  
In `pick_random_reps` which of the following are true?  
- The function takes in two inputs ✅  
- It returns an integer or a float  
- The returned value might be `min_reps` ✅  
- The returned value might be `max_reps` ✅  

---

**Question 5**  
What does `record_attempt` do besides returning a value?  
- It changes the value of `reps_this_time`  
- It affects more than one list element  
- It modifies the names list  
- It prints a message to the user  
- It mutates the list passed in as `total_reps` ✅  

---

**Question 6**  
Which of the following behaviors are always true every time `print_instruction` is called?  
- Printing text to the console ✅  
- Paused program execution  
- Modifying global variables  
- Updating a list or dictionary  
- Returning data to the caller  

---

**Question 7**  
In `summarize_stats` which of the following are true?  
- It prints exactly one line every time it's called  
- It prints exactly `len(names)` number of lines every time it's called ✅  
- It prints exactly `len(total_reps)` number of lines every time it's called ✅  
- It sorts exercises alphabetically in the printout  
- It sorts exercises by number of reps in the printout  
- It assumes the input lists `names` and `total_reps` align by index ✅  

---

**Question 8**  
Which of the following assumptions must hold for `handle_round` to work as intended?  
- The index returned by `pick_random_exercise_index` is valid for `names` ✅  
- `total_reps` and `names` correspond index‑by‑index ✅  
- `min_reps` is less than or equal to `max_reps` ✅  
- `total_reps` is a tuple  
- `print_instruction` returns a string that is later used  

---

**Question 9**  
Consider the case where the user presses Enter first, then types `"done"` next. Which of the following are true?  
- Exactly 9 program‑defined functions are called ✅  
- `handle_round` is called exactly once ✅  
- `summarize_stats` is called exactly once ✅  
- `pick_random_exercise_index` is never called  
- `record_attempt` is called exactly once ✅  

---

## Assignment Summary
In this assignment, we applied Python functions to build and analyze a simple exercise session program.  

**Key takeaways:**
- `load_exercise_list` parses a string into a list of exercises, demonstrating string handling and list creation.  
- `initialize_stats` returns parallel lists of names and totals, reinforcing alignment between data structures.  
- `pick_random_exercise_index` and `pick_random_reps` illustrate randomization, ensuring variation in exercise selection and repetitions.  
- `record_attempt` shows how to mutate specific elements in a list, highlighting in‑place updates versus creating new objects.  
- `print_instruction` demonstrates the difference between printing output and returning values.  
- `summarize_stats` organizes and prints statistics, emphasizing alignment between inputs and outputs.  
- `handle_round` and `run_session` integrate all functions into a loop‑driven session, showing how modular components combine into a complete interactive program.  
