import random


class MontyHall:
    def __init__(self, doors=3):
        self.doors = doors
        self.reset_game()

    def reset_game(self):
        self.prize_door = random.randint(0, self.doors - 1)
        self.selected_door = None
        self.opened_door = None

    def choose_door(self, door):
        self.selected_door = door

    def open_door(self):
        available_doors = set(range(self.doors)) - {self.selected_door, self.prize_door}
        self.opened_door = random.choice(list(available_doors))

    def switch_door(self):
        self.selected_door = (
            set(range(self.doors)) - {self.selected_door, self.opened_door}
        ).pop()

    def is_winner(self):
        return self.selected_door == self.prize_door


def simulate_monty_hall(switch, num_trials=1000):
    game = MontyHall(5)
    win_count = 0

    for _ in range(num_trials):
        game.reset_game()
        game.choose_door(random.randint(0, game.doors - 1))
        game.open_door()
        if switch:
            game.switch_door()
        if game.is_winner():
            win_count += 1

    return win_count / num_trials


if __name__ == "__main__":
    num_trials = 1000000

    print(f"Number of games per method: {num_trials:,}")

    win_rate_no_switch = simulate_monty_hall(switch=False, num_trials=num_trials)
    win_rate_switch = simulate_monty_hall(switch=True, num_trials=num_trials)

    print(f"Win rate without switching: {win_rate_no_switch * 100:.2f}%")
    print(f"Win rate with switching: {win_rate_switch * 100:.2f}%")
