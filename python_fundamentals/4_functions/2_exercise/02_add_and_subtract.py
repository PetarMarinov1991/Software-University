def add_and_subtract(numbers):

    def sum_numbers():
        return numbers[0] + numbers[1]

    def subtract():
        return sum_numbers() - numbers[2]

    return subtract()


numbers = [int(input()) for _ in range(3)]
print(add_and_subtract(numbers))
