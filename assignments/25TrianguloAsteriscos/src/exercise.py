
def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Enter triangle height: "))
    var = 1
    espacios = num - 1
    
    while  num >= var:
        if num != espacios:
            print(' '*(espacios),'*' * var)
            var = var + 1
            espacios = espacios -1
        elif num == espacios:
            var = var + 1
            print('*' * var)
        
    


if __name__=='__main__':
    main()
