def main():
    #escribe tu código abajo de esta línea
    suma = 0
    num = 1
    contador = 0
 
    while num > 0:
        num = float(input())
        if num < 0:
            print(suma/contador)
        else:
            suma = suma + num
            contador = contador + 1

if __name__=='__main__':
    main()
