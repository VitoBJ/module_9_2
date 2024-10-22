
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = list(map(len, filter(lambda s: len(s) >= 5, first_strings)))


from itertools import product

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(f, s) for f, s in product(first_strings, second_strings) if len(f) == len(s)]


combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)