                                            #TODO:HEALTH MANAGEMENT
import time
def lock():
    ask1=int(input("type 1 for diet and 2 for exercise\nwhat do you want to lock(Diet or exercise):"))
    # print("type 'd or D' for diet and 'e or E' for exercise")
    L = ['Rahul', 'shyam', 'anshu']
    if ask1==1:
        print("For whome do you wana lock Diet?")
        ask2 = int(input("enter your choice:(in b/w 1 for rahul,2 for shyam,3 for anshu)"))
        if ask2==1:
            ask3=input("write your diet:")
            print(f"diet of {L[0]} is: {ask3} at {time.asctime(time.localtime(time.time()))}")
            with open("health_R_D.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The diet of {L[0]} is: {ask3}")
        elif ask2 ==2:
            ask3 = input("write your diet:")
            print(f"diet of {L[1]} is: {ask3} at {time.asctime(time.localtime(time.time()))}")
            with open("health_Sh_D.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The diet of {L[1]} is: {ask3}")
        elif ask2 ==3:
            ask3 = input("write your diet:")
            print(f"diet of {L[2]} is: {ask3} at {time.asctime(time.localtime(time.time()))}")
            with open("health_A_D.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The diet of {L[2]} is: {ask3}")
        else:
            print("you entered a wrong input!please follow the above rule$THANK YOU$")

    elif ask1==2:
        print("For whome do you wana lock Exercise?")
        ask4 = int(input("enter your choice:(in b/w 1 for Rahul,2 for shyam,3 for anshu)"))
        if ask4==1:
            ask5=input("write your exercise:")
            print(f"exercise of {L[0]} is : {ask5} at {time.asctime(time.localtime(time.time()))}")
            with open("health_R_E.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The exercise of {L[0]} is:{ask5}")
        elif ask4==2:
            ask5 = input("write your exercise:")
            print(f"exercise of {L[1]} is : {ask5} at {time.asctime(time.localtime(time.time()))}")
            with open("health_Sh_E.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The exercise of {L[1]} is:{ask5}")
        elif ask4==3:
            ask5 = input("write your exercise:")
            print(f"exercise of {L[2]} is : {ask5} at {time.asctime(time.localtime(time.time()))}")
            with open("health_A_E.txt", 'a') as f:
                f.write(f"{time.asctime(time.localtime(time.time()))}:-The exercise of {L[2]} is:{ask5}")
        else:
            print("you entered a wrong input!please follow the above rule$THANK YOU$")

    else:
        print("you entered wrong input\nplease enter input according to given instruction")



def retrieve():
    ask6 = int(input("type 1 for diet and 2 for exercise\nwhat do you want to retrieve(Diet or exercise):"))
    # print("type 'd or D' for diet and 'e or E' for exercise")
    L = ['Rahul', 'shyam', 'anshu']
    if ask6 == 1:
        print("For whome do you wana retrieve Diet?")
        ask7 = int(input("enter your choice:(1 for rahul,2 for shyam,3 for anshu)"))
        if ask7 == 1:
            with open("health_R_D.txt", 'r') as f:
                a=f.readlines()
                print(a)
        elif ask7==2:
            with open("health_Sh_D.txt", 'r') as f:
                a=f.readlines()
                print(a)
        elif ask7==3:
            with open("health_A_D.txt", 'r') as f:
                a=f.readlines()
                print(a)
        else:
            print("you entered wrong input!please follow the above rule$$THANK YOU$$")

    elif ask6== 2:
        print("for whome do you wana retrive exercise?")
        ask8 = int(input("enter your choice:(1 for rahul,2 for shyam,3 for anshu)"))
        if ask8 == 1:
            with open("health_R_E.txt", 'r') as f:
                a=f.readlines()
                print(a)
        elif ask8 ==2:
            with open("health_Sh_E.txt", 'r') as f:
                a=f.readlines()
                print(a)
        elif ask8==3:
            with open("health_A_E.txt", 'r') as f:
                a=f.readlines()
                print(a)
        else:
            print("you entered wrong input!please follow the above rule$$THANK YOU$$")

    else:
        print("you entered wrong input\nenter according to the given instruction")


if __name__ == "__main__":
    print("There are three client named(Rahul,Shyam,Anshu)")
    ask=int(input("do you want to lock or retrieve(type 1 for lock and 2 for retrieve):"))
    if ask==1:
        lock()
    elif ask==2:
        retrieve()
    else:
        print("you entered wrong choice\n")