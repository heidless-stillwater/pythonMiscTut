

# ex_1
numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
  squared.append(num ** 2)

# print(squared)

# ex_2
def square(number):
  return number ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

#print(f"squared: {squared}")
#list(squared)

# ex_3
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = list(map(int, str_nums))
# print(f"int_nums: {int_nums}")

# list(int_nums)
# print(f"str_nums: {str_nums}")

# ex_4
numbers = [-2, -1, 0, 1, 2]

abs_values = list(map(abs, numbers))
#print(f"abs_values: {abs_values}")

float_numbers = list(map(float, numbers))
#print(f"float_numbers: {float_numbers}")

words = ["Welcome", "to", "Real", "Python"]
word_count = list(map(len, words))
#print(f"word_count: {word_count}")

# ex_5
numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers)
# print(list(squared))

sentences = ["havana tropical banana tropical",
            "behavious tropical fruity"]

tropical_count = list(map(lambda s: s.count("tropical"), sentences))
fruity_count = list(map(lambda s: s.count("fruity"), sentences))

print(f"tropical_count: {tropical_count}")
print(f"fruity_count: {fruity_count}")

