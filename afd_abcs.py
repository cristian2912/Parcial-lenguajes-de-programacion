
def acepta(s):
    state = 'q0'  # inicio
    i = 0
    while i < len(s):
        ch = s[i]
        if state == 'q0':
            if ch == 'a':
                state = 'q0'
            elif ch == 'b':
                state = 'q1'
            elif ch == 'c':
                state = 'q2'
            else:
                return False  # no permitido
        elif state == 'q1':
            if ch == 'b':
                state = 'q1'
            elif ch == 'c':
                state = 'q2'
            else:
                return False
        elif state == 'q2':
            if ch == 'c':
                state = 'q2'
            else:
                return False
        i += 1
    return state in ('q0', 'q1', 'q2')


def main():
    try:
        while True:
            s = input().strip()  # lee una linea
            if acepta(s):
                print("ACEPTADA")
            else:
                print("RECHAZADA")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
