print("Xoxo")
print("오류를 어떻게 고친건지 모르겠어요..! 하지만 일단 됐다..!")

# Info
# brief = txt 파일을 이용해서 구현한 로그인, 회원가입 프로그램
# remark = home 화면에서 로그인, 회원가입이 가능하고 로그인 이후 로그아웃, 회원탈퇴가 가능하도록 설계
# author = MINGYOUNG BAN 
# date = 2023.02.09
# todo = 이후 페이지 내의 기능을 추가하거나 json등을 활용한 개발을 시도하고 싶음
# code = 시작점은 home 함수


# 회원가입 함수 
# ID, PW, PW 재입력을 받는다. 
def signup():
    db = open("members.txt", "r")
    ID = input("Please Enter Your New Id : ")
    PW = input("Please Enter Your New PW : ")
    PwConfirm = input("Confirm PW : ")
    c =[]
    d =[]
    for i in db:
        a,b = i.split(" : ")
        b = b.strip()
        c.append(a)
        d.append(b)
    data = dict(zip(c, d))
   
    #회원가입 확인 기능
    
    if PW != PwConfirm:
        print("You entered diffrent password")
        signup()
        #pw과 pw 확인에서 다른 pw를 입력하면 다시 처음으로 돌아가게 한다. 
    else:
        if len(PW)<4:
            print("Your password is too short")
            signup()     #pw가 8글자보다 짧으면 다시 입력하게 처음으로 돌아간다.
        elif ID in c:
            print("Same ID aready exist")
            signup()    #기존에 있는 ID의 경우에는 다시 입력하게 처음으로 돌아간다. 
        else:
            db = open("members.txt", "a")
            db.write(ID+ " : "+PW+"\n")
            print("Welcome")    #앞의 경우가 아니면 회원가입 성공
    

#로그인 함수 - id와 pw를 확인한다. 
def login():
    db = open("members.txt", "r")
    ID = input("Please Enter Your Id : ")
    PW = input("Please Enter Your PW : ")
    
    if not len(ID or PW) <1 :
        d =[]
        f =[]
        for i in db:
            a,b = i.split(" : ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        try :
            if data[ID] :
                try :
                    if PW == data[ID]: 
                        print("-------------")
                        print("Welcome back")
                        print("-------------")
                        
                        activity() #로그인 이후 다른 활동이 가능한 페이지로 이동
                        
                    else :
                        print("Incorrect Access : Check your ID and PW") #ID or PW incorrect
                        
                except:
                    print("Incorrect Access : Check your ID or PW once again") #ID or PW incorrect
            else:
                print("There is no data. Please check your ID and PW") #데이터가 없을 때
        except:
            print("Login Error") 
    else:
        print("Please Enter at least one character for your ID and PW.") #입력 값을 입력하지 않을 때
        
        
#activity 함수 : stay, sign out(탈퇴), log out 중 하나를 숫자를 입력하여 선택할 수 있다. 
def activity(option=None):
    print("Choose a number : 1. Remain doing nothing \n 2. Sign out \n 3. Logout")
    option = input("1 | 2 | 3:")
    if option =="1": 
        print("A happy cat smiles for you! Thank you for staying here!") #아무것도 하지 않을 경우를 위한 선택지
    elif option =="2":
        print("We are sorry to hear that...")
        signout() #탈퇴 함수로 이동
    elif option =="3":
        print("Bye Bye")
        home() #초기 회면으로 돌아감 
    else:
        print("Wrong option! Error!")
        
#signout 회원 탈퇴 함수        
def signout():
 
    ID = input("Please Enter Your Id to sign out : ")
    PW = input("Please Enter Your PW to sign out : ")
    
    #탈퇴를 위한 id pw확인
     
    with open("members.txt", "r") as db:
        search = db.readlines()

    targetLine = []
    result = False 
    
    for line in search:
        memID, memPW =line.strip().split(" : ")
        
        if ID == memID and PW == memPW:
            result = True
        else:
            targetLine.append(line)
    
    if result:
        with open("members.txt", "w") as db:
            db.writelines(targetLine)
            
            print("You successfully signed out") #탈퇴 성공
            
    else:
        print("ID or PW is incorrect. Please check your input once again.")
    #db에 없는 id 나 pw를 입력한 경우
    

#home 화면 함수. 초기 화면으로 로그인, 회원 가입을 숫자를 선택해서 이동 가능          
def home(option=None):
    print("Input Number : 1. Login 2. Register \n")
    option = input("1 | 2:")
    if option =="1":
        login() #로그인 
    elif option =="2":
        signup() #회원가입
        print("Wrong option! Error!")
            
home()
                    
