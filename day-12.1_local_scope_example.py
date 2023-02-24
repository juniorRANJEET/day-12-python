# local scope
# local function exit "with in function" not outside the function
def drink_portion():
    portion_strength = 2
    print(portion_strength)
drink_portion()
print(portion_strength) # this will throw an error