import json
import os
import shutil


def update_assets(assets_file: str, root_dir: str, sc_path: str):
    # open assets file
    with open(assets_file, 'r') as f:
        assets = json.load(f, strict=False)

    # define target speech and binks dir
    speech_dir = os.path.join(sc_path, 'fx', 'Speech')
    binks_dir = os.path.join(sc_path, 'binks')

    # update each character
    for char in assets.keys():
        # update speech files
        for item in assets[char]['Speech'].items():
            if item[0]:
                shutil.copy2(os.path.join(root_dir, item[0]), os.path.join(speech_dir, item[1] + '.wav'))
            else:
                os.remove(os.path.join(speech_dir, item[1] + '.wav'))

        # update binks
        for item in assets[char]['Binks'].items():
            if item[0]:
                shutil.copy2(os.path.join(root_dir, item[0]), os.path.join(binks_dir, item[1] + '.bik'))
            else:
                os.remove(os.path.join(binks_dir, item[1] + '.bik'))


def update_aivs(aiv_file: str, root_dir: str, sc_path: str):
    # open assets file
    with open(aiv_file, 'r') as f:
        aivs = json.load(f, strict=False)

    # define target speech and binks dir
    aiv_dir = os.path.join(sc_path, 'aiv')

    # update each character
    for char in aivs.keys():
        # update speech files
        for item in aivs[char].items():
            if item[0]:
                shutil.copy2(item[0], os.path.join(aiv_dir, item[1] + '.aiv'))
            else:
                os.remove(os.path.join(aiv_dir, item[1] + '.aiv'))
