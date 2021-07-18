import json
import os
import codecs


class SingleCharacter:

    def __init__(self, mod_file_path: str):
        self.file_path = mod_file_path
        self.root_dir = os.path.dirname(self.file_path)
        # load json file
        with open(self.file_path, 'r') as f:
            self.data = json.load(f, strict=False)

        self.aic = self.data['AIC']
        self.aiv = None
        self.aiv_base_dir = None
        self.troops = None
        self.assets = None
        self.assets_speech_dir = None
        self.assets_binks_dir = None
        if 'AIV' in self.data.keys():
            self.aiv = self.data['AIV']
            self.aiv_base_dir = os.path.join(self.root_dir, self.aiv['base_dir'])
        if 'Troops' in self.data.keys():
            self.troops = self.data['Troops']
        if 'Assets' in self.data.keys():
            self.assets = self.data['Assets']
            self.assets_speech_dir = os.path.join(self.root_dir, self.assets['base_dir'], self.assets['Speech']['base_dir'])
            self.assets_binks_dir = os.path.join(self.root_dir, self.assets['base_dir'], self.assets['Binks']['base_dir'])

    def get_num_speech_assets(self):
        fx_files = [item for sublist in self.assets['Speech'].values() for item in sublist]
        return len(fx_files)

    def get_num_binks_assets(self):
        bik_files = [item for sublist in self.assets['Binks'].values() for item in sublist]
        return len(bik_files)


