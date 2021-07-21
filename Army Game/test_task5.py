"""
Testing file for Question 5 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask5(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__conduct_combat(self):
        t1 = Army()
        t2 = Army()
        battle = Battle()
        formation = 1

        # Test if combat is conducted correctly and if it returns
        # appropriate result for all Archer p1 army and empty p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 10, 0, formation)
        t2._Army__assign_army("", 0, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Fairer 0,10,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Tests combat is conducted correctly and if it
        # returns appropriate result for 1 Soldier p1 army and 1 Archer p2 army
        # Assumes __assign_army is working correctly 
        t1._Army__assign_army("", 1, 0, 0, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Fairer 1,0,0 0,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force), "", msg="Army 1 wrong for Fairer 1,0,0 0,1,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "Archer's life = 1 and experience = 1", msg="Army 2 wrong for Fairer 1,0,0 0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

# =============================================================================================================================
        # your first tests for __conduct_combat go here #
        
        # PLAYER 2 WIN #
        # Test if combat is conducted correctly and if it returns
        # appropriate result for empty p1 army and all p2 army
        # Assumes __assign_army is working correctly
        # manual inputs 
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 10, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Fairer 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        
        # PLAYER 1 WIN #
        # Tests combat is conducted correctly and if it
        # returns appropriate result for 1 Archer p1 army and 1 Soldier p2 army
        # Assumes __assign_army is working correctly
        # manual inputs 
        t1._Army__assign_army("", 0, 1, 0, formation)
        t2._Army__assign_army("", 1, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Fairer 0,1,0 1,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 0,1,0 1,0,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force), "Archer's life = 1 and experience = 1", msg="Army 1 wrong for Fairer 1,0,0 0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

# =============================================================================================================================
        # your second tests for __conduct_combat go here #

        # PLAYER 1 WIN #
        # Test if combat is conducted correctly and if it returns
        # appropriate result for all Soldier p1 army and 1 p2 army
        # Assumes __assign_army is working correctly
        # manual inputs 
        t1._Army__assign_army("", 20, 0, 0, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Fairer 20,0,0 0,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        
        # PLAYER 2 WIN #
        # Tests combat is conducted correctly and if it
        # returns appropriate result for 1 Soldier p1 army and all Soldier p2 army
        # Assumes __assign_army is working correctly 
        t1._Army__assign_army("", 1, 0, 0, formation)
        t2._Army__assign_army("", 30, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Fairer 1,0,0 30,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force), "", msg="Army 1 wrong for Fairer 1,0,0 30,0,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "Soldier's life = 1 and experience = 0,Soldier's life = 2 and experience = 1,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0,Soldier's life = 3 and experience = 0"
            , msg="Army 2 wrong for Fairer 1,0,0 0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

# =============================================================================================================================
        # your third tests for __conduct_combat go here #
        
        # DRAW #
        # Test if combat is conducted correctly and if it returns
        # appropriate result for all Soldier p1 army and all Cavalry p2 army
        # Assumes __assign_army is working correctly
        # manual inputs 
        t1._Army__assign_army("", 5, 5, 5, formation)
        t2._Army__assign_army("", 5, 5, 5, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Fairer 5,5,5 5,5,5 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # DRAW #
        # Tests combat is conducted correctly and if it
        # returns appropriate result for 5 Soldier, 5 Archer, 5 Cavalry p1 army and 5 Soldier, 5 Archer, 5 Cavalry p2 army
        # Assumes __assign_army is working correctly
        # manual inputs 
        t1._Army__assign_army("", 5, 5, 5, formation)
        t2._Army__assign_army("", 5, 5, 5, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Fairer 5,5,5 5,5,5 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force), "", msg="Army 1 wrong for Fairer 5,5,5 5,5,5")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 5,5,5 5,5,5")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask5)
    unittest.TextTestRunner(verbosity=0).run(suite)
