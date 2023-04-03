class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.saved_high_score = self._read_high_score()
        self.high_score = self.saved_high_score

    def _read_high_score(self):
        try:
            with open("util/high_score.txt", "r") as f:
                contents = f.read()

                if not contents:
                    return 0

                return int(contents)
        except FileNotFoundError:
            print('There is no file "high_score.txt"')
            return 0

    def _write_high_score(self):
        try:
            with open("util/high_score.txt", "w") as f:
                self.high_score = round(self.high_score, -1)
                f.write(str(self.high_score))
        except FileNotFoundError:
            print('There is no file "high_score.txt"')

    def update_high_score(self):
        if self.saved_high_score < self.high_score:
            self._write_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
