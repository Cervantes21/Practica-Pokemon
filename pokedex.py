import requests
import json
import os

url = 'http://pokeapi.co/api/v2/pokemon/'

def buscarPokemon(num):
    peticion = requests.get(url + str(num))
    respuesta = json.loads(peticion.content)
    print(respuesta['name'])

if __name__ == '__main__':

    while True:

        option = input('\nEnter para ingresar al Pokedex \nZ para Salir ')
        if option == '':
            os.system('clear')
            poke_num = input('Da un número del 1 al 898 para elegir un pokemón: ')
            os.system('clear')
            buscarPokemon(poke_num)

        elif option == 'z':
            os.system('clear')
            print('Au revoir!!')
            break

