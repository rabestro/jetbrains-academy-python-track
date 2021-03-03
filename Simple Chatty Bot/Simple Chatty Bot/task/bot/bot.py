print('Hello! My name is Aid.')
print('I was created in 2020.')

name = input('Please, remind me your name.')

print(f'''
What a great name you have, {name}!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print(f"""Your age is {age}; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.""")

# read a number and count to it here
number = int(input())
counter = 0
while counter <= number:
    print(str(counter) + " !")
    counter += 1
print('Completed, have a nice day!')
