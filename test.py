import main
import unittest
import random
class TestClovece(unittest.TestCase):

    def test_pass_turn(self):
        ref = main.State()
        self.assertEqual(ref.turn_player(),0)
        ref = ref.pass_turn()
        self.assertEqual(ref.turn_player(),1)
        ref = ref.pass_turn()
        self.assertEqual(ref.turn_player(),2)
        ref = ref.pass_turn()
        self.assertEqual(ref.turn_player(),3)
        ref = ref.pass_turn()
        self.assertEqual(ref.turn_player(),0)

    def test_dice(self):
        ref = main.State()
        test_count = 6
        for i in range(test_count):
            player_id = random.randint(0,3)
            thing_id = random.randint(0,3)
            step = random.randint(1,6)
            last = ref.pl[player_id][thing_id]
            ref = ref.dice(player_id, thing_id, step)
            self.assertEqual(ref.pl[player_id][thing_id],last + step)

    def 
if __name__ == "__main__":
    unittest.main()
