if __name__ == '__main__':

    wheel1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}']
    wheel2 = ['2', '7', 'U', 'K', 'B', '3', 'F', '1', 'H', 'R', '6', 'L', 'C', 'V', '4', 'Q', 'E', 'D', 'X', 'W', '8', '}', 'N', 'O', 'A', 'P', '5', 'Z', 'I', 'G', 'T', 'Y', '0', '9', '{', '_', 'J', 'S', 'M']
    wheel3 = ['0', 'U', 'R', 'H', 'Q', 'S', '1', '7', 'B', '3', '{', 'Y', 'E', 'N', '6', 'T', 'M', 'K', '2', 'O', 'P', '8', 'X', '}', 'C', 'F', 'V', 'I', '4', '5', 'A', 'Z', 'G', '_', 'W', '9', 'J', 'L', 'D']
    wheel4 = ['J', 'B', '_', 'N', 'F', 'A', '4', '0', 'V', 'D', 'Y', '{', '1', 'C', '7', '6', '3', 'S', '2', 'R', 'M', 'L', 'I', '}', 'X', '5', 'Q', 'U', 'H', '8', 'W', 'O', 'T', '9', 'K', 'P', 'G', 'Z', 'E']

    print ('*'*80)
    print ('NOT SO ENIGMATIC, by NuclearFarmboy')
    print ('*'*80)

    flagClear = str(input("INPUT FLAG IN CLEARTEXT, GET ENCRYPTED FLAG: "))
    flagEncrypted = ""

    try:
        for letter in flagClear:
            wheel1Index = wheel1.index(letter)
            wheel2char = wheel2[wheel1Index]
            wheel3Index = wheel3.index(wheel2char)
            wheel4char = wheel4[wheel3Index]
            flagEncrypted += wheel4char
            wheel2 = [wheel2[-1]] + wheel2[:-1]
            wheel3 = wheel3[1:] + [wheel3[0]]
            wheel4 = [wheel4[-1]] + wheel4[:-1]
    except:
        print('ERROR FOUND INVALID CHARACTER')
        exit()

    print('FINAL CLEAR FLAG: ', flagClear)
    print('FINAL ENCRYPTED FLAG: ', flagEncrypted)

