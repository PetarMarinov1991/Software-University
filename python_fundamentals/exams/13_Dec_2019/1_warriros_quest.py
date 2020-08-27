skill = input()

while True:
    command = input()

    if command == 'For Azeroth':
        break

    command = command.split()

    if command[0] == 'GladiatorStance':
        skill = skill.upper()
        print(skill)
    elif command[0] == 'DefensiveStance':
        skill = skill.lower()
        print(skill)
    elif command[0] == 'Dispel':
        idx, letter = int(command[1]), command[2]
        if 0 < idx < len(skill):
            skill = skill.replace(skill[idx], letter)
            print('Success!')
        else:
            print('Dispel too weak.')
    elif command[0] == 'Target':
        if command[1] == 'Change':
            substring, second_substring = command[2], command[3]
            skill = skill.replace(substring, second_substring)
            print(skill)
        elif command[1] == 'Remove':
            substring = command[2]
            skill = skill.replace(substring, '')
            print(skill)
    else:
        print("""Command doesn't exist!""")
