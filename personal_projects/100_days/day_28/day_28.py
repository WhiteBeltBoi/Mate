import random
random.seed(10)
names =["Cara", "Sydney", "Agika", "Bobby", "Anny", "Mia"]
student_scores = {student:random.randint(0, 100) for student in names}
print(student_scores)
passed_students = {}
# for name, score in student_scores.items():
#     if score >= 60:
#         passed_students[name] = score

passed_students_comp= {student:score for student, score in student_scores.items() if score >= 60}
print(passed_students_comp)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_sentence = [word for word in sentence.split("")]
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {Day:temp * 9 /5 + 32 for Day, temp  in weather_c.items()}

print(weather_f)