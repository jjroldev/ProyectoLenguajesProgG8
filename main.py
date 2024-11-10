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
    'var': 'VAR'
}


# Lista de nombres de tokens
tokens = (
) + tuple(reserved.values())

# Expresiones regulares para operadores


# Definición de tokens para tipos básicos


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
