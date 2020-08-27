side_size = float(input())
num_of_sheets = int(input())
area_of_sheet = float(input())

gift_box_area = side_size ** 2 * 6
third_sheet = num_of_sheets // 3
regular_sheet = num_of_sheets - third_sheet

covered_area = regular_sheet * area_of_sheet + third_sheet * (area_of_sheet / 4)
percentage = covered_area / gift_box_area * 100

print(f'You can cover {percentage:.2f}% of the box.')
