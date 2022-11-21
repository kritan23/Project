import sys 		
import time             
str=input("Enter a String:")
while True:
    time.sleep(.50)
    print("------------------------Welcome to String operation Menu------------------------")
    print("Press 'Enter' To Continue")
    k=input()
    print("1. Print String")
    print("2. Length of String")
    print("3. No. of Alphabets")
    print("4. No. of Digits")
    print("5. Total No. of Vowels present in the String")
    print("6. Total No. of Consonant present in the String")
    print("7. Change the String into Uppercase")
    print("8. Change the String into Lowercase")
    print("9. To capitalize the String")
    print("10. To Join A New String To The old String")
    print("11. To Split The Given String")
    print("12. To Do The Partition Of The Given String")
    print("0. Exit")
    ch=int(input("Enter your choice 0-12="))
    
    if ch==1:
        print("The String :",str)

    elif ch==2:
        print("String length=",len(str))

    elif ch==3:
        count=0
        for i in str:
            if i.isalpha():
                count+=1
        print("Number of alphabets=",count)

    elif ch==4:
        cnt=0
        for i in str:
            if i.isdigit():
                cnt+=1
        print("Number of digits=",cnt)

    elif ch==5:
        vow=0
        for i in str:
            if i in "aeiouAEIOU":
                vow+=1
        print("Total number of vowels=",vow)

    elif ch==6:
        cons=0
        for i in str:
            if i not in "aeiouAEIOU":
                cons+=1
        print("Total number of consonants=",cons)

    elif ch==7:
        for i in str:
            o=str.upper()
        print("The changed upper String is",o)

    elif ch==8:
        for i in str:
            z=str.lower()
        print("The changed lower String is",z)

    elif ch==9:
        print(str.capitalize())

    elif ch==10:
        c="-"
        print(c.join(str))

    elif ch==11:
        print(str.split())

    elif ch==12:
        print(str.partition("a"))
        
    elif ch==0:
        break

    else:
        print("Your Choice Is Not Present In The List. Choose Another No.")
sys.exit
