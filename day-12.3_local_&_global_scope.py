# local & global scope


player_health_rating = 10
def game():
    def drink_portion():
        portion_strength = 2
        print(player_health_rating) #
    drink_portion()
game()