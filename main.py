from random import shuffle, randint


class MarginOfSafetyException(Exception):
    pass


class SlotsCountException(Exception):
    pass


class WeightException(Exception):
    pass


class RobotPowerException(Exception):
    pass


class Tool:
    def __init__(self, name, weight, margin_of_safety=100) -> None:
        self.name = name
        self.weight = weight
        self.margin_of_safety = margin_of_safety
        self.standart_break_amount = 10

    def get_break_amount(self, accuracy):
        return self.standart_break_amount - (self.standart_break_amount / 100) * accuracy

    def action(self, accuracy):
        if self.margin_of_safety < 0:
            self.margin_of_safety = 0
        self.display()
        self.__is_still_work()
        self.margin_of_safety -= self.get_break_amount(accuracy)

    def __is_still_work(self):
        if self.margin_of_safety == 0:
            raise MarginOfSafetyException(f"Инструмент {self.name} изношен")

    def display(self):
        print(f"Название: {self.name}...прочность: {self.margin_of_safety}...вес: {self.weight}")


class Saw(Tool):
    def action(self, accuracy):
        print("взззззвзззз")
        super().action(accuracy)


class Drill(Tool):
    def action(self, accuracy):
        if randint(1, 5) == 2:
            print(f"{self.name} замкнула.")
            self.margin_of_safety = 0
        else:
            print("дрдрддррр")
        super().action(accuracy)


class Hammer(Tool):
    def action(self, accuracy):
        print("бам-бам")
        super().action(accuracy)


class Robot:
    def __init__(self, name, tools_slots_count, power) -> None:
        self.name = name
        self.tools_slots = []
        self.tools_slots_count = tools_slots_count
        self.weight_limit = randint(10, 30)
        self.power = power
        print(f"Имя робота: {self.name} - слотов: {self.tools_slots_count} - лимит по весу: {self.weight_limit}")

    def setup_tool(self, tool):
        if self.weight_limit - tool.weight < 0:
            raise WeightException(f"Превышен лимит по весу")
        if self.tools_slots_count:
            self.tools_slots.append(tool)
            self.tools_slots_count -= 1
            self.weight_limit -= tool.weight
        else:
            raise SlotsCountException("Слоты закончились")

    def drop_tool(self, tool):
        if tool:
            self.tools_slots.remove(tool)
        else:
            print("Нет такого инструмента")

    def action(self):
        if not self.power:
            raise RobotPowerException("У робота сели батарейки")
        if not self.tools_slots:
            print("Нечем работать")
        else:
            for tool in self.tools_slots:
                try:
                    tool.action(self.power // 10)
                    self.power -= 20
                except MarginOfSafetyException as e:
                    print(e)
                    self.drop_tool(tool)


saw = Saw("pila", randint(3, 10), randint(80, 120))
drill = Drill("drel", randint(3, 10), randint(80, 120))
hammer = Hammer("Molotok", randint(3, 10), randint(80, 120))
saw2 = Saw("pila2", randint(3, 10), randint(80, 120))
drill2 = Drill("drel2", randint(3, 10), randint(80, 120))
hammer2 = Hammer("Molotok2", randint(3, 10), randint(80, 120))

robot = Robot("Vasya", randint(1, 4), 500)

tools = [saw, drill, hammer, saw2, drill2, hammer2]
shuffle(tools)

while robot.tools_slots_count and tools:
    tool = tools.pop(randint(0, len(tools) - 1))
    try:
        robot.setup_tool(tool)
    except SlotsCountException as e:
        print(e)
        break
    except WeightException as e:
        print(e)

while robot.tools_slots:
    try:
        robot.action()
    except RobotPowerException as e:
        print(e)
        break
