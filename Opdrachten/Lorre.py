n = input()
n = int(n)
for i in range(n):
    zin = input()
    woorden = zin.split()
    if len(woorden) > 4:
        print("Crackers!")
    else:
        print(zin + " krAh!")
