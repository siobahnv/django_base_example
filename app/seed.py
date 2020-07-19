from app.models import Example, User

def seedTheUserData():
    player_file = ["Bryan", "Greg", "JoHannah"]

    for player in player_file:
        new_player = User(
            username=player,
            first_name=player,
            password=None,
        )
        new_player.set_password("lolz")
        new_player.save()

def seedEverything():
    seedTheUserData()
    print("Finished seeding!")
