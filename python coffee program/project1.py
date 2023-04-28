import time
import random

# class definition
class Coffee:
    'Coffee class'
    cofcount = 0

    def __init__(self, water, milk, coffee, mocha, heat, price, rank, name):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.mocha = mocha
        self.heat = heat
        self.price = price
        self.rank = rank
        self.name = name
        Coffee.cofcount += 1

Cappuccino = Coffee(50, 50, 50, 0, 1.2, 12, 1, 'Cappuccino')
Latte = Coffee(80, 20, 50, 0, 1.0, 10, 2, 'Latte')
Mocha = Coffee(50, 50, 40, 10, 1.4, 15, 3, 'Mocha')
Cafe_Americano = Coffee(100, 0, 50, 0, 0.8, 10, 4, 'Cafe Americano')
Espresso = Coffee(70, 0, 80, 0, 1.3, 14, 5, 'Espresso')

# material
material = {'Water': 100, 'Milk': 500, 'Coffee': 500, 'Mocha': 200}

# bookkeeping
sell_record = {'Cappuccino': 0, 'Latte': 0, 'Mocha': 0, 'Cafe Americano': 0, 'Espresso': 0, 'Money': 0}

# function definition
def select_coffee(select_num, select_list=[Cappuccino, Latte, Mocha, Cafe_Americano, Espresso]):
    if select_num == 'Q' or select_num == 'q':
        return 'continue'
    elif select_num == 'quit':
        return 'quit'
    for selected_coffee in select_list:
        if int(select_num) == selected_coffee.rank:
            return selected_coffee

def count_cash():
    twenty = int(input('how many 20￥count? : '))
    ten = int(input('how many 10￥count? : '))
    five = int(input('how many 5￥count? : '))
    one = int(input('how many 1￥count? : '))
    return twenty * 20 + ten * 10 + five * 5 + one

# main process
while True:
    # initial state
    print('***********************************************************************************\n + \
           **********************A nice day starts with a cup of coffee!**********************\n + \
           ***********************************************************************************')
    print('1. Cappuccino [Water: 50ml, Milk: 50ml, Coffee: 50ml; Heat: 1.2 kcal]: 12￥\n + \
           2. Latte [Water: 80ml, Milk: 20ml, Coffee: 50ml; Heat: 1.0 kcal]: 10￥\n + \
           3. Mocha [Water: 50ml, Milk: 50ml, Coffee: 40ml, Mocha: 10ml; Heat: 1.4 kcal]: 15￥\n + \
           4. Cafe Americano [Water: 100ml, Milk: 0ml, Coffee: 50ml; Heat: 0.8 kcal]: 10￥\n + \
           5. Espresso [Water: 70ml, Milk: 0ml, Coffee: 80ml; Heat: 1.3 kcal]: 14￥\nQuit [Q/q] ')
    print('***********************************************************************************')

    # select coffee
    select_num = input('Please select your item: ')
    selected_coffee = select_coffee(select_num)
    if selected_coffee == 'continue':
        continue
    elif selected_coffee == 'quit':
        break
    need_to_pay = selected_coffee.price

    # material check
    
    while True:
        if selected_coffee == 'continue':
            continue
        elif selected_coffee == 'quit':
            break
        elif material['Water'] < selected_coffee.water or material['Milk'] < selected_coffee.milk or material['Coffee'] < selected_coffee.coffee or material['Mocha'] < selected_coffee.mocha:
            print(f'Sorry, {selected_coffee.name}\' material is not enough, please select another one.')
            select_num = input('Please select your item: ')
            selected_coffee = select_coffee(select_num)
        else:
            break_condition = input('Your item is available, please enter \'c\' to continue: ')
            if break_condition == 'c':
                break
    if selected_coffee == 'quit':
        break

    # lucky number game
    game_switch = input('Do you want to attend the lucky number game? [y/n]: ')

    if game_switch == 'n':
        pass
    else:
        lucky_number = str(input('Please input your lucky number (integer from 0-9): '))
        random_number = str(random.randint(1, 1000))
        if lucky_number == random_number[-1]:
            print('Congratulations! You win the game and luckily win a 15%% discount!')
            need_to_pay = selected_coffee.price * 0.85
        else:
            print('Sorry you didn\'t win the game')

    # coupon check
    coupon_switch = input('Is a coupon available? [y/n]: ')

    if coupon_switch == 'n':
        pass
    else:
        coupon_id = int(input('Please input your coupon No.: '))
        qualified_id = random.randint(4312000, 4312999)
        if coupon_id == qualified_id:
            discount_num = round(random.uniform(0.7, 0.9), 2)
            print(f'Congratulations! You win a {100 - discount_num * 100}%% discount!')
            need_to_pay = need_to_pay * discount_num
        else:
            print('Sorry, your coupon is not available')

    print(f'Your item price after all discount is: {need_to_pay}￥')

    # pay part
    print('Please enter your cash, ')

    already_pay = count_cash()
    exit_switch = False
    while already_pay < need_to_pay:
        keep_switch = str(input('Please continue to insert your cash [c] or quit with [q]: '))
        if keep_switch == 'q':
            exit_switch = True
            break
        else:
            already_pay += count_cash()
    if exit_switch:
        continue

    print(f'Your total amount is: {already_pay}; Your change is {already_pay - need_to_pay}')
    donate_research = str(input('Do you want to donate your loose change? [y/n]: '))
    print(f'Your change is: {already_pay - need_to_pay}, please receipt it!')

    # production process
    print('**Your coffee is making:')
    time.sleep(0.5)
    print('------------------------------------------------------------------')
    time.sleep(0.5)
    print('**Coffee preparing finished!')
    time.sleep(0.5)
    print('------------------------------------------------------------------')
    time.sleep(0.5)
    print('**Coffee making finished!')
    time.sleep(0.5)
    print('------------------------------------------------------------------')
    time.sleep(0.5)
    print('** Coffee packaging finished!')
    print('------------------------------------------------------------------')

    # material update
    material['Water'] -= selected_coffee.water
    material['Milk'] -= selected_coffee.milk
    material['Coffee'] -= selected_coffee.coffee
    material['Mocha'] -= selected_coffee.mocha

    # sell record update
    sell_record[selected_coffee.name] += 1
    sell_record['Money'] += need_to_pay

    # return to menu
    return_to_menu = input('Please take your coffee carefully! Press [R/r] to return the menu: ')
    if return_to_menu == 'Q' or return_to_menu == 'q':
        break

print('***********************************************************************************\n + \
      ******************************welcome to backstage*******************************\n + \
      ***********************************************************************************')
print(f'Sell record: {sell_record}')