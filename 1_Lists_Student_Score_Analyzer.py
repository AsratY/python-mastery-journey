# 1️⃣ Lists — Student Score Analyzer

# 🎯 Build: A program that manages and analyzes student scores.

# 🛠 Use: lists, indexing, slicing, append, sort, min, max, sum

# 📋 Instructions

# Create a list of student scores (hardcoded first).

# Print:

# Highest score

# Lowest score

# Average score

# Sort scores ascending and descending.

# Allow the user to add a new score.

# Recalculate stats after insertion.

# ⭐ Upgrade

# Remove invalid scores (<0 or >100)

# Show top 3 scores using slicing

def print_stats(student_score):
    print(f"The Highest score is: {max(student_score)}")
    print(f"The Lowest score is: {min(student_score)}")
    print(f"The Average score is: {sum(student_score)/len(student_score)}")


def add_score():
    try:
        score = float(input("Enter Score: "))
        return score
    except:
        print("Enter Numbers Only!")
        add_score()


def remove_invalid(student_score):
    for item in student_score:
        if item > 100 or item < 0:
            student_score.remove(item)


student_score = [23, 45, 67, 87, 56, 40, 93, 87,
                 65, 42, 36, 54, 47, 61, 37, 28, 63, 95, 68, 76]
print_stats(student_score)
print()

ascend_score = sorted(student_score)
print(f"Scores in Ascending: \n{ascend_score}")
descend_score = ascend_score[::-1]
print(f"Scores in Descending: \n{descend_score}\n")

score = add_score()
student_score.append(score)

remove_invalid(student_score)
print_stats(student_score)

student_score = sorted(student_score)
print(f"The Top 3 scores are: {student_score[-3:]}")
