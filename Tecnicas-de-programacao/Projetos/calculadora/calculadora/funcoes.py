def soma(a, b):
    '''
    args:
        a: (int, float)
        b: (int, float)
    return:
        a + b (int,float)
    '''

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f'O input "a" e "b" devem ser um número, recebido {a} ({type(a)}), {b} ({type(b)})') 

def subtracao(a, b):
        '''
    args:
        a: (int, float)
        b: (int, float)
    return:
        a + b (int,float)
    '''

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError(f'O input "a" e "b" devem ser um número, recebido {a} ({type(a)}), {b} ({type(b)})') 