class BaseMod:

    def __init__(self,
                 base_file_path: str,
                 vanilla_path: str):
        self.base_file_path = base_file_path
        self.base_dir = os.path.dirname(self.base_file_path)
        self.vanilla_path = vanilla_path
        with open(self.base_file_path, 'r') as f:
            self.base_file = json.load(f, strict=False)
        self.aic = None
        self.troops = None
        self.aiv = None
        self.assets = None
        self.load_files()

    def load_files(self) -> None:
        """
        load all the relevant files from base mod config file
        """
        # Load AIC file
        if self.base_file['AIC']:
            with codecs.open(os.path.join(self.base_dir, self.base_file['AIC']), 'r', 'utf-8-sig') as f:
                self.aic = json.load(f, strict=False)
        else:
            # load Vanilla AIC
            with open(os.path.join(self.vanilla_path, 'vanilla_aic.json'), 'r') as f:
                self.aic = json.load(f, strict=False)

        # Load Troops file
        if self.base_file['Troops']:
            with codecs.open(os.path.join(self.base_dir, self.base_file['Troops']), 'r', 'utf-8-sig') as f:
                self.troops = json.load(f, strict=False)
        else:
            # load Vanilla Troops
            with open(os.path.join(self.vanilla_path, 'vanilla_troops.json'), 'r') as f:
                self.troops = json.load(f, strict=False)

        # Load AIV file
        if self.base_file['AIV']:
            with open('char_aiv.json', 'r') as f:
                self.aiv = json.load(f, strict=False)
                for char in self.aiv.keys():
                    for item in self.aiv[char].items():
                        self.aiv[char][item[0]] = os.path.join(os.path.abspath(self.base_file['AIV']), item[1])
        else:
            # load Vanilla AIV
            with open(os.path.join(self.vanilla_path, 'vanilla_aiv.json'), 'r') as f:
                self.aiv = json.load(f, strict=False)
                for char in self.aiv.keys():
                    for item in self.aiv[char].items():
                        self.aiv[char][item[0]] = os.path.join(self.vanilla_path, item[1])

        # Load Assets file
        if self.base_file['Assets']:
            with open(os.path.join(self.base_dir, self.base_file['Assets']), 'r') as f:
                self.assets = json.load(f, strict=False)
        else:
            # load Vanilla Assets
            with open(os.path.join(self.vanilla_path, 'vanilla_assets.json'), 'r') as f:
                self.assets = json.load(f, strict=False)
                for char in self.assets.keys():
                    for item in self.assets[char]['Speech'].items():
                        self.assets[char]['Speech'][item[0]] = os.path.join(self.vanilla_path, 'assets', item[1])
                    for item in self.assets[char]['Binks'].items():
                        self.assets[char]['Binks'][item[0]] = os.path.join(self.vanilla_path, 'assets', item[1])

    def update_character(self, new_char: SingleCharacter, replace_char: str = 'Wazir') -> bool:
        """
        Update characters
        :param new_char:
        :param replace_char:
        :return: <bool> showing update success
        """

        characters = ['Caliph', 'Frederick', 'Pig', 'Phillip', 'Richard', 'Rat', 'Saladin', 'Sheriff', 'Snake',
                      'Sultan', 'Wolf', 'Abbot', 'Marshall', 'Nizar', 'Emir', 'Wazir']
        if replace_char not in characters:
            raise Exception('Invalid standard character name given for update')

        # update AIC
        # get index
        idx = [i for i in range(len(self.aic['AICharacters'])) if self.aic['AICharacters'][i]['Name'] == replace_char][0]
        # add Custom Name
        self.aic['AICharacters'][idx]['CustomName'] = new_char.aic['CustomName']
        self.aic['AICharacters'][idx]['Personality'] = new_char.aic['Personality']

        # update Troops
        if new_char.troops:
            # get index
            idx = [i for i in range(1, 17) if self.troops[str(i)]['Name'] == replace_char][0]
            # add custom troops configuration
            self.troops[str(idx)]['Lord'] = new_char.troops['Lord']
            self.troops[str(idx)]['normal'] = new_char.troops['normal']
            self.troops[str(idx)]['crusader'] = new_char.troops['crusader']
            self.troops[str(idx)]['deathmatch'] = new_char.troops['deathmatch']

        # update AIV
        if new_char.aiv:
            for i, item in enumerate(self.aiv[replace_char].items()):
                self.aiv[replace_char][item[0]] = os.path.join(os.path.abspath(new_char.aiv_base_dir),
                                                               new_char.aiv[str(i+1)])

        # Update Assets
        if new_char.assets:
            new_speech_dict = dict.fromkeys(self.assets[replace_char]['Speech'], "")
            new_binks_dict = dict.fromkeys(self.assets[replace_char]['Binks'], "")
            special_character = False
            if self.assets[replace_char]['SpecialCharacter']:
                # special character (Pig, Rat, Snake, Wolf) -> different speech files (only 22 files)
                special_character = True

            # Update speech file paths
            with open('char_speech.json', 'r') as f:
                sp_info = json.load(f)
            for item in new_char.assets['Speech']['actions'].items():
                key_pre = sp_info[replace_char]['prefix'] + '_' + item[0]
                if item[1]:
                    if special_character and 'player' in item[0]:
                        keys = [key_pre for i
                                in range(len(item[1][:sp_info[replace_char]['actions'][item[0]]]))]
                    else:
                        keys = [key_pre + '_' + str(i + 1).zfill(2) for i
                                in range(len(item[1][:sp_info[replace_char]['actions'][item[0]]]))]

                    for i, k in enumerate(keys):
                        new_speech_dict[k] = os.path.join(new_char.assets_speech_dir, item[1][i])
            self.assets[replace_char]['Speech'] = new_speech_dict

            # Update binks videos
            with open('char_binks.json', 'r') as f:
                bik_info = json.load(f)
            for item in new_char.assets['Binks']['actions'].items():
                if item[1]:
                    action = item[0]
                    # anger or angry?
                    if item[0] == 'anger':
                        if bik_info[replace_char]['actions']['anger'] == 0 and bik_info[replace_char]['actions']['angry'] == 1:
                            action = 'angry'
                    # taunt or taunting?
                    elif item[0] == 'taunt':
                        if bik_info[replace_char]['actions']['taunt'] == 0 and bik_info[replace_char]['actions']['taunting'] == 1:
                            action = 'taunting'
                    # create the keys
                    if bik_info[replace_char]['numerate_files']:
                        keys = [bik_info[replace_char]['prefix'] + '_' + action + str(i+1)
                                for i in range(len(item[1][:bik_info[replace_char]['actions'][item[0]]]))]
                    else:
                        keys = [bik_info[replace_char]['prefix'] + '_' + action
                                for i in range(len(item[1][:bik_info[replace_char]['actions'][item[0]]]))]
                    for i, k in enumerate(keys):
                        new_binks_dict[k] = os.path.join(new_char.assets_binks_dir, item[1][i])
            self.assets[replace_char]['Binks'] = new_binks_dict

        return True

    def save_base_mod(self, output_dir: str, output_name: str = 'my_mod') -> None:
        # save aic file
        with open(os.path.join(output_dir, output_name + '_aic.json'), 'w') as f:
            json.dump(self.aic, f)

        # save troops file
        with open(os.path.join(output_dir, output_name + '_troops.json'), 'w') as f:
            json.dump(self.troops, f)

        # save aiv file
        with open(os.path.join(output_dir, output_name + '_aiv.json'), 'w') as f:
            json.dump(self.aiv, f)

        # save assets file
        with open(os.path.join(output_dir, output_name + '_assets.json'), 'w') as f:
            json.dump(self.assets, f)

