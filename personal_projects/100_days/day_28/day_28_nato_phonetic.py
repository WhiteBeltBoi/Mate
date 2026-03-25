import csv
# I did without csv reader too, to just practice rawdogging it with simple Python
# with open("nato_phonetic_alphabet.csv", newline="") as f:
#     my_dict = {}
#     f.readline()
#     for line in f:
#         words = line.strip().split(",")
#         my_dict[words[0]] = words[1]

with open("nato_phonetic_alphabet.csv") as file:
    reader = csv.reader(file)
    my_dict = {letter:code for (letter,code) in reader}

print(my_dict)

user_input= input("Enter your name: ").upper()
# nato_phonetic = []
# for letter in user_input:
#     nato_phonetic.append(my_dict[letter])

# print(nato_phonetic)

nato_phonetic_list_comprehension = [my_dict[letter] for letter in user_input]

print(nato_phonetic_list_comprehension)

with open("name_as_phonetic_alphabet.csv", "w") as file:
    file.write("\n".join(nato_phonetic_list_comprehension))
