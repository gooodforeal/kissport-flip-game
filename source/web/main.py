import random


def flip(print, input, rnd=True):
    turns = 50
    score_target = int(turns / 2 - 1)
    score = 0
    correct = 0
    probabilities = [0.5] * 16
    responses = [0] * 4
    memory_factor = 0.8
    randomness_factor = 0.3
    print(" " * 25 + "FLIP")
    print(" " * 18 + "CREATIVE COMPUTING")
    print(" " * 16 + "MORRISTOWN NEW JERSEY")
    print("\n\n")
    explanation = input("EXPLANATION (Y OR N)? ")
    if explanation.upper() == "Y":
        print("ON EACH TURN, YOU GUESS YES <'Y'> OR NO <'N'>.")
        print("ONLY ONE IS CORRECT, AND THE PROGRAM HAS DECIDED")
        print("WHICH ONE, BEFORE YOU MAKE YOUR GUESS. AT FIRST")
        print("YOUR ODDS ARE 50%, PURE CHANCE. BUT LATER THE")
        print("PROGRAM WILL TRY TO TAKE ADVANTAGE OF PATTERNS")
        print("IN YOUR GUESSING.")
        print("\n")
        print(f"GAME ENDS AFTER {turns} TURNS; A SCORE OF {score_target} OR MORE")
        print("IS GOOD. PROGRAM TELLS WHEN YOU WIN A TURN,")
        print("BY TYPING AN ASTERISK ('*') AS THE FIRST")
        print("CHARACTER OF THE FOLLOWING LINE.")
    print("BEGIN.")
    for i in range(4):
        if random.random() < 0.5:
            responses[i] = 1
    print(" ")
    while turns > 0:
        probability_index = 8 * responses[3] + 4 * responses[2] + 2 * responses[1] + responses[0] + 1
        estimated_probability = probabilities[probability_index - 1]
        adjusted_probability = estimated_probability
        if adjusted_probability != 0.5:
            adjusted_probability = (adjusted_probability * randomness_factor) + (
                0 if adjusted_probability < 0.5 else 1) * (1 - randomness_factor)
        program_answer = 1 if random.random() < adjusted_probability else 0
        guess = input("? ")
        while guess.upper() not in ("Y", "N"):
            print("ERROR, MUST BE  Y  OR  N  .")
            guess = input(" ")
        if guess.upper() == "Y":
            player_answer = 1
        else:
            player_answer = 0
        if player_answer == program_answer:
            correct += 1
            print("*")
        else:
            print(" ")
        responses[0] = responses[2]
        responses[1] = responses[3]
        responses[2] = player_answer
        responses[3] = program_answer
        probabilities[probability_index - 1] = memory_factor * probabilities[probability_index - 1] + (
                    1 - memory_factor) * player_answer
        turns -= 1
        score += 1
    print(f"\nEND OF GAME.\nYOU GOT {correct} OUT OF {score} CORRECT.\n\n")
    play_again = input("PLAY AGAIN (Y OR N)? ")
    if play_again.upper() == "Y":
        flip(print, input)


if __name__ == "__main__":
    flip(print, input)
