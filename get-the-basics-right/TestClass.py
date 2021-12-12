class Player:
    teamName = "Liverpool"  # class level attributes

    def __init__(self, player_name, jersey_color, goals_scored):
        # Object level attributes...
        self.__player_name = player_name
        self.jersey_color = jersey_color
        self.goals_scored = goals_scored

    def to_String(self):
        a = 5
        #print("Player Name-->", self.player_name)
        print("Jersey Color-->", self.jersey_color)
        print("Goals Recorded-->", self.goals_scored)
        print("squaring this number", a ** 2)

    @classmethod  # class methods definition...
    def get_team_name(cls):
        print("You're currently playing for the team : ", cls.teamName)

    @staticmethod
    def get_top_player(name):
        print("the top player for Liverpool is ", name)


liver_pool = Player("Messi", "blue and Red", 2)

# this line will CAUSE ERROR!
#print(liver_pool.__player_name)

print(liver_pool.jersey_color)



# regular method
liver_pool.to_String()

# Class level methods.
Player.get_team_name()

# static method invocation
Player.get_top_player("Ronaldo")