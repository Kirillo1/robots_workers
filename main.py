from random import shuffle, randint


class MarginOfSafetyException(Exception):
    pass


class SlotsCountException(Exception):
    pass


class Tool:
    def __init__(self, name, margin_of_safety=100) -> None:
        self.name = name
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
        print(f"Название: {self.name}...прочность: {self.margin_of_safety}")


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
        print(f"Имя робота: {self.name} - слотов: {self.tools_slots_count}")

    def setup_tool(self, tool):
        if self.tools_slots_count:
            self.tools_slots.append(tool)
            self.tools_slots_count -= 1
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


saw = Saw("pila")
drill = Drill("drel")
hammer = Hammer("Molotok")
saw2 = Saw("pila2")
drill2 = Drill("drel2")
hammer2 = Hammer("Molotok2")


robot = Robot("Vasya", randint(1,4))

tools = [saw, drill, hammer, saw2, drill2, hammer2]
shuffle(tools)

for tool in tools:
    try:
        robot.setup_tool(tool)
    except SlotsCountException as e:
        print(e)
        break

while robot.tools_slots:
    robot.action()



# for tool in tools:
#     robot.setup_tool(tool)
#     for _ in range(11):
#         try:
#             robot.action()
#         except MarginOfSafetyException as e:
#             print(e)
#             robot.drop_tool()
#             break
#     robot.drop_tool()
