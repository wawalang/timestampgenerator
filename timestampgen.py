import audioread, sys, itertools
from pathlib import Path
whitelist=[] # whitelisted file extensions
noConv=[] # non-converted song durations
sNamesNoExt=[] # song names (no extensions)
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
    files=sorted([i.name for i in p.iterdir() if i.is_file() and i.suffix.lower() in whitelist]) # need to understand
    return files
def timestFormat(h,m,s, songname): # converts the duration and song name into the timestamp format.
    if h==0:
        return str(int(m)).zfill(2)+":"+str(s).zfill(2)+" - "+songname
    else:
        return str(int(h)).zfill(2)+":"+str(int(m)).zfill(2)+":"+str(s).zfill(2)+" - "+songname
directory=input("Type the directory of the album.\n(press enter if script is in correct directory.)\n>>> ")
for i in songlister(directory):
    if directory=="":
        audiof=audioread.audio_open(i)
    else:
        audiof=audioread.audio_open(directory+"/"+i)
    for w in whitelist:
        sNamesNoExt.append(Path(i).stem)
    length=round(audiof.duration, 1)
    noConv.append(length)
ttNo2=list(itertools.accumulate(noConv))
for i in ttNo2:
    hours, minutes, seconds=durationsep(i)
    seconds=int(seconds)
    timestamps.append([hours, minutes, seconds])
print("CONVERTED TIMESTAMPS:\n00:00 - "+sNamesNoExt[0])
for ind, it in enumerate(timestamps):
    if ind+1>len(timestamps)-1:
        break
    else:
        print(timestFormat(it[0],it[1],it[2],sNamesNoExt[ind+1]))
