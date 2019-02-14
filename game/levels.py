from game.entities.platform import Platform

MAXLEVEL = 1


class Levels:
    def __init__(self, screen, step):
        self.screen = screen
        self.step = step

    def load_level(self, level_number):
        if 0 < level_number <= MAXLEVEL:
            if level_number == 1:
                level = self.load_first_level()
            else:
                return None
            x = y = 0
            platforms = []
            for row in level:
                for col in row:
                    if col == "P":
                        platforms.append(Platform(self.screen, (x, y), self.step))
                    x += self.step
                y += self.step
                x = 0
            return platforms
        else:
            return None

    @staticmethod
    def load_first_level():
        level = [
            "",
            "",
            "",
            "",
            "",
            "PPPPPPP",
            "",
            "",
            "           P",
            "PPPPPPPPPP   PPPPPPPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
        ]
        return level
