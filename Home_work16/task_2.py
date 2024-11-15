class Mathematician:
    def __init__(self):
        pass
    def square_nums (self):
        num_list = list(range(8))
        square_numbers = [num ** 2 for num in num_list ]
        return f'Numbers squared: {square_numbers}'

    def remove_positives (self):
        num_list1 = list(range(-8,8))
        remove_pos = [num for num in num_list1 if num < 0]
        return f'This list only negative numbers: {remove_pos}'

    def filter_leaps (self):
        num_list2 = list(range(1900,2024,5))
        leap_year = []
        for year in num_list2:
            if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
                leap_year.append(year)
        return f'This is a leap year {leap_year}.'



sq = Mathematician ()
print(sq.square_nums())

rp = Mathematician()
print( rp.remove_positives())

nl = Mathematician ()
print(nl.filter_leaps())