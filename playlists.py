import os 
import sys

LINES = open('playlists.txt', 'r').readlines()

os.chdir('playlists')

def sync_playlist(playlist, link):
    # if folder does not exists not create one, then switch to the directory
    if not os.path.isdir(playlist):
        os.mkdir(playlist)
    os.chdir(playlist)


    # check if sync file exists
    if os.path.exists(f'{playlist}.spotdl'):
        print('syncing in:', playlist)
        os.system(f'spotdl sync {playlist}.spotdl')
    else:
        print('creating sync file in:', playlist)
        os.system(f'spotdl sync {link} --save-file {playlist}.spotdl')

    # go back one directory
    os.chdir('..')

# if a specific playlist was passed
if len(sys.argv) > 1:
    for line in LINES:
        stripped = line.strip().split(" ")
        
        # skip comments
        if stripped[0][0] != "#":
            playlist, link = stripped

            if playlist == sys.argv[1]:
                sync_playlist(playlist, link)

# else sync all files
else:
    for line in LINES:
        stripped = line.strip().split(" ")
        
        # skip comments
        if stripped[0][0] != "#":
            playlist, link = stripped

            sync_playlist(playlist, link)