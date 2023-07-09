import pandas as pd
import time

df = pd.read_excel('database.xlsx')
username_list = list(df['username'])
username = input('Enter your Username: ')

if username not in username_list:
    print(username, 'username does not exist!')
    exit()
else:
    password = input('Enter your Password: ')

user_info = df[['username', 'password']][df['username'] == username]

fare = {
    'New York': 'London',
    'New York': 'California',
    'London': 'New York',
    'London': 'California',
    'California': 'New York',
    'California': 'London'
}

if user_info['password'].values[0] == password:
    print('Successfully logged in...\n')
    source = input('Enter your Source: ')
    destination = input('Enter your Destination: ')
    if source.lower().replace(" ", "") == 'newyork' and destination.lower().replace(" ", "") == 'london':
        if username == 'indian_user':
            price = 50000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 40000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 60000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 45000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 55000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    elif source.lower().replace(" ", "") == 'newyork' and destination.lower().replace(" ", "") == 'california':
        if username == 'indian_user':
            price = 30000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 20000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 25000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 45000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 35000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    elif source.lower().replace(" ", "") == 'london' and destination.lower().replace(" ", "") == 'newyork':
        if username == 'indian_user':
            price = 50000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 40000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 60000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 45000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 55000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    elif source.lower().replace(" ", "") == 'london' and destination.lower().replace(" ", "") == 'california':
        if username == 'indian_user':
            price = 90000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 70000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 85000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 95000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 65000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    elif source.lower().replace(" ", "") == 'california' and destination.lower().replace(" ", "") == 'newyork':
        if username == 'indian_user':
            price = 30000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 20000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 25000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 45000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 35000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    elif source.lower().replace(" ", "") == 'california' and destination.lower().replace(" ", "") == 'london':
        if username == 'indian_user':
            price = 90000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'american_user':
            price = 70000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'british_user':
            price = 85000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'australian_user':
            price = 95000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        elif username == 'russian_user':
            price = 55000
            print('The fare for',username,'from', source, 'to', destination, 'is:', price)
        else:
            print('Error 404!')
    else:
        price = 'NaN'
        print('The fare for', source, 'to', destination, 'is:', price)
        print('No Flights Found!')
    print('\n')
    #time.sleep(1)
else:
    print('Invalid Credentials...')






