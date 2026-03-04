#converts from base start to base final. 
def convertbase(string, bStart, bFinal):
    alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
    decimal = int(string, bStart)
    if decimal == 0: return "0"
    result = ""
    while decimal:
        result = alpha[decimal % bFinal] + result
        decimal //= bFinal
    return result

if __name__ == "__main__":
    print(convertbase("code", 36, 35))
    #converts from base 8 to base 10 for ex
    print(convertbase("357", 8, 10))
