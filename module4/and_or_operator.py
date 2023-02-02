# exercise : WATCH COCO
# ask user's name amd age . if user's name start with ('a' or'A') and age is above 10 than print you can watch coco movie , else print sorry you cannot watch coco

name,age=input("enter your name and age separated by comma").split(",")
if (name.strip()[0]=='a'or name.strip()[0]=='A') and int(age.strip())>10 :
    print("you can watch COCO movie ")
else:
    print("you cannot watch coco movie")