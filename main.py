import copy
import random

reference = None

class State(object):
    
    """State of clovece"""
    def __init__(self, players = None, turn = 0):
        if players is not None:
            self.pl = players
        else:
            self.pl = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
        self.turn = turn
    
    def dice(self, player_id, thing_id, step):
        player = list(self.pl[player_id]).copy()
        player[thing_id] += step
        copy_pl = copy.deepcopy(self.pl)
        copy_pl[player_id] = player
        new_turn = self.turn + 1
        return State(copy_pl, new_turn)
    
    def print_state(self):
        for i in range(0, len(self.pl)):
            print("Player %d's pieces are on fields: 0:%d 1:%d 2:%d 3:%d" 
                  % (i, self.pl[i][0], self.pl[i][1],
                        self.pl[i][2],
                        self.pl[i][3]))

    def turn_player(self):
        return self.turn % 4
    
    def pass_turn(self):
        return State(self.pl, self.turn + 1)

if __name__ == "__main__":
    reference = State()
    while reference.turn_player() < 10:
        print("Player %d on turn." % reference.turn_player())
        dice = random.randint(1, 6)
        print("Dice: ", dice)
        reference.print_state()
        command = input(">")
        if command.startswith("move "):
            id_thing = command.split(" ")[1]
            reference = reference.dice(
                    reference.turn_player(),
                    int(id_thing), dice)
        else:
            reference = reference.pass_turn()

