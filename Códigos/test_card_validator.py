from card_validator import identificar_bandeira

def test_visa():
    assert identificar_bandeira('4111111111111111') == 'Visa'

def test_mastercard():
    assert identificar_bandeira('5555555555554444') == 'MasterCard'

def test_amex():
    assert identificar_bandeira('378282246310005') == 'American Express'

def test_discover():
    assert identificar_bandeira('6011111111111117') == 'Discover'

def test_jcb():
    assert identificar_bandeira('3530111333300000') == 'JCB'

def test_invalido():
    assert identificar_bandeira('1234567890123456') == 'Bandeira não reconhecida'
