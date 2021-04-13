def main():
    fileVariable = open("Chibaku.txt", "r")
    fileVariable.read(1)
    fileVariable.read(2)
    fileVariable.read(3)

    print( fileVariable.read(5))
main()