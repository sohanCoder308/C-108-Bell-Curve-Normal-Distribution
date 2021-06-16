import random
import plotly.figure_factory as pff

result = []
count = []

for i in range(0, 100):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    # print(first_dice, second_dice)
    dice1_plus_dice2 = first_dice + second_dice
    result.append(dice1_plus_dice2)
    count.append(i)

figure = pff.create_distplot([result],["Result"])
figure.show()