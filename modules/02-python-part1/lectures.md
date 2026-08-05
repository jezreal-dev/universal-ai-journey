# Python Coding, Part 1 – Lectures

📅 Completed — May 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- ✅ Lecture 1: What Computers Do For You  
- ✅ Lecture 2: Logic and Decisions  
- ✅ Lecture 3: Repeating Actions  
- ✅ Lecture 4: Working with Data  
- ✅ Lecture 5: Putting Together Larger Programs  

---

## Lecture 1: What Computers Do For You

### Overview
Ana Bell introduces programming by contrasting what computers excel at (speed, memory, precision) with what humans excel at (creativity, intuition, dealing with ambiguity). Programming bridges this gap by giving computers exact instructions — algorithms — that they can execute step by step.

### Learning Objectives
- Understand how computers follow instructions exactly.  
- Differentiate between human creativity and computer precision.  
- Define programs and algorithms.  
- Recognize Python object types: `int`, `float`, `str`.  
- Write and debug simple expressions, assignments, and functions.  

### Detailed Concepts
- **Expressions**: calculations that evaluate to a single value.  
  - Integers (`int`): whole numbers like `5`, `-10`.  
  - Floats (`float`): decimal numbers like `3.14`, `9.8`.  
  - Strings (`str`): sequences of characters like `"Python"`.  
- **Assignments**: binding names to values using `=`.  
  - Python evaluates the right-hand side first, then assigns the result to the variable name.  
- **Functions**: reusable blocks of code that take inputs and return outputs.  
  - Examples: `print()`, `len()`, `int()`, `float()`.  
- **Precision**: computers don’t infer meaning — they only do what you tell them. Ambiguity leads to errors.  

### Examples
- `area = 3.14 * 9.8 ** 2` → evaluates expression, stores result in memory under `area`.  
- `name = fname + " " + lname` → concatenates strings with a space.  

---

## Lecture 2: Logic and Decisions

### Overview
Introduces decision-making in code using conditionals. Programs become adaptive by evaluating conditions and branching into different paths.

### Learning Objectives
- Write `if`, `elif`, and `else` statements.  
- Use Boolean expressions (`True`, `False`).  
- Compare values with relational operators (`==`, `!=`, `<`, `>`).  
- Debug logical errors.  

### Detailed Concepts
- **Conditionals**: allow programs to make choices.  
- **Boolean logic**: expressions that evaluate to true/false.  
- **String operations**: comparing, slicing, concatenating.  
- **Debugging**: tracing logic errors when code runs but produces wrong results.  

### Example
```python
age = 18
if age >= 18:
    print("You can vote")
else:
    print("Too young")
```

---

## Lecture 3: Repeating Actions

### Overview
Explores loops to automate repetition. Instead of copying code many times, loops repeat tasks efficiently.

### Learning Objectives
- Write `while` loops (repeat while condition holds).  
- Write `for` loops (repeat a set number of times).  
- Use counters and accumulators.  
- Debug infinite loops.  

### Detailed Concepts
- **While loops**: run until condition becomes false.  
- **For loops**: iterate over ranges, lists, or strings.  
- **Counters**: track number of iterations.  
- **Accumulators**: build results across iterations.  
- **Debugging**: use print statements to trace flow.  

### Example
```python
count = 0
while count < 3:
    print("Try again")
    count += 1
```

---

## Lecture 4: Working with Data

### Overview
Introduces lists as a way to store and manipulate collections of data.

### Learning Objectives
- Create and manipulate lists.  
- Index and slice lists.  
- Iterate through lists with loops.  
- Build programs that handle structured data.  

### Detailed Concepts
- **Lists**: ordered collections, e.g. `numbers = [1, 2, 3]`.  
- **Indexing**: `numbers[0]` → first element.  
- **Slicing**: `numbers[1:3]` → subset.  
- **Iteration**: `for n in numbers:` → loop through items.  

---

## Lecture 5: Putting Together Larger Programs

### Overview
Combines all previous concepts into larger, functional programs.

### Learning Objectives
- Modular programming with functions.  
- Combine conditionals, loops, and lists.  
- Debug larger programs.  
- Build interactive applications.  

### Detailed Concepts
- **Functions**: break problems into smaller tasks.  
- **Integration**: use loops, conditionals, and data structures together.  
- **Debugging**: trace errors in multi-function programs.  
- **Applications**: simple games, calculators, or text-based tools.  

---

## My Reflections
- Lecture 1 taught me that programming is about precision — computers only do what we tell them.  
- Lecture 2 showed me how logic makes programs adaptive, and debugging logical errors is crucial.  
- Lecture 3 revealed the power of loops, and how counters/accumulators make repetition useful. Debugging infinite loops was a big lesson.  
- Lecture 4 introduced lists, which made me appreciate how data can be organized and manipulated efficiently.  
- Lecture 5 brought everything together, showing how modular programming builds scalable solutions.  

**Key takeaway:** Programming is about **thinking like a computer** — breaking problems into steps, applying logic, using repetition, and organizing data to build larger, useful programs.  