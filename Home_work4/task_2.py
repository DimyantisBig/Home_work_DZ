num = input("Enter a number: ")
if len(num) > 10:
    print('Your number is too long')
elif num.isdigit():
    print('Good number, thank you')
else:
    print('Incorrect input')


