"""
Задача:
Учитывая целое число num, несколько раз складывать все его цифры, пока результат
не будет содержать только одну цифру, и возвращать его.
Example 1:
Input: num = 38
Output: 2
Explanation: Процесс
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Поскольку 2 имеет только одну цифру, верните ее.
Example 2:
Input: num = 0
Output: 0

"""
def addDigits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9
    
print(addDigits(38))
print(addDigits(0))
    