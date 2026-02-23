print("Welcome To Love Calculator!")

user_name = input("Your Name: ")
lover_name = input("Lover Name: ")

user_name = list(user_name.upper().strip())
lover_name = list(lover_name.upper().strip())

true = ["T", "R", "U", "E"]
love = ["L", "O", "V", "E"]

count_true = 0
count_love = 0

for letter in true:
    count_true += user_name.count(letter)
    count_true += lover_name.count(letter)

for letter in love:
    count_love += user_name.count(letter)
    count_love += lover_name.count(letter)

score = int(str(count_true)+str(count_love))

if score > 85 or score < 10:
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif score > 40 and score < 70:
    print(f"Your score is {score}%, you are alright together.")
else:
    print(f"Your score is {score}%.")
