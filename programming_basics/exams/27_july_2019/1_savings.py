income = float(input())
months = int(input())
expenses = float(input())

unexpected_expenses = income * 0.30
monthly_savings = income - (expenses + unexpected_expenses)
total_savings = monthly_savings * months
percent = (monthly_savings / income) * 100

print(f'She can save {percent:.2f}%\n{total_savings:.2f}')
