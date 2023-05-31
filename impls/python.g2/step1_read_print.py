# step 0 of MAL
import printer
import reader
import readline

def READ(*x):
    return reader.read_str(x[0])

def EVAL(*x):
    return x[0]

def PRINT(*x):
    return printer.pr_str(x[0])

def rep(*x):
    return PRINT(EVAL(READ(*x)))

if __name__ == '__main__':
    while True:
        line = input("user> ")
        readline.add_history(line)
        print(rep(line))

