from loaders.reader import Reader
from loaders.read_json import read_json


HOME_PATH = '/home/omaresquivel'
DEV_PATH = '/home/omaresquivel/Desarrollo'
BASH_PATH = '/home/omaresquivel/Desarrollo/bash'


reader = Reader(
    HOME_PATH,
    {
        'dev_path': DEV_PATH,
        'bash_path': BASH_PATH,
    }
)

reader.define_reader('json', read_json)
response_pokemon = reader.reader('json', '/', '/home/omaresquivel/Desarrollo/bash/pokemon.json')


print('\n\nresponse_pokemon')
for key in list(response_pokemon.keys()):
    print(key)
print(response_pokemon.get('name'))
print(response_pokemon.get('forms'))
print(response_pokemon.get('abilities'))