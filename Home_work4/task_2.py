num = input("Enter a number: ")
if len(num) != 10:
    print('Your number is wrong')
elif num.isdigit():
    print('Good number, thank you')
else:
    print('Incorrect input')


