my_sheep = input().split(", ")

if my_sheep.pop() == "wolf":
    print("Please go away and stop eating my sheep")
    exit(0)

queue = my_sheep[::-1]

for sheep in range(len(queue)):
    if not queue[sheep] == "sheep":
        print(f"Oi! Sheep number {sheep + 1}! You are about to be eaten by a wolf!")
        break
