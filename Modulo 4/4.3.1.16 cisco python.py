from os  import  strerror

contador  = { chr ( ch ): 0  for  ch  in  range ( ord ( 'a' ), ord ( 'z' )+1 )}
nm_fl  =  input ( "¿Cual es el nombre del archivo?: " )
try :
    archivo  =  open ( nm_fl , "rt" )
    for  line  in  archivo :
        for  char  in  line :
            if  char.isalpha ():
                contador [ char.lower ()] +=  1
    archivo.close ()
    archivo = open(nm_fl+'.hist','wt')
    for  char  in  sorted(contador.keys(), key=lambda x: contador[x], reverse=True):
        cnt = contador[char]
        if cnt > 0:
            archivo.write(char +'-->' +str(contador[char])+ '\n')
    archivo.close()

except  IOError as e:
    print ( "Error: " , strerror ( e.errno ))
    exit()
