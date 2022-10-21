# Entrega 1 #
En esta primera entrega, vamos desarrollar un sencillo algoritmo de **descompresión** sobre el genoma de la levadura (*Saccharomyces cerevisiae*). Para ello contaremos con un fichero llamado *sacCer3cmp.txt* que contendrá secuencias de nucleótidos en un formato que se detallará en breve. 

Un nucleótido es la estructura fundamental básica de los ácidos nucleicos (ARN y ADN) y estarán representados por las letras A (Adenina), G (Guanina), C (Citosina) y T (Timina). Nuestro fichero original, estará formado por líneas de la forma:

        CCACACCACACCCACACACCCACACACCACACCACACACCACACCACACC
        CACACACACACATCCTAACACTACCCTAACACAGCCCTAATCTAACCCTG
        GCCAACCTGTCTCTCAACTTACCCTCCATTACCCTGCCTCCACTCGTTAC

Nuestro fichero comprimido, estará formado por líneas de la forma:

        2CACA2CACA3CACACA3CACACA2CACA2CACACA2CACA2CACA2C
        CACACACACACAT2CT2ACACTA3CT2ACACAG3CT2ATCT2A3CTG
        G2C2A2CTGTCTCTC2AC2TA3CT2CA2TA3CTG2CT2CACTCG2TAC

Aunque parezca un poco extraño, la idea detrás de esta técnica es muy sencilla. Fijémonos en esta secuencia pequeña de ADN:

        AAAAAAAAAACCTGG

Observará que la A se repite 10 veces al principio, y que la C y la G, se repiten dos veces respectivamente.

Una forma de ahorrar espacio (de comprimir) estas secuencias, podría ser anteponiendo a cada serie, el número de veces que aparece un nucleótido. Así, en el ejemplo de arriba, obtendríamos:

        10A2CT2G (diez veces A, dos veces C, una vez T, y 2 veces G)

Observaciones:
- En el caso en el que solo haya una repetición, no se antepone el número (el caso de T en el ejemplo).
- El número de repeticiones puede tener más de un dígito.

Complete y pruebe las funciones cuya cabecera y descripción se proporcionan, para descomprimr un fichero de nucleótidos en el formato descrito anteriormente. Para ello, deberá recorrer el fichero comprimido, y para cada línea deberá recuperar el formato original. Cada línea descomprimida, deberá escribirse en otro fichero que almacenará el resultado.