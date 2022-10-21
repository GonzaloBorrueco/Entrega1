def descomprime_fichero(origen, destino):
    """función que descomprime un fichero de nucleótidos comprimido y guarda el resultado
    en otro fichero
    Args:
        origen (str): ruta hacia el fichero comprimido
        destino (str): ruta hacia el fichero donde se guardarán los datos originales
        archivo_origen (function): función para abrir el archivo de origen en formato lectura
        archivo_destino (function): función para abrir el archivo de origen en formato escritura
        txt (str): línea de texto que representa una secuencia de nucleótidos en formato comprimido
        lineas (function): función para leer cada línea del archivo de origen
    """
    archivo_origen = open(origen, 'r')                  #Abrimos el archivo de origen en modo lectura
    archivo_destino = open(destino, 'w')                #Abrimos el archivo de destino en modo escritura
    lineas = archivo_origen.readlines()                 #Leemos cada línea del archivo de origen y las metemos en una variable
    for txt in lineas:                                  #Por cada línea del fichero:
      archivo_destino.writelines(descomprime(txt))          #Llamamos a la función "descomprime" para cada línea del archivo. 
                                                            #El resultado de la función (la línea descomprimida) se guarda en el archivo de destino

def descomprime(txt):
    """función auxiliar que descomprime una línea del fichero comprimido y la devuelve en su formato original

    Args:
        txt (str): línea de texto que representa una secuencia de nucleótidos en formato comprimido
        digito (str): línea de texto que representa los dígitos de los números correspondiente a cada nucleótido
        numero (int): número entero que representa el conjunto de dígitos en formato entero correspondiente a las veces que se repite cada nucleótido
        letra (str): línea de texto que representa la letra correspondiente a cada nucleótido
    Returns:
        secuencia (str): secuencia de nucleótidos
    """
    secuencia=""                                        #Se define "secuencia" como una cadena de texto vacía
    i=0                                                 #Se utiliza la variable "i" como índice para la cadena "secuencia"
    
    while i < len(txt):                                 #Bucle while para que el índice recorra toda la línea "txt", sin pasarse
        digito=""                                       #Se define "digito" como una cadena de texto vacía
        
        if txt[i].isdigit():                            #Bucle if para comprobar si el caracter es un número
            while i < len(txt) and txt[i].isdigit():        #Bucle while para que, mientras el índice se encuentre dentro del rango de la línea,  
                digito+=txt[i]                                  #se añadan los dígitos a la cadena de texto "digito"
                i+=1                                            #y se incremente en 1 la cuenta del índice para pasar al siguiente caracter
            
            numero=int(digito)                              #Fuera del while, se convierte en un número entero la cadena "digito"
            letra=txt[i]                                    #Al haber acabado el bucle, se asume que el siguiente caracter es una letra
            secuencia+=letra*(numero-1)                     #por lo que se añade a la cadena "secuencia" X veces (siendo X el número anterior menos uno porque la letra entra a parte)

        else:
            while i < len(txt) and txt[i].isdigit() == False:   #Bucle while para comprobar si los caracteres siguientes NO son números
                letra=txt[i]                                        #Se guarda la letra en la variable "letra"
                i+=1                                                #Se incrementa en 1 la cuenta del índice para pasar al siguiente caracter
                secuencia+=letra                                    #Se guarda la letra en la secuencia
            
    return(secuencia)                   #Devuelve la cadena de texto "secuencia"


def check_Ok(descomprimido, original):
    """función que comprueba si el fichero generado por nosotros coincide con el original

    Args:
        descomprimido (str): ruta hacia el fichero descomprimido por nosotros
        original (str): ruta hacia el fichero original

    Returns:
        bool: Devuelve True si el fichero descomprimido coincide con el original
    """
    ok=True
    fd=open(descomprimido, encoding='utf-8')
    fo=open(original, encoding='utf-8')
    for linea1,linea2 in zip(fd,fo):
        ok=linea1==linea2
        if not ok:
            break
    fd.close()
    fo.close()
    return ok

######################################### Test ################################################
if __name__ == '__main__':
    '''
    Realice las siguientes pruebas:
    1.- descomprima el fichero 'sacCer3cmp.txt' y guardelo en el fichero 'sacCer3descmp.txt' 
        (ambos en la ruta de la carpeta 'data')
    2.- Compruebe que el algoritmo funciona usando el método 'ckeck_Ok', que toma como parámetros
        la ruta hacia el fichero que usted ha generado ('sacCer3descmp.txt'), y la ruta hacia 
        el fichero original ('sacCer3.txt')
    '''
#1
descomprime_fichero("data/sacCer3cmp.txt","data/sacCer3descmp.txt")

#2
print(check_Ok("data/sacCer3descmp.txt","data/sacCer3.txt"))
