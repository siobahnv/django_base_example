from app.models import Player, User, Course, Birdie

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

def seedTheCourseData():
    courses = [
        "Broadmoor",
        "Camas Meadows",
        "Colwood",
        "Heron Lakes Great Blue",
        "Heron Lakes Greenback",
        "Tri Mountain"
    ]

    for course in courses:
        new_course = Course(
            name=course
        )
        new_course.save()

def seedEverything():
    seedTheUserData()
    seedTheCourseData()
    print("Finished seeding!")
