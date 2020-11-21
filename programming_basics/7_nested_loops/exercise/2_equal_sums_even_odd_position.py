start = int(input())
end = int(input())

for number in range(start, end + 1):
    num = str(number)

    even_sum = int(num[0]) + int(num[2]) + int(num[4])
    odd_sum = int(num[1]) + int(num[3]) + int(num[5])

    if even_sum == odd_sum:
        print(num, end=' ')
