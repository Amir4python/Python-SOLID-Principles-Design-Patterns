"""
Working with Class Aggregation
Create two classes called "Team" and "Player" to represent sports teams and their players using class aggregation.

Class "Player":

Properties:

name (a string representing the player's name)

position (a string representing the player's position) - number (an integer representing the player's jersey number)

Methods:

__init__(self, name, position, number): Initializes the player with the given name, position, and jersey number.

Class "Team":

Properties:

name (a string representing the team's name)

players (a list of Player instances representing the team's players)

Methods:

__init__(self, name): Initializes the team with the given name and an empty list of players.

add_player(self, player): Adds a player (Player instance) to the team's players list.

get_player_info(self, number): Returns a string containing the player's name, position, and jersey number in the format "Name (Position) - Number" for the player with the given jersey number. If no player is found with the given jersey number, return "Player not found."


"""

class Player:
    def __init__(self, name, position, number):
        # Initialize the name, position, and number properties
        self.name=name
        self.position=position
        self.number=number

class Team:
    def __init__(self, name):
        # Initialize the name property and an empty players list
        self.name=name
        self.players=[]

    def add_player(self, player):
        # Add a Player instance to the team's players list
        self.players.append(player)

    def get_player_info(self, number):
        # Return the player's name, position, and jersey number as a formatted string
        # or "Player not found" if no player with the given jersey number is found
        for player in self.players:
            if player.number==number:
                return f"{player.name} ({player.position}) - {player.number}"
        else:
            return "Player not found."
if __name__=="__main__":
# Test your implementation
    player1 = Player("John Doe", "Forward", 10)
    player2 = Player("Jane Smith", "Midfielder", 8)
    player3 = Player("Mark Johnson", "Defender", 4)

    team1 = Team("Dream Team")
    team1.add_player(player1)
    team1.add_player(player2)

    print(team1.get_player_info(10))  # Should output "John Doe (Forward) - 10"
    print(team1.get_player_info(8))   # Should output "Jane Smith (Midfielder) - 8"
    print(team1.get_player_info(4))   # Should output "Player not found"
