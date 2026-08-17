def calculate_team_total_rating(list_of_players: list) -> int:
    return sum(item.get_rating() for item in list_of_players)


def elves_concert(list_of_players: list) -> None:
    for item in list_of_players:
        item.play_elf_song()


def feast_of_the_dwarves(list_of_players: list) -> None:
    for item in list_of_players:
        item.eat_favourite_dish()
