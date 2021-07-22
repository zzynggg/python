# Author: Yong Zi Ying
# Grade: 84/90 HD
"""
This is the combination of Task 1, Task2 and Task 3.
Figher class from Task 1, Soldier class, Archer class, Cavalry class from Task 2 and
Army class from Task 3 are used in Task 4.
For Task 5, there's some minor changes in Army class, def __assign_army(self, name:str, sold: int, arch: int, cav: int, formation: int)-> None:
method. The queue formation which is represented by 1 is included in this Task.
"""

from abc import ABC, abstractmethod
from stack_adt import Stack, ArrayStack
from queue_adt import Queue, CircularQueue

class Fighter(ABC):
    """
    Fighter is an abstract class. It contains some abstract and non-abstract methods.
    The abstract method need to be implemented by the children class. 
    """
    def __init__(self, life: int, experience: int) -> None:
        """ Initialising the variables such as life and experience.
        :complexity: O(1)
        :pre: life >= 0 
        :pre: experience >=0
        """
        if life < 0:
            raise ValueError ("life must be larger than equal to 0")
        if experience < 0:
            raise ValueError ("experience must be larger than equal to 0")
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        """ Return True if the fighter is alive else False.
        :complexity: O(1)
        """
        if self.life > 0:
            return True
        else:
            return False

    def lose_life(self, lost_life: int) -> None:
        """ Subtrating the life of the unit by the amout indicated by lost_life(normally is 1). 
        :complexity: O(1)
        :pre: lost_life >= 0
        """
        if lost_life < 0:
            raise ValueError ("lost_life must be larger than equal to 0")
        self.life -= lost_life
        
    def get_life(self) -> int:
        """ Return the fighter's life.
        :complexity: O(1)
        """
        return self.life

    def gain_experience(self, gained_experience: int) -> None:
        """ Increase the experience of the unit by the amount indicated by gained_experience(normally is 1).
        :complexity: O(1)
        :pre: gain_experience >= 0
        """
        if gained_experience < 0:
            raise ValueError ("gain_experience must be larger than equal to 0")
        self.experience += gained_experience

    def get_experience(self) -> int:
        """ Return the experience of the unit.
        :complexity: O(1)
        """
        return self.experience

    @abstractmethod
    def get_speed(self) -> int:
        """ Return the speed of the unit.
        """
        pass

    @abstractmethod
    def get_cost(self) -> int:
        """ Return the cost of the unit.
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """ Return the amount of damage performed by the unit when it attacks.
        """
        pass
    
    @abstractmethod
    def defend(self, damage: int) -> None:
        """ Evaluate the life lost after defence expression and changes life accordingly.
        :pre: damage >= 0
        """
        damage = self.get_attack_damage()
        if damage < 0:
            raise ValueError ("damage must be larger than equal to 0")
        pass

    @abstractmethod
    def get_unit_type(self) -> str:
        """ Return the unit's type.
        """
        pass

    def __str__(self) -> str:
        """ Return the string indicating the type of unit, its current life and experience.
        """
        res = self.get_unit_type() + "'s life = " + str(self.get_life()) + " and experience = " + str(self.get_experience())
        return res
       
        
# ~~~ Soldier ~~~ #
class Soldier(Fighter):
    """
    Soldier is a children class of Fighter class. It contains the detail of Soldier.
    """  
    COST = 1
    UNIT = "Soldier"

    def __init__(self) -> None:
        """ Initialising the variables such as life and experience.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
        """ Return the speed of the unit.
        :complexity: O(1)
        """
        spd = 1 + self.experience
        return spd

    def get_cost(self) -> int:
        """ Return the cost of the unit.
        :complexity: O(1)
        """
        return self.COST

    def get_attack_damage(self) -> int:
        """ Return the amount of damage performed by the unit when it attacks.
        :complexity: O(1)
        """
        damaged = 1 + self.experience
        return damaged
    
    def defend(self, damage: int) -> None:
        """ Evaluate the life lost after defence expression and changes life accordingly.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        if damage > self.experience:
            self.lose_life(1)
        
    def get_unit_type(self) -> str:
        """ Return the unit's type.
        :complexity: O(1)
        """
        return self.UNIT


# ~~~ Archer ~~~ #
class Archer(Fighter):
    """
    Archer is a children class of Fighter class. It contains the detail of Archer.
    """ 
    COST = 2
    SPEED = 3
    UNIT = "Archer"
    
    def __init__(self) -> None:
        """ Initialising the variables such as life and experience.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
        """ Return the speed of the unit.
        :complexity: O(1)
        """
        return self.SPEED

    def get_cost(self) -> int:
        """ Return the cost of the unit.
        :complexity: O(1)
        """
        return self.COST
    
    def get_attack_damage(self) -> int:
        """ Return the amount of damage performed by the unit when it attacks.
        :complexity: O(1)
        """
        damaged = 1 + self.experience
        return damaged

    def defend(self, damage: int) -> None:
        """ Evaluate the life lost after defence expression and changes life accordingly.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        self.lose_life(1)    

    def get_unit_type(self) -> str:
        """ Return the unit's type.
        :complexity: O(1)
        """
        return self.UNIT

# ~~~ Cavalry ~~~ #
class Cavalry(Fighter):
    """
    Cavalry is a children class of Fighter class. It contains the detail of Cavalry.
    """ 
    COST = 3
    SPEED = 2
    UNIT = "Cavalry"

    def __init__(self) -> None:
        """ Initialising the variables such as life and experience.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        Fighter.__init__(self, 4, 0)

    def get_speed(self) -> int:
        """ Return the speed of the unit.
        :complexity: O(1)
        """
        return self.SPEED

    def get_cost(self) -> int:
        """ Return the cost of the unit.
        :complexity: O(1)
        """
        return self.COST
    
    def get_attack_damage(self) -> int:
        """ Return the amount of damage performed by the unit when it attacks.
        :complexity: O(1)
        """
        damaged = (2*self.experience) + 1
        return damaged

    def defend(self, damage: int) -> None:
        """ Evaluate the life lost after defence expression and changes life accordingly.
        The pre-consition are checked in Fighter class(parent class)
        :complexity: O(1)
        """
        if damage > (self.experience/2):
            self.lose_life(1)    

    def get_unit_type(self) -> str:
        """ Return the unit's type.
        :complexity: O(1)
        """
        return self.UNIT


