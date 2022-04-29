from gtts import gTTS
from playsound import playsound
import os


def get_chracters(string):
    characters_list = []
    for i in range(len(string)):
        characters_list.append(string[i])
    return characters_list


def accuracy_number(word_characters_splited, list_of_words_characters_splited, max_matches=0, max_matches_index=0):
    for i in range(len(list_of_words_characters_splited)):
        count = 0
        for j in range(len(word_characters_splited)):
            if(word_characters_splited[j] in list_of_words_characters_splited[i]):
                count += 1
        if(count > max_matches):
            max_matches = count
            max_matches_index = i
    return max_matches_index


pokemon = input("Enter Pokemon Name : ")

# >>> making a list of all the pokemon names
pokemon_names = []
with open("Poke_ID.txt") as f:
    for i in range(1, 152):
        pokemon_names.append(f.readline().split()[1])

loop_check = True

while(True):
    if(pokemon in pokemon_names):
        with open("Poke_ID.txt") as f:
            for i in range(1, 152):
                name = f.readline()
                if((pokemon.lower()+"\n") in name):
                    ID = int(name[0]+name[1]+name[2])
                    break

        with open("Poke_Data.txt") as f:
            for i in range(3, 454, 3):
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                f.readline()
                if((i/3) == ID):
                    print("\n" + pokemon.capitalize() + " :\n")
                    print(line1+line2+line3)
                    print("PokeDex : (Speaking ...)")
                    gTTS(text=pokemon+"\n"+line1+line2+line3,
                         lang='en', slow=False).save("Dex_Audio.mp3")
                    playsound("Dex_Audio.mp3")
                    os.remove("Dex_Audio.mp3")
                    print("---------------------------------------------------\n")
                    break
            break
    else:
        if(loop_check == False):
            print("Pokemon Not Found...")
            break
        loop_check = False

        characters_list = get_chracters(pokemon)
        pokemon_names_characters_list = []
        
        for i in range(151):
            pokemon_names_characters_list.append(
                get_chracters(pokemon_names[i]))

        pokemon = pokemon_names[accuracy_number(characters_list, pokemon_names_characters_list)]
