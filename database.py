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
trainers_node = members.child('trainerS')
trainers_node.set(
    {
    'Saifeddin': {
        'Name' : 'Saifeddin Ahmad Muhamad Abdul-Raheem',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012'
                },
    'Muhamad':
                {
        'Name' : 'Muhamad Ahmad Muhamad Abdul-Raheem',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Ahmad':
                {
        'Name' : 'Ahmad Ashraf Uhn',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Ali':
                {
        'Name' : 'Ali Muhamad Muhamad Nagi',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Abdullah':
                {
        'Name' : 'Abdulla Hama As-Said Habib',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Mahmoud':
                {
        'Name' : 'Mahmoud Husein',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Mahmoud':
                {
        'Name' : 'Mahmoud Talat',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Ahmad Madeh Nouh':
                {
        'Name' : 'Ahmad Madeh Nouh',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Amr Refat Zakarya':
                {
        'Name' : 'Amr Refat Zakarya',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Abdul-Rahma sherif Fawzy Beshri':
                {
        'Name' : 'Abdul-Rahma sherif Fawzy Beshri',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Moaz Ibrahim':
                {
        'Name' : 'Moaz Ibrahim',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Muhamad Abdullah':
                {
        'Name' : 'Muhamad Abdullah',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Abdou':
                {
        'Name' : 'Abdu',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                },
    'Mustafa Fathi':
                {
        'Name' : 'Abdul-Rahma sherif Fawzy Beshri',
        'Gender' : 'male',
        'Exercises type' : 'fitness',
        'NOWD' : '5',
        'WT' : '4 - 12',
        'Mobile phone' : '01014792012' 
                }
    }
)

# --- update ---
# name = 'سيف الدين أحمد'
# update_trainers = trainers_node.child(f'{name}').update({
#     'Name' : 'محمد'
# })

data = db.reference('members/trainerS').get()
for trainer in data.keys():
    trainer_data = db.reference(f'members/trainerS/{trainer}').get()
    name = trainer_data['Name']
    gender = trainer_data['Gender']
    print(name)
    print(gender)