
def main():
    #Escribe tu código debajo de esta línea
    height = int(input("Enter triangle height: "))   
    
    for var in range(1, height+1):
        espacios = height - var
        print(' '*(espacios),'*' * var)


if __name__=='__main__':
    main()
