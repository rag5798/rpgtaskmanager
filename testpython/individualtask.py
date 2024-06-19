from task import Task
import random

class IndividualTask(Task):
    __hit = int
    __damage = int
    

    def __init__(self, title: str, difficulty: int, requirements: list[str], description: str):
        super().__init__(title, difficulty, requirements, description)
        #TODO fill out the rest?

    @property
    def hit(self) -> int:
        return self.__hit
    
    @hit.setter
    def hit(self, value: int):
        self.__hit = value

    @property
    def damage(self) -> int:
        return self.__damage
    
    @damage.setter
    def damage(self, value:int):
        self.__damage = value

    def Attack_Roll(advantage: bool) -> int:
        """As per DnD 5E rules, returns the result of an attack roll.
        If advantage is True, the higher of two d20 rolls is returned.
        If advantage is False, a single d20 roll is returned."""
        if advantage:
            rolls = Task.Die_Roll("d20", 2)
            return max(rolls)
        else:
            return Task.Die_Roll("d20", 1)[0]

    def Damage_Roll(die: str, quantity: str) -> int:
        """As per DnD 5E rules, returns an int for the
        amount of damage dealt in an attack."""
        damage_list = Task.Die_Roll(die, quantity)
        return sum(damage_list)

    def Combat(self, advantage: bool, die: str, quantity: int):
        """Sets __hit and __damage"""
        self.__hit = IndividualTask.Attack_Roll(advantage)
        self.__damage = IndividualTask.Damage_Roll(die, quantity)
        
    def Get_Combat_Results(self) -> str:
        return (f"Roll to hit: {self.__hit}, Roll for damage: {self.__damage}")

        


    