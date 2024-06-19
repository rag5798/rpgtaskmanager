from task import Task

class RepeatedTask(Task):
        # Buff types, int indicates each instance/stack of the buff
        # __heal_buff = int
        # __ac_buff = int
        # __advantage = int
        # __magic_buff = int
        # __auto_crit = int
        __completions = int

        def __init__(self, difficulty: int, requirements: list[str], description: str, frequency: list[int], buff: int):
            super().__init__(difficulty, requirements, description)
            self.__frequency = frequency
            self.__buff = buff
                # 1 = Heal over time
                # 2 = AC buff
                # 3 = Advantage buff
                # 4 = Magic Attack Buff
                # 5 = Auto Crit Buff

        @property
        def frequency(self) -> list[int]:
            return self.__frequency
        
        @frequency.setter
        def frequency(self, value:list[int]):
            self.__frequency = value

        @property
        def buff(self) -> int:
            return self.__buff
        
        @buff.setter
        def buff(self, value: int):
            self.buff = value

        def Set_Buff(buff) -> None:
            """Creates a modifier to add to an attack roll
            to make it more likely to overcome an enemy's AC."""
            buff += 1

        def Complete_Instance(self) -> None:
            """Used to add an instance of a completed repeated task, also adds an instance/stack to the buff."""
            self.__completions += 1

        def Get_Buff_Name(self) -> str:
            """Returns name of Buff based on difficulty."""
            if self.__buff == 1:
                return "Heal over time."
            elif self.__buff == 2:
                return "Armor Class buff."
            elif self.__buff == 3:
                return "Advantage Buff."
            elif self.__buff == 4:
                return "Magic Attack Buff."
            elif self.__buff == 5:
                return "Auto Crit Buff."
            
        def Set_Frequency(self) -> list[int]:
            """Sets the frequency of the task to be completed."""
            escape = False
            days = []

            # Loop to input weekdays
            while not escape:
                day = str(input("Enter a weekday in order (or 'stop' to finish): "))
                if day.lower() == "monday" and "Monday" not in days:
                    days.append("Monday")
                elif day.lower() == "tuesday" and "Tuesday" not in days:
                    days.append("Tuesday")
                elif day.lower() == "wednesday" and "Wednesday" not in days:
                    days.append("Wednesday")
                elif day.lower() == "thursday" and "Thursday" not in days:
                    days.append("Thursday")
                elif day.lower() == "friday" and "Friday" not in days:
                    days.append("Friday")
                elif day.lower() == "saturday" and "Saturday" not in days:
                    days.append("Saturday")
                elif day.lower() == "sunday" and "Sunday" not in days:
                    days.append("Sunday")
                elif day.lower() == "stop":
                    escape = True
                else:
                    print("Invalid input or day already entered. Please enter a valid weekday or type 'stop' to end.")