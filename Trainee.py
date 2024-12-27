import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('gym0-83a26-firebase-adminsdk-sokxa-4305373246.json')

firebase_admin.initialize_app(cred,
{
    'databaseURL' : 'https://gym0-83a26-default-rtdb.firebaseio.com/'     
})
members = db.reference('members/')  
trainee_node = members.child('Trainees')


#return data of this user From the data base
def get_data(username,Pass):
    t_data = db.reference(f'members/Trainees/{username}').get()
    for i in range(5):# Test if Pasword is True
        if(Pass != t_data['Pass']):
            print("Erorr Pass Try Again ")
            Pass=input("Pass => ")
        else:
            print(f"Hello {t_data['Name'].split()[0]}".center(50))
            Name=t_data['Name']
            Work_time=f"{t_data['Work_time'] , {t_data['Hours']}}"
            Kind=t_data['Kind']
            Age=t_data['Age']
            BMI=t_data['BMI']
            Trainer=t_data['Trainer']
            Gender=t_data['Gender']
            return(f" Name => {Name} \n Work_Time => {Work_time} \n Age => {Age} \n BMI => {BMI} \n Trainer => {Trainer} \n Kind => {Kind} \n Gender => {Gender}")
    return "Error Password"


#this function if trainee want to update his data
def update(username):
    trainee_data= db.reference(f'members/Trainees/{username}')
    test='y'
    while test=='y':
        print("What Do You Want To Change")
        print("1- Name\n2- Password \n3- Age \n4- BMI & Kind \n5-Gender")
        select=input("Select(1,2,3,4) => ")
        if(select=='1'):
            Name=input("new name => ")
            trainee_data.update({'Name':Name})
            print("Name is Updated Successfully")
        elif(select=='2'):
            for i in range(100):
                Pass=input("new Pass => ") #THis label Should contain (8 charcter)
                if len(Pass)!=8:
                    print("Password Should contain 8 characters")
                else:break
            trainee_data.update({'Pass':Pass})
            print("Password is Updated Successfully")
        elif(select=='3'):
            Age=input("new Age => ")
            trainee_data.update({'Age':Age})
            print("Age is Updated Successfully")
        elif(select=='4'):
            Weight=int(input("Weight (Kg) => "))
            hight=float(input("Hight (m) => "))
            BMI = Weight/(hight*hight) # To calculate BMI
            
            #give The suggestion excercise debending on his BMI
            print(f"OK , Your BMI Is => {BMI}")
            if(BMI<18.5) : print("Underweight , Proposed training is (gain weight Exercises) ")
            elif(BMI>=18.5 and BMI<=24.9) : print(" Normal , Proposed training is (Budybuilding Exercises) ")
            elif(BMI>=25) : print(" OverWeight , Proposed training is (Cardio Exercises) ")
            
            print("Available exercises Are : ")
            #connecting with database of trainers to get aviloable Excerices
            trainee_node = members.child('Trainee')
            t_data = db.reference(f'members/Trainees/').get()
            dic_of_Kinds={}#dictionery from Trainers of Types Of Excerices
            dic_of_Trainers={}#dictionery from Trainers of Types Of Name of Trainers
            dic_of_Hours={}#dictionery from Trainers of Types Of Time of Excerices
            
            for il,i in enumerate(t_data,1):
                print(il,t_data[i]["Kind"])
                dic_of_Kinds[il]=t_data[i]["Kind"]
                dic_of_Trainers[il]=t_data[i]["Name"]
                dic_of_Hours[il]=t_data[i]['Hours']
            select=int(input("Please, Select "))
            Kind=dic_of_Kinds[select]
            Trainer=dic_of_Trainers[select]
            Hourse_Open_GYM=dic_of_Hours[select]
            trainee_data.update({'Kind':Kind})
            trainee_data.update({'Trainer':Trainer})
            trainee_data.update({'Hours':Hourse_Open_GYM})
            trainee_data.update({'Hours':Hourse_Open_GYM})
            print("Data is Updated Successfully")
        elif(select=='5'):
            Gender=input("Gender  => ")
            trainee_data.update({'Gender':Gender})
            print("Gender is Updated Successfully")
        test=input("Do You Wante Rechange any thing =>(y,n)").strip().lower()

    print("Ok , All has been Changed Successfully ")


