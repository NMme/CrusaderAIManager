import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label

import os
import shutil
import json
import codecs




class MyApp(App):

    def build(self):
        self.root = "/home/Games/Crusader-HDUP/CrusaderAIManager"
        self.ai_shorts = {'Caliph': 'ca',
                          'Frederick': 'fr',
                          'Pig': 'pg',
                          'Phillip': 'ph',
                          'Richard': 'ri',
                          'Rat': 'rt',
                          'Saladin': 'sa',
                          'Sheriff': 'sh',
                          'Snake': 'sn',
                          'Sultan': 'su',
                          'Wolf': 'wf',
                          'Abbot': 'ab',
                          'Marshall': 'ma',
                          'Nizar': 'ni',
                          'Emir': 'em',
                          'Wazir': 'wa'
                          }
        self.characters = ['Caliph', 'Frederick', 'Pig', 'Phillip', 'Richard', 'Rat', 'Saladin', 'Sheriff', 'Snake',
                           'Sultan', 'Wolf', 'Abbot', 'Marshall', 'Nizar', 'Emir', 'Wazir']
        return Label(text='Hello world')


    def back_up_vanilla(self, sc_path: str):
        # backup all the vanilla stronghold files

        # create new folder
        vanilla_folder = os.path.join(self.root, 'vanilla')
        os.mkdir(vanilla_folder)
        os.mkdir(os.path.join(vanilla_folder, '_fx_speech_'))
        os.mkdir(os.path.join(vanilla_folder, '_binks_'))
        os.mkdir(os.path.join(vanilla_folder, '_resources_'))

        # copy all the original files here
        #shutil.copy2()


def create_assets_config_file():
    # open speech file
    with open('char_speech.json', 'r') as f:
        cs = json.load(f)

    # open binks file
    with open('char_binks.json', 'r') as f:
        bi = json.load(f)

    vanilla_root_dir = "/data/vanilla/speech"
    out_file = dict()

    # iterate over all characters
    for char in cs.keys():
        char_assets = dict()
        speech_files = dict()
        bink_files = dict()
        special_char = False
        char_assets['SpecialCharacter'] = 0

        # check what kind of character we have
        if cs[char]['num_actions'] == 22:
            special_char = True
            char_assets['SpecialCharacter'] = 1

        # add all speech actions
        for item in cs[char]['actions'].items():
            if item[1] > 0:
                if special_char and 'player' in item[0]:
                    file_keys = [cs[char]['prefix'] + '_' + item[0]]
                else:
                    file_keys = [cs[char]['prefix'] + '_' + item[0] + '_' + str(i).zfill(2) for i in range(1, item[1] + 1)]
                for f in file_keys:
                    speech_files[f] = os.path.join('vanilla', 'speech', (f + '.wav'))
        char_assets['Speech'] = speech_files

        # add special announcements for special characters
        if special_char:
            announce_files = {char + '_Attack': os.path.join('vanilla', 'speech', (char + '_Attack.wav')),
                              char + '_Defeat': os.path.join('vanilla', 'speech', (char + '_Defeat.wav'))}
            char_assets['Announcements'] = announce_files

        # add all bink files
        for item in bi[char]['actions'].items():
            if item[1] > 0:
                if bi[char]['numerate_files']:
                    file_keys = [bi[char]['prefix'] + '_' + item[0] + str(i) for i in range(1, item[1] + 1)]
                else:
                    file_keys = [bi[char]['prefix'] + '_' + item[0]]
                for f in file_keys:
                    bink_files[f] = os.path.join('vanilla', 'speech', (f + '.bik'))
        char_assets['Binks'] = bink_files

        out_file[char] = char_assets

    return out_file


def test_vanilla_replace(replace_char: str = 'Wazir'):
    # some paths
    vanilla_dir = "data/mod_base/vanilla"

    # load robin hood
    with open('data/robin_hood_mod/robinhood.json', 'r') as f:
        rh = json.load(f, strict=False)

    # load vanilla mode
    with open('data/mod_base/vanilla/vanilla.json', 'r') as f:
        vanilla = json.load(f, strict=False)

    characters = ['Caliph', 'Frederick', 'Pig', 'Phillip', 'Richard', 'Rat', 'Saladin', 'Sheriff', 'Snake',
                  'Sultan', 'Wolf', 'Abbot', 'Marshall', 'Nizar', 'Emir', 'Wazir']
    if replace_char not in characters:
        raise Exception('Invalid standard character')

    # replace aic
    # load vanilla aic
    with open(os.path.join(vanilla_dir, vanilla['AIC']), 'r') as f:
        aic = json.load(f, strict=False)
    # get index
    idx = [i for i in range(len(aic['AICharacters'])) if aic['AICharacters'][i]['Name'] == replace_char][0]
    # add Custom Name
    aic['AICharacters'][idx]['CustomName'] = rh['AIC']['CustomName']
    aic['AICharacters'][idx]['Personality'] = rh['AIC']['Personality']
    # output new AIC
    with open('data/output/my_aic.json', 'w') as f:
        json.dump(aic, f)

    # replace troops
    # load vanilla troops
    with codecs.open(os.path.join(vanilla_dir, vanilla['Troops']), 'r', 'utf-8-sig') as f:
        troops = json.load(f, strict=False)
    if 'Troops' in rh.keys():
        # get index
        idx = [i for i in range(1, 17) if troops[str(i)]['Name'] == replace_char][0]
        # add custom troops configuration
        troops[str(idx)]['Lord'] = rh['Troops']['Lord']
        troops[str(idx)]['normal'] = rh['Troops']['normal']
        troops[str(idx)]['crusader'] = rh['Troops']['crusader']
        troops[str(idx)]['deathmatch'] = rh['Troops']['deathmatch']
    # output new Troops file
    with open('data/output/my_troops.json', 'w') as f:
        json.dump(troops, f)

    # set new AVI files
    with open(os.path.join(vanilla_dir, vanilla['AIV']), 'r') as f:
        aiv = json.load(f, strict=False)
    if 'AIV' in rh.keys():
        for i, aiv_files in enumerate(aiv[replace_char].keys()):
            if rh['AIV'][str(i+1)]:
                aiv[replace_char][aiv_files] = os.path.join(rh['AIV']['base_dir'], rh['AIV'][str(i+1)])
    # output new AIV file
    with open('data/output/my_aiv.json', 'w') as f:
        json.dump(aiv, f)


if __name__ == '__main__':
    #MyApp().run()
    test_vanilla_replace(replace_char='Sultan')
