# global scope
# global function: once defined it carried out even though it is not defined with in function


player_health_rating = 10
def drink_portion():
    portion_strength = 2
    print(player_health_rating) # player_health_rating not defined with in function
drink_portion()
#print(player_health_rating) # not throw an error
