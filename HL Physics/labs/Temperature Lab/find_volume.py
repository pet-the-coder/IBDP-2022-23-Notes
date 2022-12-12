
POINTS = """144	0.13
200	0.17
231	0.22
311	0.23
361	0.28
446	0.39
512	0.47
567	0.53
624	0.54
699	0.58""".split('\n')

LEFT, RIGHT = [], []
for i in POINTS:
    j = i.split()
    LEFT.append(float(j[0]))
    RIGHT.append(float(j[1]))

# find volume
def volume(p, t):
    return (50/6.02/(10**23) * 8.31 * p) / t

# find volume values
VOLUME = [volume(i, j) for i, j in zip(LEFT, RIGHT)]

# avg volume
VAVG = sum(VOLUME) / len(VOLUME)
print("Average Volume:", VAVG)

# uncertainty
def find_percent_unc(val, uncer):
    return uncer / val * 100

UVP = 0.01
UPLIST = [find_percent_unc(v, UVP) for v in RIGHT]

print("ERROR:", sum(UPLIST) / 100 * VAVG)