#NewEmail For new user
def insert_data():
    print("Please inter These Data : ")
    userName=input("User Name => ")
    
    for i in range(100):#test Password is =8 chars
        Password=input("Pass => ") #THis label Should contain (8 charcter)
        if len(Password)!=8:
            print("Password Should contain 8 characters")
        else:break
    
    #inter data 
    Name=input("Name => ")
    Age=input("Age => ")
    Gender=input("Gender => ")
    Weight=int(input("Weight (Kg) => "))
    hight=float(input("Hight (m) => "))
    BMI = Weight/(hight*hight) # To calculate BMI
    
    #give The suggestion excercise debending on his BMI
    print(f"OK , Your BMI Is => {BMI}")
    if(BMI<18.5) : print("Underweight , Proposed training is (gain weight Exercises) ")
    elif(BMI>=18.5 and BMI<=24.9) : print(" Normal , Proposed training is (Budybuilding Exercises) ")
    elif(BMI>24.9) : print(" OverWeight , Proposed training is (Cardio Exercises) ")
    
    print("Available exercises Are : ")
    #connecting with database of trainers to get aviloable Excerices
    trainee_node = members.child('Trainee')
    t_data = db.reference(f'members/Trainees/').get()
    dic_of_Kinds={}#dictionery from Trainers of Types Of Excerices
    dic_of_Trainers={}#dictionery from Trainers of Types Of Name of Trainers
    dic_of_Hours={}#dictionery from Trainers of Types Of Time of Excerices
    
    for il,i in enumerate(t_data,1):
        print(il,t_data[i]["Kind"])
        dic_of_Kinds[il]=t_data[i]["Kind"]
        dic_of_Trainers[il]=t_data[i]["Name"]
        dic_of_Hours[il]=t_data[i]['Hours']
    select=int(input("Please, Select "))
    Kind=dic_of_Kinds[select]
    Trainer=dic_of_Trainers[select]
    Hourse_Open_GYM=dic_of_Hours[select]
    print("Select The type of subscription : ")
    Kind_avilable=["1)  3 Days Per weak (20$ / mounth)" ,"2)  3 Days Per weak (55$ / 3 mounths)","3)  3 Days Per weak (100$ / 6 mounths))"
                    , "4)  6 Days Per weak (40$ / mounth)" , "5)  6 Days Per weak (95$ / 3 mounths)" ,"6)  6 Days Per weak (160$ / 6 mounths)"]
    for i in Kind_avilable:
        print(i)
    choose=int(input("Choose(1,2,3,4,5,6)  => "))
    Kind_time=Kind_avilable[choose][2:]
    
    trainee_node.update(#adding this member in the data base
        {
            userName : {
            'Name' : Name,
            'Pass' : Password,
            'Age':Age,
            'Hours':Hourse_Open_GYM,
            'Kind':Kind,
            'Gender':Gender,
            'Trainer':Trainer,
            'BMI':BMI,
            'Work_time':Kind_time
            }
        }
    )
    print("Welcome To Our Gym You have been Added Successfully")

#function of Calling
def Trainees_Class():
    print("GYM SYSTEM".center(50))
    print('*'*20)
    try:# if user name is in my data base
        user_Name=input("User_name => ")
        Pass=input("Pass => ")
        print('*'*20)
        get=get_data(user_Name,Pass)
        if(get!="Error Password"):
            print(get)
            print('*'*20)
            show_test=input("Do You Want To Update Your Data(Y,N)").strip().lower()
            if(show_test=='y'):
                print("="*20)
                update(user_Name)
            print(" Thanks To visit Our WepSight")
        else: print("Fuck You , Don't Try Again")
    
    except:# if user name not into the data base
        print("You Don't Have an account")
        print("Make New Account ")
        insert_data()

Trainees_Class()
