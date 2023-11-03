#Доопрацюйте гру зі свого попереднього дз наступним чиноом:
# A. Обʼєкт гри може отримати тільки обʼєкти гласу Гравець
# B. Додайте до класу гри класметод, виклик якого виведе на екран інформацію про правила гри ("Гра [тут назва гри].
# Гравцям потрібно обрати одну з фігур [тут перелік ігрових фігур з класу] і перемогти опонента")
class Figure:
    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class Scissors(Figure):
    def __init__(self):
        super().__init__('Scissors')

    def __gt__(self, other):
        return isinstance(other, Paper) or isinstance(other, Lizard)

    def __eq__(self, other):
        return isinstance(other, Scissors)


class Paper(Figure):
    def __init__(self):
        super().__init__('Paper')

    def __gt__(self, other):
        return isinstance(other, Rock) or isinstance(other, Spock)

    def __eq__(self, other):
        return isinstance(other, Paper)


class Rock(Figure):
    def __init__(self):
        super().__init__('Rock')

    def __gt__(self, other):
        return isinstance(other, Lizard) or isinstance(other, Scissors)

    def __eq__(self, other):
        return isinstance(other, Rock)


class Lizard(Figure):
    def __init__(self):
        super().__init__('Lizard')

    def __gt__(self, other):
        return isinstance(other, Spock) or isinstance(other, Paper)

    def __eq__(self, other):
        return isinstance(other, Lizard)


class Spock(Figure):
    def __init__(self):
        super().__init__('Spock')

    def __gt__(self, other):
        return isinstance(other, Scissors) or isinstance(other, Rock)

    def __eq__(self, other):
        return isinstance(other, Spock)


class BaseGame:
    def __init__(self, name, figures):
        self.name = name
        self.figures = figures

    def get_figure(self, options):
        return self._get_figure(options)

    def _get_figure(self, options):
        raise NotImplementedError

    @classmethod
    def display_rules(cls):
        print(f"Game: {cls.name}")
        print("Players need to choose one of the figures:")
        for figure in cls.rules:
            print(figure.name)
        print("And try to defeat the opponent")


class RSPGame(BaseGame):
    name = 'Rock Scissors Paper Lizard Spock'
    rules = [Scissors(), Paper(), Rock(), Lizard(), Spock()]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def _get_figure(self, options):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'{self.player1.name}, enter one of {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj

    def play(self):
        print(f'{self.name} started for play')
        self._play()

    def _play(self):
        f1 = self.player1.get_figure(self.rules)
        f2 = self.player2.get_figure(self.rules)

        if f1 == f2:
            print('Draw')
        elif f1 > f2:
            print(f'Player {self.player1.name} wins with {f1}')
        else:
            print(f'Player {self.player2.name} wins with {f2}')

    def play_3_times(self):
        print(f'{self.name} started for 3 time play')
        for _ in range(3):
            self._play()


class AIPlayer:
    def __init__(self, name):
        self.name = name

    def get_figure(self, options):
        import random
        return random.choice(options)


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def get_figure(self, options):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'{self.name}, enter one of {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj


ai_player1 = AIPlayer('AI')
human_player1 = HumanPlayer('Human')

game = RSPGame(human_player1, ai_player1)

game.play()

RSPGame.display_rules()
