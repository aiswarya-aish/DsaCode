actual_amount = input('Enter the total amount : ')

amount_paid = input('Enter the amount paid: ')

balance_amount = amount_paid - actual_amount
inr = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
result = {}

for rs in inr:
    if rs <= balance_amount:
        count = balance_amount // rs
        result[rs] = count
        balance_amount -= rs * count

print(result)

