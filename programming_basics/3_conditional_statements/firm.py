import math

hours_needed = int(input())
deadline = int(input())
overtime_workers_count = int(input())

work_time = deadline * 0.9 * 8
overtime = overtime_workers_count * (2 * deadline)
total_hours = math.floor(work_time + overtime)

if hours_needed <= total_hours:
    print(f'Yes!{total_hours - hours_needed} hours left.')
else:
    print(f'Not enough time!{hours_needed - total_hours} hours needed.')