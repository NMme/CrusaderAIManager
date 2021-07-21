# CrusaderAIManager
AI mod managing tool for Firefly Studio's game 'Stronghold Crusader'.

**Caution: Still very early in development and only has a small demo running**

## Idea behind this Tool
With the release of the [Unofficial Crusader Patch](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch) it became possible to add your own AIs to the game.
However adding multiple AI mods is a bit of a hassle as each new AI needs to replace one of the 16 original AIs in the game. This includes renaming AI asset (Speech .wav, video .bik) and castel data files (.aiv) to the according original AIs file name.

This tools aims to make this process a bit more easier by allowing to load a single new character AI mod into an existing 'base-mod' (can be vanilly, UCP-ai-patch or any other mod that includes all 16 original characters) by specifiying the name of the original character it replaces.
New .json files are created containing data paths to the assets of an ai (speech, binks) so they can be automatically managed by some assets manager.

UCP-patch should then be used to add the new aic an aivs to the game.

## Current status
There is a small command line demo 'ai_manager_cli.py' that can replace a single character in a basic configuration. This succesfully creates a new aic-file, troops-file and other .json files specifing file paths for .aiv and the other assets of all ais.

Next a assets-manager should be included which automatically composes the assets directories from the configuration defined in the .json of the assets.


## Why in Python?
I know python is not most efficient but it is running cross plattform and I like it.
Eventually a GUI should be added and the project can be packaged for various plattforms to make it more easily accessible.
