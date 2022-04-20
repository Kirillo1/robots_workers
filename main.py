from random import shuffle, randint


class MarginOfSafetyException(Exception):
    pass


class SlotsCountException(Exception):
    pass


class WeightException(Exception):
    pass


class Tool:
    def __init__(self, name, weight, margin_of_safety=100) -> None:
        self.name = name
        self.weight = weight
        self.margin_of_safety = margin_of_safety

    def action(self):
        if self.margin_of_safety < 0:
            self.margin_of_safety = 0
        self.display()
        self.__is_still_work()
        self.margin_of_safety -= 10

    def __is_still_work(self):
        if self.margin_of_safety == 0:
            raise MarginOfSafetyException(f"Инструмент {self.name} изношен")

    def display(self):
        print(f"Название: {self.name}...прочность: {self.margin_of_safety}...вес: {self.weight}")


class Saw(Tool):
    def action(self):
        print("взззззвзззз")
        super().action()


class Drill(Tool):
    def action(self):
        print("дрдрддррр")
        super().action()


class Hammer(Tool):
    def action(self):
        print("бам-бам")
        super().action()


class Robot:
    def __init__(self, name, tools_slots_count) -> None:
        self.name = name
        self.tools_slots = []
        self.tools_slots_count = tools_slots_count
        self.weight_limit = randint(1, 30)
        print(f"Имя робота: {self.name} - слотов: {self.tools_slots_count}")

    def setup_tool(self, tool):
        if self.weight_limit - tool.weight < 0:
            raise WeightException(f"Превышен лимит по весу")
        if self.tools_slots_count:
            self.tools_slots.append(tool)
            self.tools_slots_count -= 1
            self.weight_limit -= tool.weight
        else:
            raise SlotsCountException("Слоты заклнчились")

    def drop_tool(self, tool):
        if tool:
            self.tools_slots.remove(tool)
        else:
            print("Нет такого инструмента")

    def action(self):
        if not self.tools_slots:
            print("Нечем работать")
        else:
            for tool in self.tools_slots:
                try:
                    tool.action()
                except MarginOfSafetyException as e:
                    print(e)
                    self.drop_tool(tool)


saw = Saw("pila", randint(3, 10), randint(80, 120))
drill = Drill("drel", randint(3, 1010), randint(80, 120))
hammer = Hammer("Molotok", randint(3, 10), randint(80, 120))
saw2 = Saw("pila2", randint(3, 10), randint(80, 120))
drill2 = Drill("drel2", randint(3, 10), randint(80, 120))
hammer2 = Hammer("Molotok2", randint(3, 10), randint(80, 120))

robot = Robot("Vasya", randint(1, 4))

tools = [saw, drill, hammer, saw2, drill2, hammer2]
shuffle(tools)

while robot.tools_slots_count or tools:
    tool = tools.pop(randint(0, len(tools) - 1))
    try:
        robot.setup_tool(tool)
    except SlotsCountException as e:
        print(e)
        break
    except WeightException as e:
        print(e)
        break

while robot.tools_slots:
    robot.action()
