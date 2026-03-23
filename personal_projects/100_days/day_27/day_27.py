text_1 = []
text_2 = []

with open("file1.txt", "r") as f:
    for line in f:
        try:
            text_1.append(int(line.strip()))
        except:
            ValueError
with open("file2.txt", "r") as f:
    for line in f:
        try:
            text_2.append(int(line.strip()))
        except:
            ValueError

print(text_1)
print(text_2)
result = []
result.extend(x for x in text_2 if x in text_1 and x not in result)
print(result)