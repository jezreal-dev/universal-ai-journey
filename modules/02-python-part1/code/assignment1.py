import random
import time

def load_exercise_list(csv_text):
    """
    - csv_text is a string of exercise names separated by commas
      e.g. "squats,plank,jumping-jacks"

    Return a list whose elements are strings of exercise names.
    """
    items = csv_text.split(",") # split the input string into a list of exercise names

    print(f"Finished loading {len(items)} exercises.")
    return items

# Test your function with these two test cases:
ex1 = "push-ups,squats,plank,jumping-jacks,lunges"
print(load_exercise_list(ex1))
print()
ex2 = "squats,lunges"
print(load_exercise_list(ex2))


# 2) Initialize lists to keep track of exercise stats
def initialize_stats(names):
    """
    - names is a list of exercise names
    
    Return a list that contains as many zeroes as there are exercise names in names.
    """
    totals = []
    for i in range(len(names)):
        totals.append(0)  # TODO fixed
    return totals

# Test your function with these two test cases:
ex1 = ['push-ups', 'squats', 'plank', 'jumping-jacks', 'lunges']
print(initialize_stats(ex1))     # should print [0, 0, 0, 0, 0]

print()
ex2 = ['squats', 'lunges']
print(initialize_stats(ex2))     # should print [0, 0]


# 3) Pick a random exercise from exercise list
def pick_random_exercise_index(values):
    """
    - values is a list of exercise strings
    Return a random index representing the exercise chosen, between 0, and len(values)-1] 
    """
    print("Picking a random exercise")
    time.sleep(1)
    idx = random.randint(0, len(values)-1)
    return idx


# Test your function with these two test cases. 
# Different functions runs will give different values because of randomness. 
ex1 = ['push-ups', 'squats', 'plank', 'jumping-jacks', 'lunges']
print(pick_random_exercise_index(ex1))

print()
ex2 = ['squats', 'lunges']
print(pick_random_exercise_index(ex2))


# 4) Pick a random number of reps between min_reps and max_reps (inclusive)
def pick_random_reps(min_reps, max_reps):
    """
    min_reps and max_reps are non-negative integers
    
    Return a random integer within the input range,
    representing how many reps to do.
    """
    print("Generating a random number of reps...")
    time.sleep(1)
    
    reps = random.randint(min_reps, max_reps)
    
    return reps

# Test your function with these two test cases. 
# Different functions runs will give different values because of randomness. 
print(pick_random_reps(5, 20))
print()
print(pick_random_reps(15, 50))


# 5) Update stats when an exercise is assigned
def record_attempt(index, total_reps, reps_this_time):
    """
    - index is the index of the randomly chosen exercise
    - total_reps is the list representing the total_reps done for each exercise
    - reps_this_time is the randomly chosen number of reps this round
    
    Increment the total_reps list at the appropriate exercise location by 
    reps_this_time. total_reps list is mutated and returned.
    """
    total_reps[index] = total_reps[index] + reps_this_time
    return total_reps


# Test your function with these two test cases:
idx1 = 1
total_reps1 = [0,0,0,0,0]
reps1 = 9
print(record_attempt(idx1, total_reps1, reps1))

print()
idx2 = 4
total_reps2 = [2,12,17,9,3]
reps2 = 20
print(record_attempt(idx2, total_reps2, reps2))


# 6) Produce a friendly instruction line
def print_instruction(exercise_name, reps):
    """
    - exercise_name is a string
    - reps is an int
    
    Print an instruction string.
    e.g. 'Do 12 push-ups!'
    """
    print("Ready?")
    time.sleep(1)
    print("Set....")
    time.sleep(1)
    
    print(f"Do {reps} {exercise_name}!")


# Test your function with these two test cases:
ex1 = 'lunges'
r1 = 15
print_instruction(ex1, r1)

print()
ex2 = 'push-ups'
r2 = 8
print_instruction(ex2, r2)


# 7) Build a simple multi-line summary of stats
def summarize_stats(names, total_reps):
    """
    - names is the list of exercise names
    - total_reps is the list of total reps for each exercise
    The lists are matched up, index-by-index.

    Return a string with one line per exercise: 
    e.g. push-ups - 12
        squats - 39
    """
    
    for i in range(len(names)):
        print(f"{names[i]} - total reps: {total_reps[i]}")


# Test your function with these two test cases:
n1 = ['push-ups', 'squats', 'plank', 'jumping-jacks', 'lunges']
r1 = [2, 12, 17, 9, 23]
summarize_stats(n1, r1)

print()
n2 = ['plank', 'lunges']
r2 = [1, 100]
summarize_stats(n2, r2)


# 8) Handle one round: choose exercise + reps, update stats, show instruction
def handle_round(names, total_reps, min_reps, max_reps):
    """
    - names is the list of string exercsie names
    - total_reps is the list of reps done, where the value at the index here corresponds to the exercise in names
    - min_reps is the lower bound for randomly choosing a number of reps
    - max_reps is the upper bound for randomly choosing a number of reps

    Pick an exercise and reps, update stats, and return the new total_reps list.
    """
    
    idx = pick_random_exercise_index(names)
    reps = pick_random_reps(min_reps, max_reps)
    
    print_instruction(names[idx], reps)  
    total_reps = record_attempt(idx, total_reps, reps)  
    
    return total_reps


# Test your function with this test case:
n1 = ['push-ups', 'squats', 'plank', 'jumping-jacks', 'lunges']
r1 = [2, 12, 17, 9, 23]
minr1 = 5
maxr1 = 10

ret = handle_round(n1, r1, minr1, maxr1)
print(ret)


# 9) Glue it all together: the interactive loop
def run_session(exercises_csv, min_reps, max_reps):
    """
    - exercises_csv is the input string of exercises, separated by commas (no spaces)
    - min_reps is the lower bound for randomly choosing a number of reps
    - max_reps is the upper bound for randomly choosing a number of reps
    """
    names = load_exercise_list(exercises_csv) 
    total_reps = initialize_stats(names) 
    prompt = "Press Enter for an exercise, or type 'done' to quit: "  
    
    while True:   # TODO fixed
        user = input(prompt)    

        if user == "done":   # TODO fixed
            print("\nSession summary:")
            summarize_stats(names, total_reps) 
            break

        total_reps = handle_round(names, total_reps, min_reps, max_reps) 