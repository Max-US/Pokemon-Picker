red_elements = ["fire", "fighting", "fairy", "rock"]

pokemon = ["Charmander", "Machamp", "Clefairy", "Rampardos"]


def favorite_element(element):
    for i in range(0, len(red_elements)):
        if red_elements[i].title() == element:
            return pokemon[i]