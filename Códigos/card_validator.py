import re

def identificar_bandeira(numero: str) -> str:
    numero = re.sub(r'\D', '', numero)

    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', numero):
        return 'Visa'
    elif re.match(r'^5[1-5][0-9]{14}$', numero):
        return 'MasterCard'
    elif re.match(r'^3[47][0-9]{13}$', numero):
        return 'American Express'
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', numero):
        return 'Discover'
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', numero):
        return 'JCB'
    else:
        return 'Bandeira não reconhecida'
