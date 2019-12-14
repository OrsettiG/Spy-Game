import random
from options import options


def generate_player_roles(request):
            # Get the number of players
            num_players = int(request['numPlayers'])
            # Find out the names of the players
            player_names = request['playerNames'].split(" ")
            # Create a list with an option for each player except the spy
            choice = [random.choice(options)] * (num_players - 1)
            # Add the spy to the list
            choice.append("Spy")
            # Shuffle the list of choices
            random.shuffle(choice)
            # Zip the player names and choices together to match them up
            output = list(zip(player_names, choice))
            # Print out the pairings
            return output



# set up a text in service using twilio (or comparable) so that players can each text the number and recive a role. roles reset once a number texts twice (so if 4 people are playing and they have all texted but then 2 more people show up and text in they will get the same roles.)

# a set list of numbers can text in the number of players to set up a game. if more players join later they can text "add x" to add more players to the game