# ~~~ Army ~~~ #
class Army:
    """
    Army is a non abstact class and it does not inherite any parent class. 
    It is used to assign army for player according to the number of fighter and formation that player input.
    """ 
    MIN_CAPACITY = 1
    BUDGET = 30

    def __init__(self) -> None:
        """ Initialising the variables name and force to None.
        :complexity: O(1) 
        """
        self.name = None
        self.force = None
        
    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int)-> bool:
        """ Returns True if the total costs of the units provided are less than or equal to the allocated budget, else False.
        :complexity: O(1)
        """
        total_army_cost = soldiers + archers*2 + cavalry*3
        if total_army_cost <= self.BUDGET:
            return True
        else:
            return False

    def __assign_army(self, name:str, sold: int, arch: int, cav: int, formation: int)-> None:
        """ The army is assigned in the formation of stack form. An ADT is created.
        The name and force variabels is binded appropriately.
        :complexity: O(max(sold, arch, cav)), the Big O is depending on the maximum number
                     of fighter because the fighter need to be pushed one by one into 
                     the stack. It's either sold, arch or cav will have the biggest number. 
                     Thus, the biggest number of fighter will take more times to exit the loop.  
        """
        self.name = name
        total_armies = sold + arch + cav
        if formation == 0:
            self.force = ArrayStack(max(self.MIN_CAPACITY, total_armies))
            while cav != 0:
                self.force.push(Cavalry())
                cav -= 1
                total_armies -= 1
            
            while arch != 0:
                self.force.push(Archer())
                arch -= 1
                total_armies -= 1
            
            while sold != 0:
                self.force.push(Soldier())
                sold -= 1
                total_armies -= 1

        elif formation == 1:
            self.force = CircularQueue(max(self.MIN_CAPACITY, total_armies))
            while sold != 0:
                self.force.append(Soldier())
                sold -= 1
                total_armies -= 1

            while arch != 0:
                self.force.append(Archer())
                arch -= 1
                total_armies -= 1

            while cav != 0:
                self.force.append(Cavalry())
                cav -= 1
                total_armies -= 1

    def choose_army(self, name: str, formation: int) -> None:
        """ Reads in 3 integers soldiers, archers, cavalry by calling __correct_army_given(s, a, c) and 
        __assign_army(name, s, a, c, formation).
        :complexity: Best case is O(max(s, a, c))
                     If user input correctly in the first time,it will not entering the loop. 
                     Therefore, the Big O is depending on __assign_army(name, s, a, c, formation) which is O(max(s, a, c)).
                     
                     Worst case is O(comp!=), 
                     If user always input wrongly then it is depending on the number of times that user input incorrectly.
                     If the number of invalid input is bigger than the max(s,a,c) then the Big O is O(comp!=).
                     If the number of invalid input is smaller than the max(s,a,c) then the Big O is O(max(s, a, c)).
                     Thus, it's fully depending on user input.
        """
        res = ""
        s = int(input("Please input valid number of soldiers: "))
        a = int(input("Please input valid number of archers: "))
        c = int(input("Please input valid number of cavalry: "))
        option = self.__correct_army_given(s, a, c)     # O(1)
        while option != True:       # O(comp!=)
            s = int(input("Please input valid number of soldiers: "))
            a = int(input("Please input valid number of archers: "))
            c = int(input("Please input valid number of cavalry: "))
            option = self.__correct_army_given(s, a, c) # O(1)

        self.__assign_army(name, s, a, c, formation)       # O(max(s, a, c))
        res += "Player " + name + " choose your army as " + str(s) + " " + str(a) + " " + str(c) + "\n"
        res += "where " + str(s) + " is the number of soldiers \n" 
        res += str(a) + " is the number of archers \n" 
        res += str(c) + " is the number of cavalry \n"
        print(res)

    def __str__(self) -> str:
        """ Returns a string containing the information of each army element in force.
        :complexity: O(1)
        """
        return str(self.force)  # call the ArrayStack's __str__





