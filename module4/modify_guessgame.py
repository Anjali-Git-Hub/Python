import random
winning_num=random.randint(0,100)
count=0
num=int(input("guess a number between 1 to 100 : "))
while True:
    count+=1
    if num>winning_num:
        print("too high")
        num=int(input("guess agin : "))
        continue
    elif num<winning_num:
        print("too low")
        num=int(input("guess agin : "))
        continue
    else:
        print(f"you win and you guessed this number in {count} times ")
        break
      