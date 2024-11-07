# this module demonstrates defensive programming using mypy

def woof(n:int) -> str:        
        return "WOOF!\n"*n
    

def main() -> None:
    times:int = int(input('woof how many times? '))
    bark = woof(times)
    print("GOOOOOOOOOOOOOOOO DAWGS. SIC 'EM", bark, sep='\n')
    
if __name__ == "__main__":
    main()