email=input("introduce tu email,por favor: ")

arroba=email.count("@")

while True:
    #if(arroba!=1 or email[0]=="@" or email[-1]=="@"):
    if(arroba!=1 or email.rfind("@")==(len(email)-1) or email.find("@")==0 ):
    
        print("direccion invalida")
    else:
    
        break

    email=input("introduce tu email,por favor: ")



print("el mail es correcto")