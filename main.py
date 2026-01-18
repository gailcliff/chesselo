import random

class Player:
    id: str
    rating: int

win = 1
draw = 0.5
loss = 0

ratings: dict[str, int] = {}


def play_game(player1: Player, player2: Player) -> int:

    return random.choice([win, draw, loss])

def update_elo_scores(player1: Player, player2: Player, result: int) -> None:
    pass

if __name__ == '__main__':
    pass