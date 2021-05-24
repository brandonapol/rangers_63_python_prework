print("Hello world!")

print("\n ----------CHAPTER ONE--------- ")
# running Python 3.8.2 64-bit
# running Jupyter Notebook as well
# ran all of Chapter 1 in terminal on my mac

# 1-1
#Visited python.org 

# 1-2
#code won't run without an error so I'll just comment error-laden code
#prin('hello, world!")

# 1-3
#Not sure how "infinite skills" work in any context, and I'm
#not a great ideas guy - I'm an implements guy. Worked that way
#when I was in the music world as well - I don't come up with 
#brilliant new ideas, but I will take someone's good idea and
#make it perfect.

#Chapter Two
print("\n ----------CHAPTER TWO--------- ")
# 2-1
message = "I love my wife"
print(message)
print('\n')

# 2-2
message = "Coding computers is better than coding in an ambulance"
message = "Interior Alaska is beautiful but too cold in January"
print(message)
print('\n')

# 2-3
name = "Brandon"
print("Hello, " + str(name) + ", why are you typing in third person?")
print('\n')

# 2-4
name_case = "Brandon"
print(name_case.lower())
print(name_case.upper())
print(name_case.title())
print('\n')

# 2-5
print('''"If I can help a kid discover a liking, or 
even a passion for music in their life, then that's 
a wonderful thing." - Eddie Van Halen
''')
print('\n')

#2-6
famous_person = '''"If I can help a kid discover a liking, or 
even a passion for music in their life, then that's 
a wonderful thing." - Eddie Van Halen'''
print(famous_person)
print('\n')

# 2-7
stripper_name = "   magic honeysuckle \n\t"
print(stripper_name)
print(stripper_name.lstrip())
print(stripper_name.rstrip())
print(stripper_name.strip())
print('\n')

# 2-8
print(4 + 4)
print(9 - 1)
print(2 * 2 * 2)
print(16 / 2)
print('\n')

# 2-9
fave_number = 3
print(fave_number)
print('\n')

# 2-10 this literally is a comment

# 2-11
import this
print('\n')

# Chapter Three
print("\n ----------CHAPTER THREE--------- ")

# 3-1
names = ['lydia', 'ashley', 'daniel', 'emmett', 'jacob']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print('\n')

# 3-2
print("Salutations, " + str(names[0].title())+ '!')
print("Salutations, " + str(names[1].title())+ '!')
print("Salutations, " + str(names[2].title())+ '!')
print("Salutations, " + str(names[3].title())+ '!')
print("Salutations, " + str(names[4].title())+ '!')
print('\n')

# 3-3
my_list = [
    "janus custom motorcycle", 'lynx snowmachine', 'brand-name helicopter'
]
print("I would like to ride around Alaska in a " + str(my_list[0]))
print("I would like to ride around Alaska in a " + str(my_list[1]))
print("I would like to ride around Alaska in a " + str(my_list[2]))
print("I don't know any brand-names for helicopters but I'd prefer a safe one")
print('\n')

# 3-4
guest_list = ['Johann Sebastian Bach', 'Dietrich Bonhoeffer', 'Alvin Hoekstra']
print("Greetings, " + str(guest_list[0]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[1]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[2]) + 
', would you like to join me for dinner?')
print('\n')

# 3-5
print(str(guest_list[2]) + " can't make it to dinner.")
guest_list.pop()
# Wonder why grandpa won't make it to dinner
guest_list = [
    'Johann Sebastian Bach', 'Dietrich Bonhoeffer', 'Saint Herman of Alaska'
]
print("Greetings, " + str(guest_list[0]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[1]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[2]) + 
', would you like to join me for dinner?')
print('\n')

# 3-6
guest_list.insert(0, 'Django Reinhardt')
guest_list.insert(3, 'Miles Davis')
guest_list.append('A person who can translate French, ' + 
'German, Russian, and English')
print("Greetings, " + str(guest_list[0]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[1]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[2]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[3]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[4]) + 
', would you like to join me for dinner?')
print("Greetings, " + str(guest_list[5]) + 
', would you like to join me for dinner?')
print('\n')

