def sign(num1, num2, num3):
    numbers = [num1, num2, num3]
    if 0 in numbers:
        return 'zero'
    negatives = [num for num in numbers if num < 0]
    if len(negatives) == 1 or len(negatives) == 3:
        return 'negative'
    else:
        return 'positive'


print(sign(num1=int(input()), num2=int(input()), num3=int(input())))
