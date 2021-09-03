
def main():
    #escribe tu código abajo de esta línea
    index = int(input("Enter the index: "))
    a = 0
    b = 1
    n = 1
    suma = 0
    
    while n <= index:
        n = n + 1
        a = b
        b = suma
        suma = a + b
        
    print(suma)

if __name__=='__main__':
    main()
