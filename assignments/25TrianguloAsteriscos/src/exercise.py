
def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Enter triangle height: "))
    var = 1
    espacios = num - 2
    
    while  num >= var:
        print(' '*(espacios),'*' * var)
        var = var + 1
        espacios = espacios -1
    


if __name__=='__main__':
    main()
