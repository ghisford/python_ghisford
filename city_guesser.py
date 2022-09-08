from random import seed, randint
import requests

def get_data(num):
    url= "https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-capital-city.json"
    res = requests.get(url)
    data = res.json()
    seed(num)
    index_val = randint(0,30)
    country = data[index_val]['country']
    city = data[index_val]['city']
    return country,str(city).lower()

def create_question():
    points = 0

    print('press q to exit')
    for i in range(10):
        country,city = get_data(i)
        answer = (input(f'what is the capital of {country} ?')).lower()
        if answer == city:
            points += 1
            print("correct !")
        elif answer == 'q':
            break    
        else:
            print('wrong answer')
            print(f'the capital of {country} is {city} ')

    print(f'your total score is {points}')

create_question()