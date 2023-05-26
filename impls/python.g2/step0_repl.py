# step 0 of MAL
import readline

def READ(*x):
    return x[0]

def EVAL(*x):
    return x[0]

def PRINT(*x):
    return x[0]

def rep(*x):
    return PRINT(EVAL(READ(*x)))

if __name__ == '__main__':
    while True:
        line = input("user> ")
        readline.add_history(line)
        print(rep(line))

