import subprocess
import os


def process(command):
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )


def expect(process, pattern):
    buffer = ''
    while True:
        buffer += process.stdout.read(1).decode()
        if buffer.endswith(pattern):
            return buffer


def write(process, text):
    process.stdin.write(f'{text}\n'.encode())
    process.stdin.flush()
    return text


def test():
    print("Launching processes")
    try:
        bas = process('source-nornd.bas')
        py = process('python gamenornd.py')

        # Проверка, что программы печатают в консоль (stdout) одно и то же:
        expected_greedings = '''
                         FLIP
                  CREATIVE COMPUTING
                MORRISTOWN NEW JERSEY



EXPLANATION (Y OR N)? 
'''
        print("expecting answers...")
        expect(bas, expected_greedings)
        expect(py, expected_greedings)
        # Печать ответа пользователя в stdin:
        print("sending keys...")
        write(bas, 'Y')
        write(py, 'Y')
        instruction = '''
ON EACH TURN, YOU GUESS YES <'Y'> OR NO <'N'>.
ONLY ONE IS CORRECT, AND THE PROGRAM HAS DECIDED
WHICH ONE, BEFORE YOU MAKE YOUR GUESS. AT FIRST
YOUR ODDS ARE 50%, PURE CHANCE. BUT LATER THE
PROGRAM WILL TRY TO TAKE ADVANTAGE OF PATTERNS
IN YOUR GUESSING.

GAME ENDS AFTER  50  TURNS; A SCORE OF  24  OR MORE
IS GOOD. PROGRAM TELLS WHEN YOU WIN A TURN,
BY TYPING AN ASTERISK ('*') AS THE FIRST
CHARACTER OF THE FOLLOWING LINE.



BEGIN.
 Y 
'''
        print("expecting results")
        expect(bas, instruction)
        expect(py, instruction)
    except Exception as ex:
        print(ex)


test()
