from flask import Flask, render_template, request
import random

app = Flask(__name__)

turns = 50
score_target = int(turns / 2 - 1)
correct = 0
probabilities = [0.5] * 16
responses = [0] * 4
memory_factor = 0.8
randomness_factor = 0.3
explanation = False
game_started = False
game_over = False
result = ""
begin = False


@app.route('/', methods=['GET', 'POST'])
def flip():
    global turns
    global score_target
    global correct
    global probabilities
    global responses
    global memory_factor
    global randomness_factor
    global explanation
    global game_started
    global game_over
    global result
    global begin

    if request.method == 'POST':
        if 'explanation' in request.form and request.form['explanation'].upper() == "Y":
            explanation = True
        elif 'explanation' in request.form and request.form['explanation'].upper() == "N":
            explanation = False
            game_started = True
        elif "begin" in request.form:
            game_started = True
        elif 'guess' in request.form:
            guess = request.form['guess'].upper()
            if guess not in ("Y", "N"):
                result = "ERROR, MUST BE  Y  OR  N  ."
            else:
                probability_index = 8 * responses[3] + 4 * responses[2] + 2 * responses[1] + responses[0] + 1
                estimated_probability = probabilities[probability_index - 1]
                # Adjust the probability based on randomness and memory
                adjusted_probability = estimated_probability
                if adjusted_probability != 0.5:
                    adjusted_probability = (adjusted_probability * randomness_factor) + (
                        0 if adjusted_probability < 0.5 else 1) * (1 - randomness_factor)
                program_answer = 1 if random.random() < adjusted_probability else 0
                if guess == "Y":
                    player_answer = 1
                else:
                    player_answer = 0
                if player_answer == program_answer:
                    correct += 1
                    result = "*"
                else:
                    result = " "
                responses[0] = responses[2]
                responses[1] = responses[3]
                responses[2] = player_answer
                responses[3] = program_answer
                probabilities[probability_index - 1] = memory_factor * probabilities[probability_index - 1] + (
                        1 - memory_factor) * player_answer
                turns -= 1
                if turns == 0:
                    game_over = True
                    result = f"\nEND OF GAME.\nYOU GOT {correct} OUT OF 50 CORRECT.\n\n"

    return render_template('flip.html',
                           explanation=explanation,
                           game_started=game_started,
                           game_over=game_over,
                           result=result,
                           turns=turns,
                           score_target=score_target)


if __name__ == "__main__":
    app.run(debug=True)
