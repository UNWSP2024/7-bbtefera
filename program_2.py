# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.
def number(l, n):
    for num in l:
        if num > n:
            print(num)

numbers = [10, 25, 30, 45, 5, 60, 15]
threshold = int(input("Enter a number: "))
number(numbers, threshold)
