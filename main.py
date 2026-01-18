import random
from dataclasses import dataclass

@dataclass
class Player:
    id: str
    rating: int
    delta: int = 0

    def __str__(self):
        delta_str = f"({'+' if self.delta >= 0 else ''}{self.delta})"
        return f"{self.id} ELO: {self.rating} {delta_str}"

win = 1
draw = 0.5
loss = 0
K = 32

ratings: dict[str, int] = {}

def get_player_expectations(challenger: Player, defender: Player) -> tuple[float, float]:
    expectation_challenger = 1 / (1 + 10**((defender.rating - challenger.rating) / 400))
    expectation_defender = 1 - expectation_challenger

    return (expectation_challenger, expectation_defender)


def update_elo_scores(challenger: Player, defender: Player, challenger_new_rating: int, defender_new_rating: int) -> None:
    ratings[challenger.id] = challenger_new_rating
    ratings[defender.id] = defender_new_rating
    challenger.delta = challenger_new_rating - challenger.rating
    defender.delta = defender_new_rating - defender.rating

    challenger.rating = challenger_new_rating
    defender.rating = defender_new_rating


def play_game(challenger: Player, defender: Player) -> int:

    expectation_challenger, expectation_defender = get_player_expectations(challenger, defender)

    game_result = random.choice([win, draw, loss])

    challenger_new_rating = round(challenger.rating + K * (game_result - expectation_challenger))
    defender_new_rating = round(defender.rating + K * ((1 - game_result) - expectation_defender))

    update_elo_scores(challenger, defender, challenger_new_rating, defender_new_rating)

    return game_result


def create_player(username: str, rating=1200) -> Player:
    ratings[username] = rating

    return Player(username, rating, 0)


def get_rating(player: Player):
    return ratings[player.id]


if __name__ == '__main__':
    playerA = create_player("hikaru", 2810)
    playerB = create_player("magnus", 2840)

    for i in range(20):
        print(f"Game {i+1}: {playerA} vs. {playerB}")
        game_result = play_game(playerA, playerB)
        print(f"Game result: {playerA.id}: {['loss', 'draw', 'wins'][int(game_result * 2)]}")

        print(playerA)
        print(playerB)
        # print(f"{playerB.id} new ELO: {get_rating(playerB)}")
        print()
        print()