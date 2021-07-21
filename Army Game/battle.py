# Author: Yong Zi Ying 
""" 
In Task 5, it is just additional of Task 4 only.
The queue formation which is represented by 1 is included.
There are some extra method are used to prevent copy pasting of code.
"""
from referential_array import ArrayR
from army import Soldier, Archer, Cavalry, Army

class Battle(Army):
    """ 
    This class is allow two players to battle. Before battle both of the player need to choose army.
    After choosing army, the battle start. The result of the battle is either
    draw, player 1 win or player 2 win.
    """

    DRAW = 0
    PLAYER_ONE_WIN = 1
    PLAYER_TWO_WIN = 2

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """ Reads and creates an army for each player, sets those armies in 
        stack formation. Winner will be returned.
        :Complexity: O(comp!=), same explaination as __setup_army(player_one, player_two, formation)     
        """
        return self.__setup_army(player_one,player_two,0)    # O(comp!=)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """ Reads and creates an army for each player, sets those armies in 
        queue formation. Winner will be returned.
        :Complexity: O(comp!=), same explaination as __setup_army(player_one, player_two, formation)  
        """
        return self.__setup_army(player_one,player_two,1)    # O(comp!=)

    def __setup_army(self, player_one: str, player_two: str, formation: int) -> int:
        """ Reads and creates an army for each player, sets those armies in 
        either stack or queue formation. Winner will be returned.
        An additional method to prevent copy pasting the same code.
        :Complexity: O(comp!=), the Big O is depending on the user inputs.
                     If user input correctly in the first time then the Big O is
                     depending on __conduct_combat(army1, army2, formation) which is O(min(army1.force, army2.force)).
                     If user always input wrongly then it is depending on the number of times
                     that user input incorrectly.
                     Thus, it's fully depending on the comparison of !=.
        """
        # reads and creates an army for each player 
        army1 = Army()      # intiatiate Army class
        army1.choose_army(player_one, formation)    # O(comp!=)
        army2 = Army()      # intiatiate Army class
        army2.choose_army(player_two, formation)    # O(comp!=)
        
        # return battle result
        res = self.__conduct_combat(army1, army2, formation)    # O(min(army1.force, army2.force))
        return res

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """ Conducts combat based on the formation of the two armies passed.
        The result of the combat will return.  
        0 = draw
        1 = player_one win
        2 = player_two win
        :complexity: O(min(army1.force, army2.force)), it's based on the minimum length 
                     of either army1.force or army2.force. If either 1 of the length is is_empty
                     then the loop will exit. The other part of the code are constant, O(1).
                     Thus, the Big O is depending on the 
                     minimum length of either army1.force or army2.force.
        """  
        while not army1.force.is_empty() and not army2.force.is_empty():
            f1_alivee  = False
            f2_alivee = False
        #==================================================================
            # pop or serve fighter #
            if formation == 0:  # stack
                # pop a unit from each army
                fighter1 = army1.force.pop()
                # pop a unit from each army
                fighter2 = army2.force.pop()
            elif formation == 1:    # queue
                # serve a unit from each army
                fighter1 = army1.force.serve()
                # serve a unit from each army
                fighter2 = army2.force.serve()
        #==================================================================
            # Attack and defend #    
            # GLADIATORIAL STYLE COMBAT or FAIRER STYLE COMBAT #
            # fighter1 ATTACK; fighter2 DEFEND
            if fighter1.get_speed() > fighter2.get_speed():
                damage1 = fighter1.get_attack_damage()  # fighter1 ATTACK
                fighter2.defend(damage1)        # fighter2 DEFEND
                # if fighter2 still alive after DEFENDING fighter1 ATTACK in ROUND 1
                if fighter2.get_life() > 0:
                    damagee2 = fighter2.get_attack_damage() # fighter2 ATTACK
                    fighter1.defend(damagee2)  # fighter1 DEFEND

            # fighter2 ATTACK; fighter1 DEFEND
            elif fighter2.get_speed() > fighter1.get_speed():
                damage2 = fighter2.get_attack_damage()  # fighter2 ATTACK
                fighter1.defend(damage2)        # fighter1 DEFEND
                # if fighter1 still alive after DEFENDING fighter2 ATTACK in ROUND 1
                if fighter1.get_life() > 0:
                    damagee1 = fighter1.get_attack_damage()  # fighter1 ATTACK
                    fighter2.defend(damagee1)        # fighter2 DEFEND
                            
            # fighter1 ATTACK; fighter2 ATTACK then fighter1 DEFEND; fighter2 DEFEND
            elif fighter1.get_speed() == fighter2.get_speed():
                # regardless of whether one would die in combat
                damageee1 = fighter1.get_attack_damage()   # fighter1 ATTACK
                damageee2 = fighter2.get_attack_damage()   # fighter2 ATTACK  
                fighter1.defend(damageee2)        # fighter1 DEFEND
                fighter2.defend(damageee1)        # fighter2 DEFEND

        #================================================================== 
            # ENDING combat #
            # if fighter1 and fighetr2 both are still alive after damage and defend 
            if fighter1.get_life() > 0 and fighter2.get_life() > 0:
                # both lost one life
                fighter1.lose_life(1)   
                fighter2.lose_life(1)
                f1_alivee = True  
                f2_alivee = True

            # if fighter1 still ALIVE after damage and defend but fighter2 is not alive
            elif fighter1.get_life() > 0 and fighter2.get_life() == 0:
                fighter1.gain_experience(1)     # remains fighter gain 1 Exp
                f1_alivee = True       

            # if fighter2 still alive after damage and defend but fighter1 is not alive
            elif fighter2.get_life() > 0 and fighter1.get_life() == 0:
                fighter2.gain_experience(1)     # remain fighter gain 1 Exp
                f2_alivee = True   

            # Any unit still alive is pushed or appended back into the stack or queue. #
            if formation == 0:
                if f1_alivee and f2_alivee:
                    # pushed back into stack
                    army1.force.push(fighter1)
                    army2.force.push(fighter2)
                elif f1_alivee:
                    army1.force.push(fighter1)      # alives fighter is pushed back into force
                elif f2_alivee:
                    army2.force.push(fighter2)      # alives fighter is pushed back into force
                
            elif formation == 1:
                if f1_alivee and f2_alivee:
                    # appended back into queue
                    army1.force.append(fighter1)
                    army2.force.append(fighter2)
                elif f1_alivee:
                    army1.force.append(fighter1)      # alives fighter is appended back into force
                elif f2_alivee:
                    army2.force.append(fighter2)      # alives fighter is appended back into force

        #==================================================================
        # WINNER # 
        # ENDING game #
        # battle result 
        if army1.force.is_empty() and army2.force.is_empty():
            # draw
            return self.DRAW
        elif not army1.force.is_empty() and army2.force.is_empty():
            # Army 1 Win
            return self.PLAYER_ONE_WIN
        elif not army2.force.is_empty() and army1.force.is_empty():
            # Army 2 Win
            return self.PLAYER_TWO_WIN
        
# TESTING Manual inputs 
if __name__ == '__main__':
    battle = Battle()
    battle.fairer_combat("Yong","Wong")
