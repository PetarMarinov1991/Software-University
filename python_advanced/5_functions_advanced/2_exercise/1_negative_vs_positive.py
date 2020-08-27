def stronger_sum(numbers):
    positives_sum = sum([int(num) for num in numbers if int(num) > 0])
    negatives_sum = sum([int(num) for num in numbers if int(num) < 0])
    print(negatives_sum)
    print(positives_sum)
    if abs(negatives_sum) > positives_sum:
        return 'The negatives are stronger than the positives'
    return 'The positives are stronger than the negatives'


print(stronger_sum(input().split()))
