from backend_py import Character_Sheet as new_character
from backend_py import Mods_Checks as Status

char_name = input("Qual o nome do seu personagem? ")
char_level = int(input("Qual o nível do seu personagem? "))

rolled_values = new_character.Character_Sheet.attributes_roll()

print("Os valores rolados para os atributos foram:", rolled_values)

print("\nDistribua os valores nos atributos desejados:")

print(rolled_values)
values = []

attributes = ["For", "Des", "Cons", "Int", "Sab", "Car"]
for i in range(len(rolled_values)):
    roll = int(input("Qual valor para " + attributes[i] + "? "))
    rolled_values.remove(roll)
    values.append(roll)
    print(values, "\n")
    print(rolled_values)

races_dict = {"a": "Elfo", "b": "Meio- Elfo", "c": "Meio-Orc", "d": "Anão", "e": "Halfling"}
choose_race = input("Qual a raça do seu personagem? \nEscolha a Letra equivalente a raça.\n" + str(races_dict))
chosen_race = str(races_dict[choose_race])

final_attribute = list(new_character.Character_Sheet.race(chosen_race, attributes, values).values())
print(final_attribute)
char_attributes = final_attribute

attribute_mod = Status.define_mods(char_attributes)
print(attribute_mod)

classes_dict = {"a": "Barbaro", "b": "Guerreiro", "c": "Mago", "d": "Clerigo", "e": "Ranger"}
choose_class = input("Qual a Classe do seu personagem?\n" + str(classes_dict))
chosen_class = str(classes_dict[choose_class])

print(char_name, "  ", char_level, " ", chosen_race, "  ", chosen_class, "\n", char_attributes, "\n", attribute_mod)

print(new_character.Character_Sheet.char_class(chosen_class, attribute_mod, char_level))
