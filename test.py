import subprocess


def process(command):
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )


def expect(proc, pattern):
    pattern = pattern.strip("\n")
    buffer = ""
    while True:
        buffer += proc.stdout.read(1).decode()
        if pattern.endswith(buffer):
            return True


def write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    proc.stdin.flush()
    return text


def test():
    print("Launching processes")
    try:
        bas = process('source-nornd.bas')
        py = process('python gamenornd.py')

        # Проверка, что программы печатают в консоль (stdout) одно и то же:
        expected_greetings = '''
                         FLIP
                  CREATIVE COMPUTING
                MORRISTOWN NEW JERSEY



EXPLANATION (Y OR N)? 
'''
        print("expecting answers...")
        expect(bas, expected_greetings)
        expect(py, expected_greetings)
        print("[+] TEST 1 - PASSED")
        # Печать ответа пользователя в stdin:
        print("sending keys...")
        write(bas, 'Y')
        write(py, 'Y')
        print("[+] KEYS SENT")
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
 ? 
'''
        print("expecting results")
        expect(bas, instruction)
        expect(py, instruction)
        print("[+] TEST 2 - PASSED")

        print("sending keys...")
        write(bas, 'Y')
        write(py, 'Y')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "*? ")
        expect(py, "*? ")
        print("[+] TEST 3 - PASSED")

        print("sending keys...")
        write(bas, 'Y')
        write(py, 'Y')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "*? ")
        expect(py, "*? ")
        print("[+] TEST 4 - PASSED")

        print("sending keys...")
        write(bas, 'Y')
        write(py, 'Y')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "*? ")
        expect(py, "*? ")
        print("[+] TEST 5 - PASSED")

        print("sending keys...")
        write(bas, 'N')
        write(py, 'N')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, " ? ")
        expect(py, " ? ")
        print("[+] TEST 6 - PASSED")

        print("sending keys...")
        write(bas, 'N')
        write(py, 'N')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, " ? ")
        expect(py, " ? ")
        print("[+] TEST 7 - PASSED")

        print("sending keys...")
        write(bas, 'b')
        write(py, 'b')
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "ERROR, MUST BE Y OR N .\n? ")
        expect(py, "ERROR, MUST BE Y OR N .\n? ")
        print("[+] TEST 8 - PASSED")
    except Exception as ex:
        print(ex)


test()
