def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }
    tempStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tempStr += bcolors[nuc] + nuc
        else:
            tempStr += bcolors['reset'] + nuc

    return tempStr + '\033[0;0m'