# 3-7
print("We will only have room for two guests at dinner")
guest_list.pop()
print("Sorry, Mr. Translator, but we will not be able to host you for dinner.")
guest_list.pop()
print("Sorry, St. Herman, but we will not be able to host you for dinner.")
guest_list.pop()
print("Sorry, Mr. Davis, but we will not be able to host you for dinner.")
guest_list.pop()
print("Sorry, Mr. Bonhoeffer, but we will not be able to host you for dinner.")
del guest_list[-1:-2]
print(guest_list)
print('\n')

# 3-8
places_list = ['Tokyo', 'Guam', 'Vienna', 'Iceland', 'Trømso']
print(places_list)
print(sorted(places_list))
print(sorted(places_list, reverse=True))
print('\n')

# 3-9
print(len(guest_list))
print('\n')

# 3-10
mountains_list = ['Silvertip', 'Denali', 'Foraker', 'Doom', 'Olympus']
def every_function(mountain):
    mountains_list = ['Silvertip', 'Denali', 'Foraker', 'Doom', 'Olympus']
    for mountain in mountains_list:
        if 'Foraker' in mountains_list:
            mountains_list.remove('Foraker')
            mountains_list.append(mountain)
            mountains_list.pop()
            print(sorted(mountains_list, reverse=True))
        else:
            mountains_list.pop()
            print(sorted(mountains_list, reverse=False))
        
every_function('Bubblegum')
print('\n')

# 3-11
#for i in 'iiiii':
#print("Index error")

for i in 'iiiii':
    print("Index error")
print('\n')

# Chapter Four
print("\n ----------CHAPTER FOUR--------- ")

# 4-1
pizzas = ["Meat lovers", "gluten free", "dairy free"]
for pizza in pizzas:
    print("I like " + str(pizza) + " pizza.")
print('I really like pizza!')
print('\n')

# 4-2
animals_list = ['dog', 'cat', 'dragon', 'Shrek']
for animal in animals_list:
    print("A " + str(animal) + " would make a decent pet.")
print('Any of these would make a great pet, ' + '\n' +
'but some would require more maintenance than others.')
print('\n')

# 4-3
print(list(range(1, 21)))
print('\n')

# 4-4
numbers = list(range(1,1000001))
#for i in numbers:
#    print(str(i))
print('I commented out this exercise so I could read')
print('\n')

# 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print('\n')

# 4-6
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
print('\n')

# 4-7
threes_list = list(range(3, 33, 3))
print(threes_list)
print('\n')

# 4-8
nums_to_cube = list(range(1,10))
cubed_nums_list = [value**3 for value in nums_to_cube]
print(cubed_nums_list)
print('\n')

# 4-9
last_cubes = [value**3 for value in range(1,11)]
print(last_cubes)

# 4-10
print('The first three items in the list are: ' + str(nums_to_cube[0:3]))
print('Three items from the middle of the list are: ' +str(nums_to_cube[3:6]))
print('The last three items in the list are ' + str(nums_to_cube[-3:]))
print('\n')

# 4-11
pizzas = ["Meat lovers", "gluten free", "dairy free"]
friend_pizzas = ["Meat lovers", "gluten free", "dairy free"]
pizzas.append("buffalo")
friend_pizzas.append("mayonnaise")
print("my favorite pizzas are " + str(pizzas))
print("My friend's favorite pizzas are " + str(friend_pizzas))
print('\n')

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(str(food))
print('\n')

# 4-13
buffet = ("waffles", "pancakes", "steak", "chicken", "rice")
print(buffet)
#buffet[2] = "peanut butter"
#Bonk!
buffet = ("waffles", "pancakes", "steak", "sauce", "pokemon flesh")
print(buffet)
print('\n')

# 4-14
#Style!

# 4-15 
#More style!

