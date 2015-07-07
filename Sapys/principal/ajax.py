#Aquí pondremos todas las funciones de AJAX que necesitemos
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

def multiplay(request, a, b):
    dajax = Dajax()
    result = int(a) + int(b)
    dajax.assign('#result', 'value', str(result))
    return dajax.json()

@dajaxice_register
def updatecombo(request, option):
    dajax = Dajax()
    options = [['SEVILLA'], ['CADIZ']]
    out = []
    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)
        
    dajax.assign('combo2', 'innerHTML', ''.join(out))
    return dajax.json()