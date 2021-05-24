def hello_name(user_name):
    print('Hello, ' + user_name.title() + '!')

def greeting(user_name):
    print('hello, {}!'.format(user_name.title()))
    print(f'Hello again {user_name.title()}!')

hello_name('Brandon')
greeting('Brandon')

def odd_numbers():
    for i in range(0, 100):
        if i % 2 != 0:
            print(i)

#odd_numbers()