# Chapter Five
print("\n ----------CHAPTER FIVE--------- ")

# 5-1
water = 'bottle'
print("Is water == 'bottle'? I predict True.")
print(water == 'bottle')

print("Is water == 'bucket'? I predict False.")
print(water == 'bucket')

paint = 'blue'
print("Is paint == 'blue'? I predict True.")
print(paint == 'blue')

print("Is paint == 'red'? I predict False.")
print(paint == 'red')

German = 'Deutsch'
print("Is German == 'Deutsch'? I predict True.")
print(German == 'Deutsch')

print("Is German == 'Francais'? I predict False.")
print(German == 'Francais')

plane = 'flying'
print("Is plane == 'flying'? I predict True.")
print(plane == 'flying')

print("Is plane == 'crashed'? I predict False.")
print(plane == 'crashed')

binary = '1'
print("Is binary == '1'? I predict True.")
print(binary == '1')

print("Is binary == '0'? I predict False.")
print(binary == '0')

print('\n')

# 5-2
pizza_topping = "pineapple"
if pizza_topping != "pineapple":
    print("PINEAPPLE BELONGS ON PIZZA!")
pizza_topping = "not pineapple"
if pizza_topping != "pineapple":
    print("PINEAPPLE BELONGS ON PIZZA!")

drink = 'Coffee'
print(drink.lower() == 'coffee')
print(5 == 3)
print(5 != 3)
print(5 >= 3)
print(5 > 3)
print(5 <= 3)
print(5 < 3)
print(5 == 3)
print(5 > 3 and 5 != 3)
print(5 < 3 or 5 == 3)
print('Meat lovers' in pizzas)
print('hawaiian' in pizzas)
print('\n')

# 5-3
alien_color = "green"
if alien_color == 'green':
    print('You just earned 5 points!')
alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points!')
print('\n')

# 5-4
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')
alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')
print('\n')

# 5-5
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You just earned 15 points!')
alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You just earned 15 points!')
alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You just earned 15 points!')
print('\n')

# 5-6
age = 26
if age < 2:
    print('This person is a baby.')
elif age >= 2 and age < 4:
    print('This person is a toddler.')
elif age >= 4 and age < 13:
    print('This person is a kid.')
elif age >= 13 and age < 20:
    print('This person is a teenager.')
elif age >= 20 and age < 65:
    print('This person is an adult.')
elif age >= 65:
    print('This person is an elder.')
print('\n')

# 5-7
favorite_fruit = ['salmonberry', 'limequat', 'blueberry']
if 'apples' in favorite_fruit:
    print('You really like apples!')
if 'limequat' in favorite_fruit:
    print('You really like limequat!')
if 'strawberry' in favorite_fruit:
    print('You really like strawberry!')
if 'salmonberry' in favorite_fruit:
    print('You really like salmonberry!')
if 'blueberry' in favorite_fruit:
    print('You really like apples!')
print('\n')

# 5-8
username = ['admin', 'brandon', 'elayne', 'josh', 'lydia']
for user in username:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + str.title(user) + 
        ", thank you for logging in again")
print('\n')

# 5-9
username = []
if username == []:
    print("We need to find some users!")
print('\n')

# 5-10
current_users = ['admin', 'brandon', 'elayne', 'josh', 'lydia']
new_users = ['mike', 'brandon', 'elayne', 'rachelle', 'mama']

for user in new_users:
    if user.lower() in current_users:
        print("You need a new username")
    else:
        print("Username available!")

# 5-11
numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in numlist:
    if num == '1':
        print('1st')
    elif num == '2':
        print('2nd')
    elif num == '3':
        print('3rd')
    else:
        print(str(num) + "th")
print('\n')

# 5-12
# okay

