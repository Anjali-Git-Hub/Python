age=int(input("enter your age "))
if age==0 or age<0:
    print("you cannot watch movie")
elif 0<age<=3 :
    print("ticket price : free")
elif 3<age<=10 :
    print("ticket price : 150")
elif 0<age<=60 :
    print("ticket price: 250")
else :
    print("ticket price : 200")
