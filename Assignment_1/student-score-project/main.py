from api import fetch_students
import matplotlib.pyplot as plt

students = fetch_students()

names = []
scores = []

for student in students[:10]:
    total = (
        student["math_score"] +
        student["history_score"] +
        student["physics_score"] +
        student["chemistry_score"] +
        student["biology_score"] +
        student["english_score"] +
        student["geography_score"]
    )

    average = total / 7

    name = student["first_name"]
    names.append(name)
    scores.append(average)

print("Average Scores:")

for i in range(len(names)):
    print(names[i], "-", round(scores[i], 2))

plt.bar(names, scores)
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Test Scores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()