
def main():
    #Escribe tu código debajo de esta línea
    height = int(input("Enter triangle height: "))   
    
    for i in range(1,height+1):
        s=height-i
        print(" "*(espacios),"*"*i)


if __name__=='__main__':
    main()
