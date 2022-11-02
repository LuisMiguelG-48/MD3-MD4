from os  import  strerror

contadores  = { chr ( ch ): 0  for  ch  in  range ( ord ( 'a' ), ord ( 'z' ) +  1 )}
f_name  =  input ( "Ingresa el nombre del archivo: " )
try :
    archivo  =  open ( f_name , "rt" )
    for  line  in  archivo :
        for  char  in  line :
            if  char.isalpha ():
                contadores [ char.lower ()] +=  1
    archivo.close ()
    for  char  in  contadores.keys ():
        c  =  contadores [ char ]
        if  c  >  0 :
            print ( char , '->' , c )
except  IOError as e:
    print ( "Error: " , strerror ( e.errno ))
