class Tool:
    def __init__(self, name, margin_of_safety=100) -> None:
        self.name = name
        self.margin_of_safety = margin_of_safety

    def action(self):
        self.margin_of_safety -= 10


class Saw(Tool):
    def action(self):
        super().action()
        print("взззззвзззз")


class Drill(Tool):
    def action(self):
        super().action()
        print("дрдрддррр")


class Hammer(Tool):
    def action(self):
        super().action()
        print("бам-бам")
