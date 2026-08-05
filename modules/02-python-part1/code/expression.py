# # # def double(x):
# # #     return x*2

# # # double(5)
# # # double(17)
# # # double(-3)
# # # double(0)

# # # n1 = double(5)
# # # n2 = double(17)
# # # n3 = double(-3)
# # # n4 = double(0)
# # # n5 = double(n1)

# # # print(n1, n2, n3, n4, n5)

# # def Calculate_total(cost, tax):
# #     tax = cost * tax / 100
# #     new_cost = cost + tax
# #     return new_cost

# # n = Calculate_total(100, 15)
# # print(n)

# # def mystery(n, x):
# #     mult = n * x
# #     return mult / 100
    
# # x = mystery(5, 100)
# # mystery(10, 10)

# # text = float(input("Enter some text: "))
# # print(5*text)

# # a = input("Favorite animal: ")
# # b = input("Favorite number: ")
# # c = input("Favorite city: ")

# # print(a+b+c)

# # def check_weather(condition):
# #     if condition == "rain":
# #         print("Take an umbrella.")
# #     elif condition == "snow":
# #         print("Wear boots.")
# #     else:
# #         print("Enjoy your day.")

# # check_weather("snow")

# # def evaluate_grade(score):
# #     if score >= 90:
# #         print("A")
# #     if score >= 80:
# #         print("B")
# #     else:
# #         print("C")

# # print(evaluate_grade(75))

# # def check_balance(balance):
# #     if balance >= 100:
# #         print("You can withdraw.")
# #     elif balance >= 10:
# #         print("Small withdrawal allowed.")
# #     else:
# #         print("Try again later.")
  


# # def print_activity(day):
# #     if day == "Saturday":
# #         print("Go hiking!")
# #     elif day == "Sunday":
# #         print("Rest and relax.")
# #     print("Weekend fun!")

# # print_activity("Sunday")

# # text = "banana"
# # no_vowels = ""
# # for char in text:
# #     if char not in "aeiou":
# #         no_vowels = no_vowels + char
# #     else:
# #         no_vowels = no_vowels + '_'
# # print(no_vowels)

# # def collect_animals_with_a(animals):
# #     result = []
# #     for name in animals:
# #         if 'a' in name.lower():
# #             result.append(name)
# #     return result

# # pets = ['Tiger', 'Koala', 'penguin', 'EAGLE']
# # selected = collect_animals_with_a(pets)

# # print(selected)
# # print(pets)

# # def get_base():
# #     return float(input("Base: "))

# # def get_height():
# #     return float(input("Height: "))

# # def compute_area(base, height):
# #     return 0.5 * base * height

# # def main():
# #     b = get_base()
# #     h = get_height()
# #     area = compute_area(b, h)
# #     print(f"Area: {area}")
    
# # main()

# def get_text():
#     print("Enter your text (type END to finish):")
#     lines = []
#     while True:
#         line = input()
#         if line == "END":
#             break
#         lines.append(line)
#     return lines

# def get_keywords():
#     print("Enter keywords separated by commas:")
#     keywords = input()
#     keyword_list = []
#     for word in keywords.split(","):
#         cleaned = word.strip().lower()
#         keyword_list.append(cleaned)
#     return keyword_list

# def count_keywords(text, keywords):
#     words = " ".join(text).lower().split(' ')  # turns a list back into a string
#     result = []
#     for keyword in keywords:
#         count = words.count(keyword)
#         result.append([keyword, count])
#     return result

# def display_results(counts):
#     for pair in counts:
#         keyword = pair[0]
#         count = pair[1]
#         print(f"{keyword}: {count} occurrence(s)")

# def main():
#     text = get_text()
#     keywords = get_keywords()
#     counts = count_keywords(text, keywords)
#     display_results(counts)

# main()