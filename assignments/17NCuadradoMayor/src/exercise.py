
def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Escribe un numero : "))
    var = 1
    
    while var**2 <= num:
        var = var + 1
        if var**2 < num:
            pass
        elif var**2 > num:
            print(var)
    

if __name__=='__main__':
    main()
