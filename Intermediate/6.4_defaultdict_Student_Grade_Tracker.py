# 4️⃣ defaultdict
# ️ Exercise: Student Grade Tracker
# You are given:
# grades = [
# ("Alice", "Math", 85),
# ("Bob", "Math", 78),
# ("Alice", "Science", 92),
# ("Bob", "Science", 88),
# ("Charlie", "Math", 90)
# ]
# ️ Requirements:
# 1. Group grades by student.
# 2. Calculate average grade per student.
# 3. Group students by subject.
# 4. Find top scorer in each subject.
# 5. Convert grouped result into a normal dictionary before printing.
# ️ Real-world relevance:
# Used in reporting systems, grouping database records, analytics.


from collections import defaultdict

grades = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 78),
    ("Alice", "Science", 92),
    ("Bob", "Science", 88),
    ("Charlie", "Math", 90),
    ("Don", "Math", 90)
]

by_grade = defaultdict(list)

for item in grades:
    by_grade[item[0]].append(item[2])

by_grade = dict(by_grade)
print(by_grade)

avr_per_student = {}

for key, value in by_grade.items():
    avr_per_student[key] = (sum(value)/len(value))

avr_per_student = dict(avr_per_student)
print(avr_per_student)

by_subject = defaultdict(list)

for item in grades:
    by_subject[item[1]].append(item[0])

by_subject = dict(by_subject)
print(by_subject)

top_score = defaultdict(list)

for item in grades:
    if item[1] in top_score:
        continue
    else:
        top_score[item[1]] = max(list(i[2] for i in grades if i[1] == item[1]))

top_score = dict(top_score)
print(top_score)

top_scorer = defaultdict(list)

for item in grades:
    if item[2] == top_score[item[1]]:
        top_scorer[item[1]].append(item[0])

top_scorer = dict(top_scorer)
print(top_scorer)
