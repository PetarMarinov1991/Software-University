one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_bills = int(input())
my_sum = int(input())

for coin_1 in range(one_lv_coins + 1):
    for coin_2 in range(two_lv_coins + 1):
        for bill_5 in range(five_lv_bills + 1):

            if coin_1 * 1 + coin_2 * 2 + bill_5 * 5 == my_sum:
                print(f'{coin_1} * 1 lv. + {coin_2} * 2 lv. + {bill_5} * 5 lv. = {my_sum} lv.')

