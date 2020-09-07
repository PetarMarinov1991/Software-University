def calculate_sum(numbers):
    return sum([int(num) for num in numbers])


file_path = './files/File Reader/numbers.txt'

try:
    print(calculate_sum(open(file_path, 'r')))
except FileNotFoundError or ValueError:
    print('Error')
