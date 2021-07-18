import os
import json
from data_classes import SingleCharacter, BaseMod


def run_test():
    # load main config
    with open('main_config.json', 'r') as f:
        cfg = json.load(f, strict=False)

    print('Hello, and Welcome to the CrusaderAI Manager!')
    print('=====')
    print('Choose a base-mod:')
    for i, bm in enumerate(cfg['installed_base_mods']):
        print('%i) ' % i + bm)
    num = int(input("Please enter a number:"))
    base = BaseMod(os.path.join('data', 'mod_base', cfg['installed_base_mods'][num]), cfg['vanilla_dir'])
    print('=====')
    print('Choose a ai-mod to add to base:')
    for i, bm in enumerate(cfg['installed_mods']):
        print('%i) ' % i + bm)
    num = int(input("Please enter a number:"))
    char = SingleCharacter(os.path.join('data', cfg['installed_mods'][num]))
    print('=====')
    rc = input('Enter a Characters Name to replace ai with:')
    base.update_character(char, rc)
    base.save_base_mod(cfg['out_dir'])


if __name__ == '__main__':
    run_test()