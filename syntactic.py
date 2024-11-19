import ply.yacc as yacc
from datetime import datetime
import os
from main import tokens

# Diccionario de variables
variables = {}

# Reglas de precedencia para operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ', 'LT', 'GT', 'LTOEQ', 'GTOEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'),
    ('right', 'NOT'),
)

# Obtener fecha y usuario para logs
fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
usuario_git = "JoseMurillo2711"

# Crear carpeta de logs si no existe
if not os.path.exists("Logs"):
    os.makedirs("Logs")

# Nombre del archivo de log
log_filename = f"Logs/sintactico-{usuario_git}-{fecha_hora}.txt"

# Reglas gramaticales
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_statement(p):
    '''statement : print_statement
                 | input_statement
                 | expression_statement
                 | variable_declaration
                 | variable_assignment
                 | data_structure_declaration'''
    p[0] = p[1]

# Declaración de variables con VAR y :=
def p_variable_declaration(p):
    '''variable_declaration : VAR VARIABLE TYPE EQUAL expression
                            | VARIABLE DECLARE_ASSIGN expression'''
    if len(p) == 6:  # var resultado int = 5
        p[0] = ('var_declaration', p[2], p[3], p[5])
    else:  # resultado := 5
        p[0] = ('declare_assign', p[1], p[3])

# Asignación de valores a variables existentes
def p_variable_assignment(p):
    '''variable_assignment : VARIABLE ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_print_statement(p):
    '''print_statement : PRINTLN LPARENTESIS expression_list RPARENTESIS
                       | PRINT LPARENTESIS expression_list RPARENTESIS'''
    p[0] = ('print', p[3])

def p_input_statement(p):
    '''input_statement : VARIABLE ASSIGN SCAN LPARENTESIS RPARENTESIS'''
    p[0] = ('input', p[1])

def p_expression_statement(p):
    '''expression_statement : expression'''
    p[0] = p[1]

def p_data_structure_declaration(p):
    '''data_structure_declaration : VAR VARIABLE ASSIGN LCORCHETE RCORCHETE ARRAY'''
    p[0] = ('array', p[2])

# Expresiones
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression GT expression
                  | expression LTOEQ expression
                  | expression GTOEQ expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_paren(p):
    '''expression : LPARENTESIS expression RPARENTESIS'''
    p[0] = p[2]

def p_expression_unary(p):
    '''expression : MINUS expression %prec NOT
                  | NOT expression'''
    p[0] = (p[1], p[2])

def p_expression_term(p):
    '''expression : INT
                  | FLOAT
                  | STRING
                  | BOOL
                  | VARIABLE'''
    p[0] = p[1]

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

# Manejo de errores
def p_error(p):
    if p:
        error_message = f"Syntax error at token {p.type}, line {p.lineno}"
    else:
        error_message = "Syntax error at EOF"
    log_result(error_message, is_error=True)
    print(error_message)

# Log resultados y errores
def log_result(message, is_error=False):
    """Registrar resultados y errores en el archivo de logs."""
    log_type = "ERROR" if is_error else "RESULT"
    with open(log_filename, 'a') as log_file:
        log_file.write(f"[{log_type}] {message}\n")
    if is_error:
        print(f"Error log generado: {log_filename}")
    else:
        print(f"Resultado log generado: {log_filename}")

# Construcción del parser
parser = yacc.yacc()

# Probar el parser
def test_parser():
    while True:
        try:
            s = input('GoParser > ')
        except EOFError:
            break
        if not s:
            continue
        try:
            result = parser.parse(s)
            log_result(str(result))  # Registrar el resultado
            print(result)
        except Exception as e:
            error_message = f"Error durante el análisis: {e}"
            log_result(error_message, is_error=True)
            print(error_message)

test_parser()
