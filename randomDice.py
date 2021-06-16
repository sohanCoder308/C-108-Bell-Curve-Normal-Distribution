import random
import plotly.express as px

result = []
count = []

for i in range(0, 1000):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    # print(first_dice, second_dice)
    dice1_plus_dice2 = first_dice + second_dice
    result.append(dice1_plus_dice2)
    count.append(i)

madeBySohanFigure = px.bar(x = result, y = count)
madeBySohanFigure.show()    