# 5-13
#Like I said earlier, I'm not an entrepreneur, which is part of why I'd like
#to go into data or team-based development rather than making something from
#scratch by myself. I know my strengths and weaknesses and would rather 
#start using my strengths than try to pretend my weaknesses aren't what 
#they are.
#
# I talked with a friend of mine who had the idea of an advertisement-creating 
# application that he could use for companies that wanted to create ads. Many
# ads are expensive and difficult to create and as a result many companies 
#either don't use video-based advertisements or they do it very poorly. He 
# would like to create an application that uses stock footage to make ads.
#It would be subscription-based and very inexpensive, syncing video to audio
#and permitting loyal customers to create a variety of story-based
#advertisements for very cheap.

# Chapter Six
print("\n ----------CHAPTER SIX--------- ")

# 6-1
lydia_apol = {
    'first_name': "lydia",
    'last_name': 'apol',
    'city': "fairbanks",
}

print(lydia_apol['first_name'].title())
print(lydia_apol['last_name'].title())
print('\n')

# 6-2
favorite_numbers = {
    'daniel': 5,
    'ashley': 7,
    'jacob': 8,
    'ben': 3,
    'patrick': 2,
}

print(favorite_numbers['daniel'])
print(favorite_numbers['jacob'])
print(favorite_numbers['ashley'])
print(favorite_numbers['patrick'])
print(favorite_numbers['ben'])
print('\n')

# 6-3
glossary = {
    'dictionary': 'Connects pieces of real-world information',
    'tuple': 'Immutable list',
    'variable': 'something that holds a value',
    'for loop': 'a function that iterates through a list of items and applies' +
    'a process to each item',
    'if function': 'a function that separates data based on criteria',
}

# 6-4
glossary = {
    'dictionary': 'Connects pieces of real-world information',
    'tuple': 'Immutable list',
    'variable': 'something that holds a value',
    'for loop': 'a function that iterates through a list of items and' + 
    '\n applies a process to each item',
    'if function': 'a function that separates data based on criteria',
    'list': 'a collection of items in a particular order',
    'syntax': 'the required order and arrangement of functional commands',
    'index': 'the positioning of items within a list',
    'keys': 'the initial item in a dictionary',
    'values': 'the dependent item in a dictionary',
}
# I would like to be able to append entire key: value pairs to the glossary 
#without rewriting the entire dictionary, but it seemed very sloppy and all the
#online examples on stackoverflow were examples of a series of keys with no
#values to go with; can I append keys or only assign new values to keys?
for word, definition in glossary.items():
    print(word.title() + ": " + definition.title())
print('\n')

# 6-5
rivers = {
    'lowe': 'valdez',
    'tenana': 'fairbanks',
    'susitna': 'anchorage'
}
for river, town in rivers.items():
    print('The ' + river.title() + ' River runs through ' + town.title() + '.')
print('\n')

# 6-6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

favorite_languages_names = ['jen', 'phil', 'jerome', 'sean', 'talyla']

for name in favorite_languages_names:
    if name in favorite_languages.keys():
        print('Thank you, ' + str(name).title() + ', for responding.')
    else:
        print('Please take the poll, ' + str(name).title() + '!')
print('\n')

# 6-7
people = {
    'wife': {
        'first_name': "lydia",
        'last_name': 'apol',
        'city': "fairbanks",
    },
    'me': {
        'first_name': 'brandon',
        'last_name': 'apol',
        'city': 'fairbanks',
    },
    'ski buddy': {
        'first_name': 'jacob',
        'last_name': 'buller',
        'city': 'anchorage',
    }
}
for person, data in people.items():
    print("Person: " + person.title())
    print('Their name is ' + data['first_name'].title() + ' ' +
    data['last_name'].title() + ' and they live in ' + data['city'].title() + 
    '.')
print('\n')

# 6-8
pets = {
    'dixie': {
        'owner': 'Mike',
        'breed': 'mutt',
    },
    'bella': {
        'owner': 'Mama Fitz',
        'breed': 'mini dachsund',
    },
    'ronaldo': {
        'owner': 'Michael',
        'breed': 'dachsund',
    },
}
for dog, facts in pets.items():
    print('Dog name: ' + dog.title())
    print('Owner and breed: ' + facts['owner'].title() + ', ' + 
    facts['breed'].title())
