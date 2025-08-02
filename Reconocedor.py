import ply.lex as lexer

# Declarar todos los tokens que vamos a usar para el alfabeto
tokens = (
    'VARIABLE', # Todas las proposicionales
    'CONSTANTE', # 0,1
    'NEGACION', #~
    'CONJUNCION', #^
    'DISYUNCION', #o
    'IMPLICACION', # =>
    'IFF', # SI y SOLO SI, <=>
    'IZQ_PAREN', # (
    'DER_PAREN', # )
)

# Regex para reconocer tokens
def t_VARIABLE(t):
    r'[pqrstuvwxyz]'
    return t

def t_CONSTANTE(t):
    r'[01]'
    return t

t_NEGACION = r'~'

t_CONJUNCION = r'\^'

t_DISYUNCION = r'o'

def t_IMPLICACION(t):
    r'=>'
    return t

def t_IFF(t):
    r'<=>'
    return t

t_IZQ_PAREN = r'\('

t_DER_PAREN = r'\)'

t_ignore = ' \t' # solo para pasar de largo si hay espacios

# Si se topa con un caracter que no es de un token
# de momento solo nos lo vamos a saltar para que lo tomen en cuenta
def t_error(t):
    print(f"Caracter no valido: {t.value[0]!r}")
    t.lexer.skip(1)

# CONSTRUCCION LEXER
lexer = lexer.lex()