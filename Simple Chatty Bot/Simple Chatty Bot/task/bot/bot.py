print('Hello! My name is Aid.')
print('I was created in 2020.')

name = input('Please, remind me your name.')

print(f'''
What a great name you have, {name}!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

# reading all remainders

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")