print('\n')

# 6-9
favorite_places = {
    'joe': {
        'location': ['ketchikan', 'detroit']
    },
    'lydia': {
        'location': ['barcelona', 'new zealand', 'china']
    },
    'bethany': {
        'location': ['azerbaijan', 'pakistan']
    },
}



#Having a hard time getting it to print the locations alone
for name, place in favorite_places.items():
    print('Name: ' + name.title())
    desired_location = place
    for barf, location in desired_location.items():
        print('Place: ' + str(location))
#it's ugly, but it works for today... will revisit
print('\n')

# 6-10
favorite_numbers = {
    'daniel': [5, 8],
    'ashley': [7, 4, 1],
    'jacob': [8, 11, 2],
    'ben': [3, 6, 9],
    'patrick': [2],
}
for name, numbers in favorite_numbers.items():
    print("Name: " + name.title())
    nums_list = numbers
    print('Numbers: ')
    for num in nums_list:
        print(str(num))
print('\n')

# 6-11
cities = {
    'fairbanks': {
        'country': 'USA',
        'population': 50000,
        'fact': 'Coldest city in North America most of the time',
    },
    'vienna': {
        'country': 'austria',
        'population': 1800000,
        'fact': "Beethoven's hometown",
    },
    'tokyo': {
        'country': 'Japan',
        'population': 9270000,
        'fact': 'I grew up here',
    },
}
for name, place in cities.items():
    print('Name: ' + name.title())
    print('Country: ' + place['country'].title())
    print('Population: ' + str(place['population']))
    print('Fact: ' + place['fact'])
# Really proud that that actually worked
print('\n')

