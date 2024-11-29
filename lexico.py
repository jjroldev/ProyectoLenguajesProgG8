import ply.yacc as yacc
import ply.lex as lex
from datetime import datetime
import os

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
    'continue': 'CONTINUE',
    'for': 'FOR',
    'import': 'IMPORT',
    'return': 'RETURN',
    'var': 'VAR',
    'Println': 'PRINTLN',
    'Print': 'PRINT',
    'Printf': 'PRINTF',
    'Sprint': 'SPRINT',
    'Sprintf': 'SPRINTF',
    'Sprintln': 'SPRINTLN',
    'main': 'MAIN',
    'append': 'APPEND',
    'error': 'ERROR',
    'Scan': 'SCAN',
    'Scanf':'SCANF',
    'Scanln':'SCANLN',
    'const':'CONST',
    'fmt':'FMT',
    'bool':'BOOL',
    'int':'INT',
    'float':'FLOAT',
    'uint':'UINT',
    'string':'STRING',
    'complex':'COMPLEX'
}

# Lista de nombres de tokens
tokens = (
             'VARIABLE',
             'BOOLV',
             'STRINGV',
             'INTV',
             'FLOATV',
             'UINTV',
             'COMPLEXV',
             'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
             'EQ', 'NEQ', 'LT', 'GT', 'LTOEQ', 'GTOEQ',
             'AND', 'OR', 'NOT', 'ASSIGN', 'PLUSA',
             'MINUSA', 'TIMESA', 'DIVA', 'MODA', 'EQUAL',
             'RCORCHETE',
             'LCORCHETE',
             'RLLAVE',
             'LLLAVE',
             'RPARENTESIS',
             'LPARENTESIS',
             'COLON',
             'DOT',
             'SEMICOLON',
             'COMMA',
             'DECLARE_ASSIGN',
             'INCREMENTO',
             'DECREMENTO',
             'BITWISEAND',
             'BITWISEOR',
             'BITWISEXOR',
             'BITWISECLEAR',
             'SHIFTLEFT',
             'SHIFTRIGHT',
             'BITWISEANDASSIGN',
             'BITWISEORASSIGN',
             'BITWISEXORASSIGN',
             'SHIFTLEFTASSIGN',
             'SHIFTRIGHTASSIGN',
             'ONELINECOMMENT',
             'MULTILINECOMMENT',
             'ARRAY',
             'SLICE',
             'SLICEV',
    'SALTO_LINEA',
    'TAB',
    'MAP',
    'ARRAYMOD',
    'FORMATO',
         ) + tuple(reserved.values())

# Expresiones regulares para operadores
t_FORMATO = r'(%d|%f|%s|%c|%t|%v|%x|%o|%q|%b|%p|%e|%g|%U)'
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
t_LCORCHETE = r'\['
t_RLLAVE = r'}'
t_LLLAVE = r'{'
t_RPARENTESIS = r'\)'
t_LPARENTESIS = r'\('
t_COLON = r':'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_COMMA = r','
t_DECLARE_ASSIGN = r':='
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'
t_BITWISEAND = r'&'
t_BITWISEOR = r'\|'
t_BITWISEXOR = r'\^'
t_BITWISECLEAR = r'&\^'
t_SHIFTLEFT = r'<<'
t_SHIFTRIGHT = r'>>'
t_BITWISEANDASSIGN = r'&='
t_BITWISEORASSIGN = r'\|='
t_BITWISEXORASSIGN = r'\^='
t_SHIFTLEFTASSIGN = r'<<='
t_SHIFTRIGHTASSIGN = r'>>='
t_SALTO_LINEA=r'\n'
t_TAB =r'\t'


# Definición de tokens para tipos básicos
def t_SLICEV(t):
    r'[a-zA-Z_]\w*\[\d?:\d?\]'
    return t

def t_ARRAYMOD(t):
    r'[a-zA-Z_]\w*\[\d+\]'
    return t

def t_ARRAY(t):
    r'\[\d+\](int|float|uint|string|bool|complex)'
    return t

def t_MAP(t):
    r'map\[(int|float|uint|string|bool|complex)\](int|float|uint|string|bool|complex)'
    return t

def t_SLICE(t):
    r'\[\](int|float|uint|string|bool|complex)'
    return t

def t_BOOLV(t):
    r'true|false'
    t.value = t.value == 'true'
    return t


def t_FLOATV(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_UINTV(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_INTV(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t


def t_STRINGV(t):
    r'"([^"\\]|\\["nt\\])*"'
    return t


def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_ONELINECOMMENT(t):
    r'//.*'
    return t


def t_MULTILINECOMMENT(t):
    r'\/\((?!\/\)[\s\S])\\/'
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


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
        return ""


def generar_log(tokens, usuario_git):
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    nombre_log = f"Logs/lexico-{usuario_git}-{fecha_hora}.txt"
    with open(nombre_log, 'w') as log:
        for token in tokens:
            log.write(f"{token}\n")
    print(f"Log generado: {nombre_log}")


def procesar_archivo(nombre_archivo, usuario_git):
    data = leer_archivo(nombre_archivo)
    if not data:
        return
    lexer.input(data)
    tokens = []
    # TOKENIZAR
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    generar_log(tokens, usuario_git)