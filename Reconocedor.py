import ply.lex as lex
import ply.yacc as yacc
from graphviz import *

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

# Regex para reconocer tokens ---------------------------------
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

# CONSTRUCCION LEXER----------------------------------------------
lexer = lex.lex()

# ================================================================
# Comenzar con lo del parser

precedence = (
    ('right', 'IFF'),
    ('right', 'IMPLICACION'),
    ('left', 'DISYUNCION'),
    ('left', 'CONJUNCION'),
    ('right', 'NEGACION'),
)

def p_expresion_variable(p):
    'expresion : VARIABLE'
    p[0] = ('VAR', p[1])

def p_expresion_constante(p):
    'expresion : CONSTANTE'
    p[0] = ('CONST', p[1])

def p_expresion_negacion(p):
    'expresion : NEGACION expresion'
    p[0] = ('NOT', p[2])

def p_expresion_binaria(p):
    '''expresion : expresion CONJUNCION expresion
                  | expresion DISYUNCION expresion
                  | expresion IMPLICACION expresion
                  | expresion IFF expresion'''
    op_map = {
        'CONJUNCION': 'AND',
        'DISYUNCION': 'OR',
        'IMPLICACION': 'IMPLIES',
        'IFF': 'IFF',
    }
    token_type = p.slice[2].type
    p[0] = (op_map[token_type], p[1], p[3])

def p_expresion_parentesis(p):
    'expresion : IZQ_PAREN expresion DER_PAREN'
    p[0] = p[2]

def p_error(p):
    if p is None:
        print('fin de entrada inesperado')
    else:
        print(f"token inesperado {p.type!r}")

# CONSTRUCCION PARSER
parser = yacc.yacc()


def Arbol_Sintactico(expression, graph=None, parent=None):
    if graph is None:
        graph = Digraph()
    
    operadores_binarios = {'AND': '^', 'OR': '|', 'IMPLIES': '=>', 'IFF': '`<=>`'}
    variables_constantes = ['VAR', 'CONST']

    

    for i in range(len(expression)):  
        


        if expression[i] == 'NOT':
            padre = '~'
            operator = padre
            operand = expression[i+1]
            graph.node(str(id(expression)), label=operator)
            if parent is not None:
                graph.edge(str(id(parent)), str(id(expression)))
            Arbol_Sintactico(operand, graph, expression)
        elif expression[i] in operadores_binarios:
            operator = operadores_binarios[expression[i]]
            left_operand = expression[i+1]
            right_operand = expression[i-1]
            graph.node(str(id(expression)), label=operator)
            if parent is not None:
                graph.edge(str(id(parent)), str(id(expression)))
            Arbol_Sintactico(left_operand, graph, expression)
            Arbol_Sintactico(right_operand, graph, expression)
        elif expression[i] in variables_constantes:
            graph.node(str(id(expression)), label=expression[i+1])
            if parent is not None:
                graph.edge(str(id(parent)), str(id(expression)))

    return graph
    

def main():
    ruta = 'Pruebas.txt'

    with open(ruta, 'r') as archivo:
        for i, linea in enumerate(archivo):
            linea = linea.strip()
            if not linea:
                continue
            resultado = parser.parse(linea, lexer=lexer)
            print(f"{linea} -> {resultado} ")
            grafico = Arbol_Sintactico(resultado)
            grafico.render(f'arbol_{i}', format='png', cleanup=True)
            

main()