# 6-12
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'gcarver': {
        'first': 'george washington',
        'last': 'carver',
        'location': 'tuskegee',
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
print('\n')

# Chapter Seven
print("\n ----------CHAPTER SEVEN--------- ")

# 7-1
#rental_car = input("What kind of car would you like? ")
#print("Let me see if we have any " + rental_car + "s in stock.")
#print('\n')

# 7-2
#restaurant_seating = input('How many people are in your dinner group? ')
#restaurant_seating = int(restaurant_seating)
#if restaurant_seating >= 8:
    #print("You will have to wait for a table.")
#else:
    #print('Your table is ready!')
#print('\n')

# 7-3
#mult_of_ten = input("Give me a number: ")
#mult_of_ten = int(mult_of_ten)
#if mult_of_ten % 10 == 0:
    #print("Your number is a multiple of ten.")
#else:
    #print("Your number is not a multiple of ten.")
#print('\n')

# 7-4
#prompt = "Which toppings would you like on your pizza? "
#while True:
#    toppings = input(prompt)
#    if toppings == 'quit':
#        break
#    else:
#        print(toppings)
#print('\n')

# 7-5
#ovie_tickets = input("What is your age? ")
#movie_tickets = int(movie_tickets)
#if movie_tickets < 3:
#    print("Your ticket is free!")
#elif movie_tickets >= 3 and movie_tickets < 12:
#    print("Your ticket will be $10.")
#else:
#    print("Your ticket will be $15.")
#print('\n')

# 7-6
#prompt = "Which toppings would you like on your pizza? "
#active = True
#while active:
#    toppings = input(prompt)
#    if toppings == 'quit':
#        break
#    else:
#        print(toppings)
##This meets the requirements for all three stipulations.
#print('\n')

# 7-7
#x = 1
#while x <= 10:
#print(x)
#I already did this sort of thing earlier trying to print mountain names out
#with a loop. Screen just said 'denali' thousands of times.
#print('\n')

# Why won't for loops work when while loops do for lists?
# Skipped user[0] when I tried it.

# 7-8
#sandwich_orders = ['BLT', 'Reuben', 'Philly Cheesesteak',]
#finished_sandwiches = []
#while sandwich_orders:
#    current_sandwich = sandwich_orders.pop()
#    print('Your ' + current_sandwich + ' order is ready.')
#    finished_sandwiches.append(current_sandwich)
#print('These sandwiches were made: ' + str(finished_sandwiches))
#print('\n')

# 7-9
sandwich_orders = ['BLT', 'Reuben', 'Philly Cheesesteak', 
'pastrami', 'pastrami', 'pastrami', ]
finished_sandwiches = []
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        print('We are out of pastrami.')
    current_sandwich = sandwich_orders.pop()
    print('Your ' + current_sandwich + ' order is ready.')
    finished_sandwiches.append(current_sandwich)
print('These sandwiches were made: ' + str(finished_sandwiches))
print('\n')

# 7-10
#vacation_location = []
#polling_active = True
#while polling_active:
#    dream_vacation = input('If you could visit one place in the world, where ' + 
#    'would you go? ')
#    vacation_location.append(dream_vacation)
#    repeat = input("Would you like to add another place? (yes/ no) ")
#    if repeat == 'no':
#        polling_active = False
#for i in vacation_location:
#    print('You would like to visit ' + str(i).title() + '.')
#print('\n')

# Chapter Eight
print("\n ----------CHAPTER EIGHT--------- ")

def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")

#greet_user(input('What is your name? '))

# 8-1
def display_message():
    print('We are learning about functions and calls.')

display_message()
print('\n')

# 8-2
def favorite_book(title):
    print('One of my favorite books is ' + title.title() + '.')

favorite_book('The Great Divorce')
print('\n')

# 8-3
# 8-4
def make_shirt(size='large', text='I love Python.'):
    print('Your shirt is size ' + str(size) + ' and it reads, "' + text + '"')

make_shirt(9, 'I like spaghetti')
print('\n')
make_shirt()
make_shirt(size='medium', text='another message!')
print('\n')

# 8-5
def describe_city(city='London', country='England'):
    print('The city of ' + city.title() + ' is in ' + country.title() + '.')
describe_city('Reykjavik', 'Iceland')
describe_city('Tokyo', 'Japan')
describe_city('Montreal', 'Canada')
print('\n')

# 8-6
def city_country(city, country):
    returned_pair = (city.title()) + ', ' + (country.title())
    return returned_pair

print(city_country('santiago', 'chile'))
print(city_country('buenos aires', 'argentina'))
print(city_country('sao paolo', 'brazil'))
print('\n')

# 8-7
# def make_album(name, title, tracks=''):
#     album_short = {'artist': name, 'album': title}
#     album_long = {'artist': name, 'album': title, 'tracks': str(tracks)}
#     if tracks == '':
#         return album_short
#     else:
#         return album_long

# # 8-8
# while True:
#     print('\n Name your favorite artist and album.')
#     print('(press "q" to quit.')
#     album_artist_info = input('Artist: ')
#     if album_artist_info == 'q':
#         break
#     album_name_info = input('Album: ')
#     if album_name_info == 'q':
#         break
#     track_number_info = input('Track Number: ')
#     if track_number_info == '':
#         track_number_info = ''
#     print(make_album(album_artist_info, album_name_info, track_number_info))
#     print(make_album('Aaron Frazer', 'Introducing...'))
#     print(make_album('NOFX', 'The War On Errorism'))
#     print(make_album('Kacey Musgraves', 'Golden Hour', 13))
print('\n')

# 8-9
def show_magicians(magicians):
    for i in magicians:
        print(i)

magicians_names = ['Houdini', 'Copperfield', 'Angel']
great_magicians = []
show_magicians(magicians_names)

# 8-10
#modify list
def make_great(magician_list, finished_list):
    for magician in magician_list:
        greatened_magician = "The Great " + magician
        great_magicians.append(greatened_magician)

# Print out the list that I've changed
# Opted against modifying the original list, will mess about with it in sandbox
# Update: The text doesn't make it clear how to modify an actual list from in
# a function, which is driving me nuts. StackOverflow likewise is proving 
# difficult to find the answer to my question. Spent a full day trying to 
# figure it and at this point I'll be bald before I get it. Planning on calling
# a programmer friend from college to ask later.

make_great(magicians_names, great_magicians)  

# 8-11
# Maybe I misunderstood the directions, since it seems on this question like 
# I did what I was supposed to.
show_magicians(great_magicians)
show_magicians(magicians_names)
print('\n')

# 8-12
def make_sandwich(*sandwich_toppings):
    print('\nYour sandwich has: ')
    for topping in sandwich_toppings:
        print('- ' + topping)

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('steak', 'cheese')
make_sandwich('just a half pound of ketchup, you weirdo')
print('\n')

# 8-13
def build_profile(first, last, **user_data):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_data.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', 
location='princeton', field='physics')
print(user_profile)
print('\n')
user_profile = build_profile('brandon', 'apol', 
location='Fairbanks', field='music education', wife='lydia apol')
print(user_profile)
print('\n')

