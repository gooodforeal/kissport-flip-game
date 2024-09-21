import random


def flip(print, input, use_random=True):
    B1 = 50  # Total number of turns
    P = [0.5] * 16  # Probabilities for each of the 16 possible response patterns
    X = [0] * 4  # History of last 4 responses (0 for 'N', 1 for 'Y')
    F1 = 0.8  # Old-memory factor
    F2 = 0.3  # Randomness factor
    S1 = 0  # Number of correct guesses
    S2 = 0  # Total number of guesses
    A = ""  # Special character for correct guess

    # Explanation
    print(" " * 25 + "FLIP")
    print(" " * 18 + "CREATIVE COMPUTING")
    print(" " * 16 + "MORRISTOWN NEW JERSEY\n\n\n")
    if input("EXPLANATION (Y OR N)?: ").upper() == "Y":
        print("ON EACH TURN, YOU GUESS YES <'Y'> OR NO <'N'>.")
        print("ONLY ONE IS CORRECT, AND THE PROGRAM HAS DECIDED")
        print("WHICH ONE, BEFORE YOU MAKE YOUR GUESS. AT FIRST")
        print("YOUR ODDS ARE 50%, PURE CHANCE. BUT LATER THE")
        print("PROGRAM WILL TRY TO TAKE ADVANTAGE OF PATTERNS")
        print("IN YOUR GUESSING.")
        print("\nGAME ENDS AFTER", B1, "TURNS; A SCORE OF", int(B1 / 2 - 1), "OR MORE")
        print("IS GOOD. PROGRAM TELLS WHEN YOU WIN A TURN,",)
        print("BY TYPING AN ASTERISK ('*') AS THE FIRST")
        print("CHARACTER OF THE FOLLOWING LINE.")
        print("\n\n")

    # Game loop
    print("BEGIN.")
    print(" ")
    if use_random:
        for i in range(4):
            if random.random() < 0.5:
                X[i] = 1
            else:
                X[i] = 0
        while S2 < B1:
            # Calculate estimated probability of guessing 'Y'
            I9 = 8 * X[3] + 4 * X[2] + 2 * X[1] + X[0] + 1
            Z1 = P[I9 - 1]  # Adjust index to match Python indexing

            # Adjust probability based on randomness factor
            Z2 = Z1
            if Z2 != 0.5:
                if Z2 > 0.5:
                    Z2 = Z2 * F2 + 1 * (1 - F2)
                else:
                    Z2 = Z2 * F2 + 0 * (1 - F2)
            else:
                Z2 = random.random()

            # Determine the program's response (Z5)
            Z5 = 0
            if random.random() < Z2:
                Z5 = 1

            # Get player's input (Z3)
            print(A)
            H = input("? ").upper()
            if H == "Y":
                Z3 = 1
            elif H == "N":
                Z3 = 0
            else:
                print("ERROR, MUST BE  Y  OR  N  .")
                continue

            # Update scores and flag for correct guess
            S2 += 1
            if Z3 == Z5:
                A = "*"
                S1 += 1
            else:
                A = " "

            # Update response history (X)
            X[0] = X[1]
            X[1] = X[2]
            X[2] = X[3]
            X[3] = Z3

            # Update probability based on previous response patterns
            P[I9 - 1] = F1 * P[I9 - 1] + (1 - F1) * Z3
    else:
        random_var = 0.49
        for i in range(4):
            if random_var < 0.5:
                X[i] = 0
            else:
                X[i] = 1
        while S2 < B1:
            # Calculate estimated probability of guessing 'Y'
            I9 = 8 * X[3] + 4 * X[2] + 2 * X[1] + X[0] + 1
            Z1 = P[I9 - 1]  # Adjust index to match Python indexing

            # Adjust probability based on randomness factor
            Z2 = Z1
            if Z2 != 0.5:
                if Z2 > 0.5:
                    Z2 = Z2 * F2 + 1 * (1 - F2)
                else:
                    Z2 = Z2 * F2 + 0 * (1 - F2)
            else:
                Z2 = random_var

            # Determine the program's response (Z5)
            Z5 = 0
            if not random_var < Z2:
                Z5 = 1

            # Get player's input (Z3)
            print(A)
            H = input("? ").upper()
            if H == "Y":
                Z3 = 1
            elif H == "N":
                Z3 = 0
            else:
                print("ERROR, MUST BE  Y  OR  N  .")
                A = ""
                continue

            # Update scores and flag for correct guess
            S2 += 1
            if Z3 == Z5:
                A = "*"
                S1 += 1
            else:
                A = " "

            # Update response history (X)
            X[0] = X[1]
            X[1] = X[2]
            X[2] = X[3]
            X[3] = Z3

            # Update probability based on previous response patterns
            P[I9 - 1] = F1 * P[I9 - 1] + (1 - F1) * Z3

    # End of game
    print(A)
    print("\nEND OF GAME.\nYOU GOT", S1, "OUT OF", S2, "CORRECT.")
    print("\n\nPLAY AGAIN (Y OR N)?: ")
    if input().upper() == "Y":
        flip(print, input)  # Recursive call to start a new game


if __name__ == "__main__":
    flip(print, input)
