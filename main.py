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
    
    def dice(self, player_id, thing_id):
        step = random.randint(1, 6)
        print("Dice: ", step)
        player = list(self.pl[player_id])
        player[thing_id] += step
        copy_pl = copy.deepcopy(self.pl)
        copy_pl[player_id] = player
        new_turn = self.turn + 1
        return State(copy_pl, new_turn)
    
    def print_state(self):
        for i in range(0, len(self.players)):
            print("Player %d's pieces are on fields:%d:40 %d:41 %d:42 %d:43" 
                    % (i, self.players[i][0], self.players[i][1],
                        self.players[i][2],
                        self.players[i][3]))


if __name__ == "__main__":
    reference = State()
    




