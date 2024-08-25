print("кто ты из головоломки")
question1 = "Если в магазине не будет твоего любимого мармелада, какая у тебя будет реакция?" 
question2 = "Если без тебя пойдут гулять твои друзья, какая у тебя будет реакция?" 
question3 = "Если у тебя не будет получаться домашние задание, какая у тебя будет реакция?"
question4 = "Если будет дождь, какая реакция у тебя будет?"
question5 = "Если ты увидишь бездомного котенка, какая у тебя будет реакция?"
print(question1)
print("1.грусть 2.злость 3.радость")
answer1 = input("введите ответ цифрой: ")
print(question2)
print("1.грусть 2.злость 3.радость")
answer2 = input("введите ответ цифрой: ")
print(question3)
print("1.грусть 2.злость 3.радость")
answer3 = input("введите ответ цифрой: ")
print(question4)
print("1.грусть 2.злость 3.радость")
answer4 = input("введите ответ цифрой: ")
print(question5)
print("1.грусть 2.злость 3.радость")
answer5 = input("введите ответ цифрой: ")
happy_point = 0
engry_point = 0
sad_point = 0
if answer1 == "1":
    sad_point = sad_point + 1
else:
    if answer1 == "2":
         engry_point = engry_point + 1
    else:
        if answer1 == "3":
         happy_point = happy_point + 1
if answer2 == "1":
    sad_point = sad_point + 1
else:
    if answer2 == "2":
         engry_point = engry_point + 1
    else:
        if answer2 == "3":
         happy_point = happy_point + 1
if answer3 == "1":
    sad_point = sad_point + 1
else:
    if answer3 == "2":
         engry_point = engry_point + 1
    else:
        if answer3 == "3":
         happy_point = happy_point + 1
if answer4 == "1":
    sad_point = sad_point + 1
else:
    if answer4 == "2":
         engry_point = engry_point + 1
    else:
        if answer4 == "3":
         happy_point = happy_point + 1
if answer5 == "1":
    sad_point = sad_point + 1
else:
    if answer5 == "2":
         engry_point = engry_point + 1
    else:
        if answer5 == "3":
         happy_point = happy_point + 1
print(sad_point, happy_point, engry_point)
if happy_point >= sad_point:
    if happy_point >= engry_point:
        print("радость")
if sad_point > happy_point:
    if sad_point > engry_point:
        print("грусть")
if engry_point > happy_point:
    if engry_point > sad_point:
        print("злость")





 
    







