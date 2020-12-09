import random
import sys
# -*- coding: utf-8 -*-

print("         เกมทอยลูกเต๋าแข่งกับบอท")
print("               [กติกา]")
print("    เดาผลรวมของลูกเต๋าตั้งแต่ 2 ถึง 12")
print("หากแต้มอีกฝ่าย'หมด'ก่อนหรือแต้มถึง'15'ก่อนชนะ")
def roll_dice_and_compute_sum(ndice):
    return sum([random.randint(1, 6) \
                for i in range(ndice)])

def computer_guess(ndice):
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    return input('เดาผลรวมของการทอยลูกเต๋า :')

def play_one_round(ndice, capital, guess_function):
    guess = guess_function(ndice)
    throw = roll_dice_and_compute_sum(ndice)
    if guess == throw:
        capital += guess
    else:
        capital -= 1
    return capital, throw, guess

def play(nrounds, ndice=2):
    player_capital = computer_capital = nrounds  # start capital

    for i in range(nrounds):
        player_capital, throw, guess = \
             play_one_round(ndice, player_capital, player_guess)
        print('คุณเดา %s, ลูกเต๋าออก %s' % (guess, throw))

        computer_capital, throw, guess = \
            play_one_round(ndice, computer_capital, computer_guess)
        print('บอทเดา %s, ลูกเต๋าออก %s' % (guess, throw))

        print('สถานะ: คุณมี %s แต้ม, บอทมี %s แต้ม\n' % \
              (player_capital, computer_capital))

        if player_capital == 0 or computer_capital == 0 or player_capital >=15 or computer_capital >= 15:
            break

    if computer_capital > player_capital:
        winner = 'บอท'
        print(winner, 'ชนะ!')
    elif computer_capital == player_capital:
        print("เสมอ")
    else:
        winner = 'คุณ'
        print(winner, 'ชนะ!')

if __name__ == '__main__':
    play(10)