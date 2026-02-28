#Secret Spy:
def Secret_Spy():
    import re
    y = input()
    x = re.findall(r"\d", y)
    t = 0
    for item in x:
        t += int(item)
    print(t)

#Secret Spy2:
def Secret_Spy2():
    import re
    x = input()
    #\d+ looks for connected numbers
    m = re.findall(r"\d+", x)
    t = 0
    for item in m:
        t += int(item)
    print(t)

#Pony Counter
def pony():
    import sys
    inp = sys.stdin.read().split("\n")
    pon = int(inp[0])*(1+float(inp[2]))*int(inp[3])
    print(f"At the current rate of growth there will be {int(pon)} ponies in 284 years.")
    if int(inp[1]) >= pon:
        print("Celestia won't need to add space yet!")
    else:
        space = int(inp[1])-pon
        print(f"Celestia will need to add space for at least {space} ponies!")