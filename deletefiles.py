from glob import glob
import os 

for filename in glob('**', recursive=True):
    if '.csv' in filename and not 'EMG.csv' in filename:
        os.remove(filename)