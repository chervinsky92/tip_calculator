# Tip calculator

total = float(input('What was the total bill? $'))
tip = 1 + float(input('What percentage tip would you like to give? 10, 12, or 15? ')) / 100
total_with_tip = total * tip

people = int(input('How many people to split the bill? '))

print(f'Each person should pay: ${(total_with_tip/people):.2f}')