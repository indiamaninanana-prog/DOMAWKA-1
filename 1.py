class Computer:
    def __init__(self, processor):
        self.processor = processor

    def calc(self):
        print(f"Розрахунок виконується на процесорі {self.processor}")


class Display:
    def __init__(self, resolution):
        self.resolution = resolution

    def display(self):
        print(f"Виведення інформації на екран з роздільною здатністю {self.resolution}")


class SmartComputer(Computer, Display):
    def __init__(self, processor, resolution):
        Computer.__init__(self, processor)
        Display.__init__(self, resolution)


pc = SmartComputer("Intel Core i7", "1920x1080")
pc.calc()
pc.display()