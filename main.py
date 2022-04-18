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


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.tool = None

    def setup_tool(self, tool):
        if self.tool:
            print(f"Уже установлен интрумент: {self.name}")
        else:
            self.tool = tool

    def drop_tool(self):
        if not self.tool:
            print("Не один инструмент не установлен")
        else:
            tool = self.tool
            self.tool = None
            return tool

    def action(self):
        if not self.tool:
            print("Нечем работать")
        else:
            self.tool.action()
