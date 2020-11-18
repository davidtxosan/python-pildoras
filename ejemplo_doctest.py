def compruebaMail(mailUsuario):
    """
    la función compruebaMail evalúa un mail
    recibido en busca de la @.Si tiene una @
    es correcto,si tiene mas de una @ o si la @ está al final
    entonces será incorrecto.
    
    >>> compruebaMail('dsjaramillo@hotmail.com')
    True

    >>> compruebaMail('dsjaramillo.hotmail.com')
    False

    >>> compruebaMail('ds@jaramillo@hotmail.com')
    False

    >>> compruebaMail('ds@jaramillo.hotmail.com@')
    False

    """
    
    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1)or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()