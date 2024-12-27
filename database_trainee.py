import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('C:\\Users\\A.T\\Desktop\\pr\\part\\gym0-83a26-firebase-adminsdk-sokxa-4305373246.json')

firebase_admin.initialize_app(cred,
{
    'databaseURL' : 'https://gym0-83a26-default-rtdb.firebaseio.com/'     
})

# --- insert trainers data ---
members = db.reference('members/')
trainers_node = members.child('trainees')
trainers_node.set(
    {
    'Saifeddin': {
        'Name' : 'Saifeddin Ahmad Muhamad',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '20',
        'Mobile phone' : '01014092012'
                },
    'Muhamad':
                {
        'Name' : 'Muhamad Ahmad  Abdul-Raheem',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '19',
        'Mobile phone' : '01014092012' 
                },
    'Ahmad':
                {
        'Name' : 'Ahmad  Uhn',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '22',
        'Mobile phone' : '01014092012' 
                },
    'Ali':
                {
        'Name' : 'Ali Muhamad Abdallah Nagi',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '23',
        'Mobile phone' : '01010792012' 
                },
    'Abdullah':
                {
        'Name' : 'Abdulla  Habib',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '24',
        'Mobile phone' : '01014092012' 
                },
    'Mahmoud Mostafa':
                {
        'Name' : 'Mahmoud Mostafa',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '23',
        'Mobile phone' : '01014092012' 
                },
    'Mahmoud Talat Omar':
                {
        'Name' : 'Mahmoud Talat Omar',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '22',
        'Mobile phone' : '01014092012' 
                },
    'Ahmad Omar Nouh':
                {
        'Name' : 'Ahmad Omar Nouh',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '21',
        'Mobile phone' : '01014092012' 
                },
    'Amr Mostafa Zakarya':
                {
        'Name' : 'Amr Mostafa Zakarya',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '21',
        'Mobile phone' : '01014792012' 
                },
    'Mostafa Abdul-Rahma sherif':
                {
        'Name' : 'Mostafa Abdul-Rahma sherif',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '24',
        'Mobile phone' : '01014792012' 
                },
    'Moaz Ibrahim Mostafa':
                {
        'Name' : 'Moaz Ibrahim Mostafa',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '23',
        'Mobile phone' : '01014702012' 
                },
    'Muhamad Abdullah Mostafa':
                {
        'Name' : 'Muhamad Abdullah Mostafa',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '24',
        'Mobile phone' : '01014702012' 
                },
    'Abdou Ahmed':
                {
        'Name' : 'Abdu Ahmed',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '24',
        'Mobile phone' : '01014702012' 
                },
    'Mustafa Fathi Ahmed':
                {
        'Name' : 'Mustafa Fathi Ahmed',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'BMI' : '24',
        'Mobile phone' : '01014092012' 
                }
    }
)

# --- update ---
# name = 'سيف الدين أحمد'
# update_trainers = trainers_node.child(f'{name}').update({
#     'Name' : 'محمد'
# })

data = db.reference('members/trainees').get()
for trainee in data.keys():
    trainee_data = db.reference(f'members/trainees/{trainee}').get()
    name = trainee_data['Name']
    gender = trainee_data['Gender']
    print(name)
    print(gender)