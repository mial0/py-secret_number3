from functions import *

while True:
    select = input("What do you want to do? A) play a new game B) see the top scores C) quit? ")
    if select == "A":
        select_game_level=input("Choose the level of the game: E) easy H) hard? ")
        if select_game_level == "E":
            play_game_easy()
        elif select_game_level == "H":
            play_game_hard()
    elif select == "B":
        for score_dict in top_score():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
