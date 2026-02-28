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

