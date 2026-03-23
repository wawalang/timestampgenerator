songl=[]
conv_songl=[]
timestamps=[]
ttc=[[0,0]]
taken=True
while taken:
    a=int(input("Enter minutes: "))
    b=int(input("Enter seconds: "))
    ab=[a,b]
    songl.append(ab)
    print("number of songs:" + str(len(songl)))
    c = input("continue? y/n\n>>> ")
    if c == "n":
        taken=False

for i in songl:
    m=i[0]
    s=i[1]
    tconv=m*60+s
    conv_songl.append(tconv)
for i in conv_songl:
    if timestamps:
        timestamps.append(timestamps[-1]+i)
    else:
        timestamps.append(i)
for i in timestamps:
    cm=i//60
    cs=i%60
    ttc.append([cm,cs])
print("TIMESTAMP LIST:")
for i in ttc:
    print(str(i[0])+":"+str(i[1]))
