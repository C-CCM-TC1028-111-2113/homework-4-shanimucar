def main():
    #escribe tu código abajo de esta línea
    num = int(input())
    contador = 0
 
    while contador < num:
        contador = contador + 1
        if contador % 2 == 0:
            print(contador, '-#')
        elif contador % 2 != 0:
            print(contador, '-%')
   


if __name__=='__main__':   
    main()
