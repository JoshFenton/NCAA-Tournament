from inspect import getmembers

class game:
    def __init__(self, region, rnd, index, top_from=None, bottom_from=None, winner=None,
                 advance_to=None, top_team = None, bottom_team=None, top_score=None,
                 bottom_score=None, top_seed=None, bottom_seed=None):
        self.region = region
        self.round = rnd
        self.winner = winner
        self.name = region + "_" + str(rnd) + "_" + str(index)
        self.advance_to = advance_to
        self.bottom_from = bottom_from
        if self.bottom_from != None:
            self.bottom_from.advance_to = self
        self.top_from = top_from
        if self.top_from != None:
            self.top_from.advance_to = self
        self.top_team = top_team
        self.bottom_team = bottom_team
        self.top_score = top_score
        self.bottom_score = bottom_score
        self.top_seed = top_seed
        self.bottom_seed = bottom_seed
    
    def get_region(self):
        return self.region
    
    def get_round(self):
        return self.round
    
    def get_name(self):
        return self.name
    
    def set_winner(self, team):
        self.winner = team
        if self.top_team == team:
            seed = self.top_seed
        else:
            seed = self.bottom_seed
        if self.advance_to.top_from == self:
            self.advance_to.top_team = team
            self.advance_to.top_seed = seed
        else:
            self.advance_to.bottom_team = team
            self.advance_to.bottom_seed = seed
    
    def set_score_top(self):
        self.top_score = input("How many points did {} score?".format(self.top_team))
    
    def set_score_bottom(self):
        self.bottom_score = input("How many points did {} score?".format(self.bottom_team))
    
    def play_game(self):
        self.set_score_top()
        self.set_score_bottom()
        if self.top_score > self.bottom_score:
            self.set_winner(self.top_team)
        else:
            self.set_winner(self.bottom_team)
        
game_1 = game("East", 32, 1)
game_2 = game("East", 16, 1, bottom_from=game_1)

print(getmembers(game_1))