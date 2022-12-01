from math import ceil

people = int(input())
elevator_capacity = int(input())

courses = ceil(people / elevator_capacity)

print(courses)
