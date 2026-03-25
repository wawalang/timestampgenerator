import audioread, sys
from pathlib import Path
whitelist=[] # whitelisted file extensions
noConv=[] # non-converted song durations
sNamesNoExt=[] # song names (no extensions)
ttNo=[] # timestamps without proper conversion
timestamps=[] # timestamps with proper conversion
cwl=True # "Continue White List"
while cwl: # whitelist-appender
    a=input("type filename to whitelist, with the dot: ")
    whitelist.append(a)
    b=input('type "n" to exit whitelisting, enter to continue: ')
    if b=="n":
        cwl=False
def durationsep(leng): # Duration Separator
    hours=leng//3600
    leng%=3600
    minutes=leng//60
    leng%=60
    seconds=round(leng, 2) # rounds duration to a simpler float for ease of understanding.
    return hours, minutes, seconds
def songlister(path): # Returns song names according to file type.
    p=Path(path)
    files=[i.name for i in p.iterdir() if i.is_file() and i.suffix.lower() in whitelist] # need to understand
    return files
directory=input("Type the directory of the album.\n(press enter if script is in correct directory.)\n>>> ")
for i in songlister(directory):
    audiof=audioread.audio_open(directory+"/"+i)
    for w in whitelist:
        sNamesNoExt.append(i.strip(w))
    length=round(audiof.duration, 2)
    noConv.append(length)
for i in noConv:
    if ttNo:
        ttNo.append(timestamps[-1]+i)
    else:
        ttNo.append(i)
