from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


class Dice_static:
    def __init__(self, dice_number, die_edges, number_of_rolls):
        self.dice_number = dice_number
        self.die_edges = die_edges
        self.number_of_rolls = number_of_rolls
        max_res = 0
        for x in die_edges:
            max_res = max_res + x
        self.max_res = max_res

    # создает список результатов бросков
    def dice_rolls(self):

        results = []
        for roll_num in range(self.number_of_rolls):
            result_of_roll = []
            result = 0
            for i in range(self.dice_number):
                die = Die(self.die_edges[i])
                result_of_roll.append(die.roll())
            for i in range(len(result_of_roll)):
                result = result + result_of_roll[i]
            results.append(result)
        return results

    # создает список частоты результатов бросков(требует результат бросков dice_rolls)
    def counting(self, res: list):
        frequencies = []
        for value in range(self.dice_number, self.max_res + 1):
            frequency = res.count(value)
            frequencies.append(frequency)
        return frequencies

    # создает график(требует частоту выпадения - вычисляет counting)
    def graff(self, freq):
        data = [Bar(x=list(range(self.dice_number, self.max_res + 1)), y=freq)]
        x_axis_config = {'title': 'Result'}
        y_axis_config = {'title': 'frequency of Result'}
        my_layout = Layout(title='Result of rolling', xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({'data': data, 'layout': my_layout}, filename='result_of_roll.html')


def init_dice_rolling():
    dice_number = int(input('number of dice? '))  # запрос на количество кубов

    die_edges = []  # создание списка в котором будет храниться количество граней для каждого куба
    for i in range(dice_number):  # непосредственно опрос сколько у каждого куба граней, при пропуске
        die_edges.append(int(input('number of edges? ')))  # количество граней приравнивается к 6

    number_of_rolls = int(input('number of rolls? '))  # количество бросков
    challenge = Dice_static(dice_number, die_edges, number_of_rolls)  # хз, но кажется именно вызов этого класса
    ch_dice_rolls = challenge.dice_rolls()  # начинает работу
    county = challenge.counting(ch_dice_rolls)
    challenge.graff(county)  # формирование графа с результатами


init_dice_rolling()
