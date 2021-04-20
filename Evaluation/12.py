def Root(n):
    lastGuess = 1.0
    while True:
        nextGuess = float(lastGuess+float(n/lastGuess))/2.0
        if abs(lastGuess-nextGuess) < 0.0001:
            return nextGuess
        else:
            lastGuess = nextGuess
            nextGuess = float(lastGuess+float(n/lastGuess))/2.0
            if abs(lastGuess-nextGuess) < 0.0001:
                return nextGuess