# 8-14
def make_car(make, model, **auto_data):
    auto = {}
    auto['make'] = make
    auto['model'] = model
    for key, value in auto_data.items():
        auto[key] = value
    return auto

your_auto = make_car('volkswagen', 'jetta', color='black', engine='1.6L')
print(your_auto)
print('\n')

# 8-15
# See printing_models.py

# 8- 16
# import print_example
# from print_example import printing_function
# from print_example import printing_function as pf
# import print_example as pe
from print_example import *
printing_function('Here is my text input')

# 8-17
#I did it

# Other Problems
print("\n ----------Other Problems--------- ")

# Indentation
# The Three Ways
# # Step by step
# # Branching
# # Looping

# Question 1
def hello_name(user_name):
    print(user_name)

hello_name('Brandon')

print('\n')
# Question 2
no = 0
while no < 100:
    no += 1
    if no % 2 != 0:
        print(no)

print('\n')

# Question 3
def max_num_in_list(a_list):
    print('The largest item is ' + str(max(a_list)))

list_of_nums = [0, -1, 55, 9000, 9001]
max_num_in_list(list_of_nums)

print('\n')

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 == 0:
            return True
        elif a_year % 100 == 0 and a_year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

print(is_leap_year(400))
print(is_leap_year(300))
print(is_leap_year(2021))
print(is_leap_year(4))
print(is_leap_year(3))
print(is_leap_year(800))
print(is_leap_year(2000))

print('\n')

# Question 5
# pseudocode = 'Make a function that finds the min and max numbers in a list;' + 
# 'then sort the list and create another list that is those consecutive numbers;' +
# ' finally see if the two lists are == and spit out a result'
# def is_consecutive(example_list):
#     stupid_list = []
#     for item in example_list:
#         stupid_list.append(item)
#     total_range = range(stupid_list(0, -1))
#     print(total_range)

# quick_list = [0, 1, 2, 3]
# is_consecutive(quick_list)

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
        print(status)

a_list = [1, 2, 3, 4, 5]

is_consecutive()

print('\n')
print('\n')
print('\n')
print('\n -------------SANDBOX----------')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)
#YO THIS IS COOL

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
    #print(name.title())

    #if name in friends:
        #print(" Hi " + name.title() +
            #", I see your favorite language is " +
            #favorite_languages[name].title() + "!")

#if user not in banned_users:
    #print(user.title() + ", you can post a response if you wish.")

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

#unconfirmed_users = ['alice', 'brian', 'candace']
#confirmed_users = []

#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#
#    print("Verifying user: " + current_user.title())
#    confirmed_users.append(current_user)

#print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#print(confirmed_user.title())

#__________________
#print('\n')

#unconfirmed_users = ['alice', 'brian', 'candace']
#confirmed_users = []

#for user in unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#
#    print("Verifying user: " + current_user.title())
#    confirmed_users.append(current_user)

#print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#print(confirmed_user.title())

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)