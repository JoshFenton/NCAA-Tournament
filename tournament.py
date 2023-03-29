from inspect import getmembers
import pandas as pd

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
        if self.round != "finals":
            if self.advance_to.top_from == self:
                self.advance_to.top_team = team
                self.advance_to.top_seed = seed
            else:
                self.advance_to.bottom_team = team
                self.advance_to.bottom_seed = seed
        else:
            print("Congratulations! {} just won the championship!".format(self.winner))
    
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
            
    def __str__(self):
        if self.winner == None:
            if (self.top_team != None) & (self.bottom_team != None):
                return "This is a game in the {} region in the {} between {} and {}. The game has not been played yet.".format(self.region, self.round, self.top_team, self.bottom_team)
            else:
                return "This is a game in the {} region in the {}. The matchup has not been set yet.".format(self.region, self.round)
        else:
            return "This was a game in the {} region in the {}. The matchup was between {}, who scored {} points, and {}, who scored {} points. {} won.".format(self.region, self.round, self.top_team, self.top_score, self.bottom_team, self.bottom_score, self.winner)

"""
Rounds: round of 64, round of 32, sweet sixteen, elite eight, semifinals, finals
"""

teams = ["Alabama",
         "Texas A&M-CC",
         "Maryland",
         "West Virginia",
         "San Diego St",
         "Charleston",
         "Virginia",
         "Furman",
         "Creighton",
         "NC State",
         "Baylor",
         "UCSB",
         "Missouri",
         "Utah State",
         "Arizona",
         "Princeton",
         "Purdue",
         "Farleigh Dickinson",
         "Memphis",
         "FAU",
         "Duke",
         "Oral Roberts",
         "Tennessee",
         "Louisiana",
         "Kentucky",
         "Providence",
         "Kansas St",
         "Montana St",
         "Michigan St",
         "USC",
         "Marquette",
         "Vermont",
         "Houston",
         "N Kentucky",
         "Iowa",
         "Auburn",
         "Miami",
         "Drake",
         "Indiana",
         "Kent State",
         "Iowa State",
         "Pittsburgh",
         "Xavier",
         "Kennesaw St",
         "Texas A&M",
         "Penn State",
         "Texas",
         "Colgate",
         "Kansas",
         "Howard",
         "Arkansas",
         "Illinois",
         "Saint Marys",
         "VCU",
         "UConn",
         "Iona",
         "TCU",
         "Arizona State",
         "Gonzaga",
         "Grand Canyon",
         "Northwestern",
         "Boise St",
         "UCLA",
         "UNC Asheville"]

class ncaa_tournament:
    def __init__(self, teams):
        games = pd.read_csv('games.csv')
        for i in range(len(games)):
            if i <= 31:
                exec("self.game_{}_{}_{} = game(region = '{}', rnd='{}', index={}, top_team='{}', bottom_team='{}', top_seed={}, bottom_seed={})".format(games.region[i], games.rnd[i], games.indx[i], str(games.region_name[i]), games.round_str[i], games.indx[i], teams[2*i], teams[(2*i)+1], games.top_seed[i], games.bottom_seed[i]))
            else:
                exec("self.game_{}_{}_{} = game(region = '{}', rnd='{}', index={}, top_from=self.{}, bottom_from=self.{})".format(games.region[i], games.rnd[i], games.indx[i], str(games.region_name[i]), games.round_str[i], games.indx[i], games.top_from[i], games.bottom_from[i]))

"""
TODO
    --> find a way to save game progress as it is put in so you don't have to "play" every game in
        the tournament every time you initialize the tournament
        --> maybe a separate spreadsheet? With an update function to populate the tournament with
            games that have already been played?
            --> need separate save files so we can start from scratch if we want to.
    
    --> build the complete GUI for the tournament
        --> place all games in the entire frame
        --> build out the function to "play" the game in a different window/tab that then updates
            the results in the original game frame
            --> function should also advance the winner to the next game
    
    --> fit all created Game classes in the tournament to their respective gmae frame in the GUI
        --> maybe need to keep a list in the ncaa_tournament class that keeps track of all the
            games created in it so we can iterate through it
        --> build class methods to update the GUI and Games in the tournament at the same time
"""
        
game_1 = game("East", 32, 1)
game_2 = game("East", 16, 1, bottom_from=game_1)

print(getmembers(game_1))