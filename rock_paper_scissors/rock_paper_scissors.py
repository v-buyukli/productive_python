class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ''

    def choose(self):
        self.choice = input(f' \n{self.name}, select rock, scissors or paper: ')
        print(f'{self.name} selects {self.choice}')

    def to_numerical_choice(self):
        switcher = {'rock': 0, 'paper': 1, 'scissors': 2}
        return switcher[self.choice]

    def increment_point(self):
        self.points += 1
        print(f'\nRound resulted in a win for {self.name}')


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

        p1.choose()
        p2.choose()
        result = self.compare_choices(p1, p2)
        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()
        else:
            print('\nRound resulted in a draw')

    def compare_choices(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]


class Game:
    def __init__(self):
        self.end_game = False
        self.p1 = Participant('Player1')
        self.p2 = Participant('Player2')
        Game.start(self)

    def start(self):
        while not self.end_game:
            GameRound(self.p1, self.p2)
            self.check_end_condition()

    def check_end_condition(self):
        answer = input('\nContinue game y/n: ')
        if answer == 'y':
            GameRound(self.p1, self.p2)
            self.check_end_condition()
        else:
            print(
                '\nGame ended, {p1name} {p1points}:{p2points} {p2name}'.format(
                    p1name=self.p1.name, p1points=self.p1.points, p2name=self.p2.name, p2points=self.p2.points
                )
            )
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        if self.p1.points > self.p2.points:
            result_string = f'Winner is {self.p1.name}'
        elif self.p1.points < self.p2.points:
            result_string = f'Winner is {self.p2.name}'
        else:
            result_string = "It's a draw"
        print(result_string)
