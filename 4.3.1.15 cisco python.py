from os  import  strerror

contador  = { chr ( ch ): 0  for  ch  in  range ( ord ( 'a' ), ord ( 'z' ) +  1 )}
nm_fl  =  input ( "¿Cual es el nombre del archivo?: " )
try :
    archivo  =  open ( nm_fl , "rt" )
    for  line  in  archivo :
        for  char  in  line :
            if  char.isalpha ():
                contador [ char.lower ()] +=  1
    archivo.close ()
    for  char  in  contador.keys ():
        cont  =  contador [ char ]
        if  cont  >  0 :
            print ( char , '->' , cont )
except  IOError as e:
    print ( "Error: " , strerror ( e.errno ))

