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
