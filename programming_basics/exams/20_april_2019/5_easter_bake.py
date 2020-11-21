from math import ceil

easter_bread_count = int(input())

total_sugar_used = 0
total_flour_used = 0

max_sugar = 0
max_flour = 0

for easter_bread in range(easter_bread_count):
    gr_sugar = int(input())
    gr_flour = int(input())

    total_sugar_used += gr_sugar
    total_flour_used += gr_flour

    if gr_sugar > max_sugar:
        max_sugar = gr_sugar

    if gr_flour > max_flour:
        max_flour = gr_flour

package_sugar = ceil(total_sugar_used / 950)
package_flour = ceil(total_flour_used / 750)

print(f'Sugar: {package_sugar}')
print(f'Flour: {package_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
