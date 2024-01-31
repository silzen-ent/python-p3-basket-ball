def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

# print(game_dict().values()) #D1.1

#D1.2: num_points_per_game()
def num_points_per_game(player_name): 
    for team_data in game_dict().values():
        for player_data in team_data["players"]:
            if player_data["name"] == player_name:
                return player_data["points_per_game"]
    return None 
print(num_points_per_game("Kristaps Porzingis")) 


#D2
def player_age(player_name): 
    for team_data in game_dict().values():
        for player_data in team_data["players"]:
            if player_data["name"] == player_name:
                return player_data["age"]
    return None
print(player_age("Rui Hachimura"))


#D3: team_colors()
def team_colors(name):
    for team_data in game_dict().values():
        if team_data["team_name"] == name:
            return team_data["colors"]
    return None
print(team_colors("Cleveland Cavaliers"))


#D4: team_names()
def team_names():
    return [team_data["team_name"] for team_data in game_dict().values()]
print(team_names())


#D5: player_numbers()
def player_numbers(team_name):
    for team_data in game_dict().values():
        if team_data["team_name"] == team_name:
            return [player_data["number"] for player_data in team_data["players"]]
    return None
print(player_numbers("Cleveland Cavaliers"))


#D6: player_stats()
def player_stats(player_name):
    for team_data in game_dict().values():
        for player_data in team_data["players"]:
            if player_data["name"] == player_name:
                return {
                    "name:": player_data["name"],
                    "number:": player_data["number"],
                    "position:": player_data["position"],
                    "points_per_game:": player_data["points_per_game"],
                    "rebounds_per_game:": player_data["rebounds_per_game"],
                    "assists_per_game:": player_data["assists_per_game"],
                    "steals_per_game:": player_data["steals_per_game"],
                    "blocks_per_game:": player_data["blocks_per_game"],
                    "career_points:": player_data["career_points"],
                    "age:": player_data["age"],
                    "height_inches:": player_data["height_inches"],
                    "shoe_brand:": player_data["shoe_brand"]
                }
    return None
print(player_stats("Darius Garland"))

#D7: average_rebounds_by_shoe_brand()
def average_rebounds_by_shoe_brand():
    rebounds_by_brand = {}
    players_counts_by_brand = {}

    for team_data in game_dict().values():
        for player_data in team_data["players"]:
            brand = player_data["shoe_brand"]
            rebounds = player_data["rebounds_per_game"]

            if brand not in rebounds_by_brand:
                rebounds_by_brand[brand] = []
                players_counts_by_brand[brand] = 0

            rebounds_by_brand[brand].append(rebounds)
            players_counts_by_brand[brand] += 1

    for brand, rebounds_list in rebounds_by_brand.items():
        average_rebounds = sum(rebounds_list) / players_counts_by_brand[brand]
        print(f"{brand}: {average_rebounds: .2f}")
average_rebounds_by_shoe_brand()