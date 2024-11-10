import ply.yacc as yacc
import ply.lex as lex

# Palabras reservadas de Golang
reserved = {
    'break': 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'select': 'SELECT', 
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'else': 'ELSE',
    'goto': 'GOTO',
    'package': 'PACKAGE',
    'switch': 'SWITCH',
    'const': 'CONST',
    'fallthrough': 'FALLTHROUGH',
    'if': 'IF',
    'range': 'RANGE',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'import': 'IMPORT', 
    'return': 'RETURN',
    'var': 'VAR',
    'float64':'FLOAT64',
    'float32':'FLOAT32',
}


# Lista de nombres de tokens
tokens = (
    'VARIABLE',
    'BOOL',
    'STRING',
    'INT',
    'FLOAT',
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
    'EQ', 'NEQ', 'LT', 'GT', 'LTOEQ', 'GTOEQ',
    'AND', 'OR', 'NOT', 'ASSIGN', 'PLUSA',
    'MINUSA', 'TIMESA', 'DIVA', 'MODA',
    'RCORCHETE',
    'LCORCHETE',
    'RLLAVE',
    'LLLAVE',
    'RPARENTESIS',
    'LPARENTESIS',
    'COLON',
    'DOT',
    'SEMICOLON',
) + tuple(reserved.values())

# Expresiones regulares para operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTOEQ = r'<='
t_GTOEQ = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_PLUSA = r'\+='
t_MINUSA = r'-='
t_TIMESA = r'\*='
t_DIVA = r'/='
t_MODA = r'%='
t_RCORCHETE = r'\]'
t_LCORCHETE= r'\['
t_RLLAVE=r'}'
t_LLLAVE = r'{'
t_RPARENTESIS=r'\)'
t_LPARENTESIS = r'\('
t_COLON = r':'
t_DOT = r'\.'
t_SEMICOLON = r';'

# Definición de tokens para tipos básicos
def t_BOOL(t):
    r'true|false'
    t.value = t.value == 'true'
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value=float(t.value)
    return t

def t_INT(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\["nt\\])*"'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type=reserved.get(t.value,'VARIABLE')
    return t

# Salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba del lexer
data = '''
'''

# Entrada para el lexer
lexer.input(data)

# Tokenización
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
