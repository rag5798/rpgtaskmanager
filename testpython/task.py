import random

class Task:
    __isdone = False

    def __init__(self, title: str, difficulty: int, requirements: list[str], description: str):
        self.__title = title
        self.__difficulty = difficulty
        self.__requirements = requirements
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value: int):
        self.__difficulty = value

    @property
    def isdone(self) -> bool:
        return self.__isdone

    @isdone.setter
    def isdone(self, value: bool):
        self.__isdone = value

    @property
    def requirements(self) -> list[str]:
        return self.__requirements

    @requirements.setter
    def requirements(self, value: list[str]):
        self.__requirements = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    def OnStart(title, repeat = bool, time = bool):
        pass

    def Die_Roll(die: str, quantity: int):
        die_map = {
            "d4": 4,
            "d6": 6,
            "d8": 8,
            "d10": 10,
            "d12": 12,
            "d20": 20,
            "d100": 100
        }
        
        die = die.lower()
        if die in die_map:
            max_value = die_map[die]
            return [random.randint(1, max_value) for _ in range(quantity)]
        else:
            print("Invalid die name. Please try again.")
            return []

    def Get_Task_Description(self):
        print(self.title)
        print(f"Task Description: {self.description}")
        print(f"Task Requirements: ")
        for i in self.requirements:
            print(f"    {i}")

        if self.__isdone:
            print("Task completed.\n")
        else:
            print("Task not done.\n")

    def Complete(self) -> bool:
        """Used to mark a task as complete."""
        self.__isdone = True

