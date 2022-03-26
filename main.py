def fibonacci_recursiveFUNC(nth_POS):
    primitives = [1,2]
    if nth_POS in primitives:
        return nth_POS -1
    else:
        return fibonacci_recursiveFUNC(nth_POS-1) + fibonacci_recursiveFUNC(nth_POS -2)

def main():
    exitCONDITION = ['exit','quit', 'break']

    nth_Pos = input("Enter a valid nth POS value")
    while nth_Pos not in exitCONDITION:
        try:
            print(fibonacci_recursiveFUNC(int(nth_Pos)))
        except Exception:
            print("something went wrong")
        else:
            nth_Pos = input("Enter a valid nth POS value")

if __name__ == '__main__':
    main()