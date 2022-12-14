
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

# print(LEFT, RIGHT)

# find volume
n = 50 / (6.02*10**23)
R = 8.31
def volume(p, t):
    v = (n * R * p) / t
    print(p, t, v)
    return v

# uncertainty
def find_percent_unc(val, uncer):
    return uncer / val * 100

# find volume values
VOLUME = [volume(j, i) for i, j in zip(LEFT, RIGHT)]

UVP = 0.03
UPLIST = [find_percent_unc(v, UVP) for v in RIGHT]

# for i in range(len(UPLIST)):
#     print(f"{VOLUME[i]} +- {UPLIST[i] * VOLUME[i]/100}")

# avg volume
VAVG = sum(VOLUME) / len(VOLUME)
print("Average Volume:", VAVG)
print(sum(UPLIST) / 100)
print("ERROR:", sum(UPLIST) / 100 * VAVG)

