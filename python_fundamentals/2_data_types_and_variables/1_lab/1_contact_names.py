def contact_names(first_name, second_name, delimiter):
    return first_name + delimiter + second_name


first_name = input()
second_name = input()
delimiter = input()

print(contact_names(first_name, second_name, delimiter))
