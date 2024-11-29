import ply.yacc as yacc
from datetime import datetime
import os
from lexico import tokens

# Obtener fecha y usuario para logs
fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
usuario_git = "jjroldev"

# Crear carpeta de logs si no existe
if not os.path.exists("Logs"):
    os.makedirs("Logs")

# Nombre del archivo de log
log_filename = f"Logs/sintactico-{usuario_git}-{fecha_hora}.txt"

# Reglas gramaticales

def p_programa(p):
    '''programa : declaraciones'''

def p_declaracion_entera_variable(p):
    '''declaracion_entera_variable : VAR VARIABLE INT ASSIGN operaciones_aritmetica_entero'''

def p_comparador_entero(p):
    '''comparador_entero : INTV operador_relacional INTV'''

def p_declaraciones(p):
    '''declaraciones : declaracion_statement
                      | declaracion_statement SALTO_LINEA declaraciones'''

def p_declaracion_stastement(p):
    '''declaracion_statement : declaracion_array
                            | declaracion_mapa
                            | declaracion_variable
                            | imprimir
                            | modificar_estructuras
                            | estructuraif
                            | estructuraif_else
                            | estructura_for
                            | funcion
                            | ONELINECOMMENT
                            | MULTILINECOMMENT
                            | leer_entradas
                            | comparador_entero'''

def p_funcion(p):
    '''funcion : FUNC MAIN LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE
              | FUNC VARIABLE LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE
              | FUNC VARIABLE LPARENTESIS parametros RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE'''

def p_parametros(p):
    '''parametros : parametro
                 | parametro COMMA parametros'''

def p_parametro(p):
    '''parametro : VARIABLE type'''

def p_estructuraif_else(p):
    '''estructuraif_else : estructuraif ELSE condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE'''

def p_estructuraif(p):
    '''estructuraif : IF condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE'''

def p_estructura_for(p):
    '''estructura_for : FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable1 LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE
                     | FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable2 valor LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE
                     | FOR VARIABLE operador_logico LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE'''

def p_operador_modifica_variable1(p):
    '''operador_modifica_variable1 : INCREMENTO
                              | DECREMENTO'''

def p_operador_modifica_variable2(p):
    '''operador_modifica_variable2 : ASSIGN
                              | PLUSA
                              | MINUSA
                              | TIMESA
                              | DIVA
                              | MODA'''

def p_declaraciones_tabs(p):
    '''declaraciones_tabs : declaracion_statement_tabs
                          | declaracion_statement_tabs SALTO_LINEA declaraciones_tabs'''


def p_declaracion_statement_tabs(p):
    '''declaracion_statement_tabs : TAB declaracion_array
                            | TAB declaracion_mapa
                            | TAB declaracion_variable
                            | TAB imprimir
                            | TAB modificar_estructuras
                            | TAB estructuraif
                            | TAB estructuraif_else
                            | TAB estructura_for
                            | TAB funcion
                            | TAB ONELINECOMMENT
                            | TAB MULTILINECOMMENT
                            | TAB leer_entradas'''

def p_condiciones(p):
    '''condiciones : condicion
                  | condicion operador_logico condiciones'''

def p_condicion(p):
    'condicion : VARIABLE operador_relacional valor'

def p_operaciones_aritmetica_entero(p):
    '''operaciones_aritmetica_entero : operacion_aritmetica_entero
                                     | operacion_aritmetica_entero operador operaciones_aritmetica_entero'''

def p_operacion_aritmetica_entero(p):
    '''operacion_aritmetica_entero : INTV
                                  | INTV operador INTV'''


def p_declaracion_variable(p):
    '''declaracion_variable : VAR VARIABLE type ASSIGN operaciones_aritmeticas
                           | VAR asignacion
                           | VAR variables type
                           | VAR VARIABLE type
                           | VARIABLE DECLARE_ASSIGN valor
                           | CONST VARIABLE ASSIGN operacion_aritmetica
                           | VAR LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESIS
                           | CONST LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESIS'''


def p_declaracion_array(p):
    '''declaracion_array : VARIABLE DECLARE_ASSIGN ARRAY LLLAVE valores RLLAVE
                        | VAR VARIABLE ASSIGN ARRAY LLLAVE valores RLLAVE'''

def p_declaracion_mapa(p):
    '''declaracion_mapa : VARIABLE DECLARE_ASSIGN MAP LLLAVE pares RLLAVE'''

def p_modificar_structuras(p):
    '''modificar_estructuras : agregar_elemento_array'''

def p_pares(p):
    '''pares : par
             | par COMMA pares'''

def p_par(p):
    '''par : valor COLON valor'''

def p_agregar_elemento_array(p):
    '''agregar_elemento_array : ARRAYMOD ASSIGN valor'''

def p_imprimir(p):
    '''imprimir : FMT DOT PRINTLN LPARENTESIS operaciones_aritmeticas RPARENTESIS
               | FMT DOT PRINT LPARENTESIS operaciones_aritmeticas RPARENTESIS
               | FMT DOT PRINTF LPARENTESIS operaciones_aritmeticas RPARENTESIS'''

def p_leer_entradas(p):
    '''leer_entradas : FMT DOT SCAN LPARENTESIS parametros_scan RPARENTESIS
                    | FMT DOT SCANLN LPARENTESIS parametros_scan RPARENTESIS
                    | FMT DOT SCANF LPARENTESIS FORMATO COMMA parametros_scan RPARENTESIS'''

def p_parametros_scan(p):
    '''parametros_scan : parametro_scan
                      | parametro_scan COMMA parametros_scan'''

def p_parametro_scan(p):
    '''parametro_scan : BITWISEAND VARIABLE'''

def p_asignacion(p):
    '''asignacion : VARIABLE ASSIGN valor'''


def p_valores(p):
    '''valores : valor
              | valor COMMA valores'''

def p_variables(p):
    '''variables : VARIABLE
                | VARIABLE COMMA variables'''

def p_operacion_aritmetica(p):
    '''operacion_aritmetica : valor
                           | valor operador operacion_aritmetica'''

def p_operaciones_aritmeticas(p):
    '''operaciones_aritmeticas : operacion_aritmetica
                              | operacion_aritmetica COMMA operaciones_aritmeticas'''

def p_declaraciones_sencillas(p):
    '''declaraciones_sencillas : asignacion
                              | asignacion TAB declaraciones_sencillas'''


def p_type(p):
    '''type : BOOL
            | INT
            | FLOAT
            | UINT
            | STRING
            | COMPLEX
            | ARRAY
            | SLICE
            | MAP'''

def p_operador(p):
    '''operador : PLUS
               | MINUS
               | MOD
               | TIMES
               | DIV'''

def p_valor(p):
    '''valor : BOOLV
                | INTV
                | FLOATV
                | UINTV
                | STRINGV
                | VARIABLE
                | SLICEV'''

def p_operador_relacional(p):
    '''operador_relacional : EQ
                           | NEQ
                           | LT
                           | GT
                           | LTOEQ
                           | GTOEQ'''

def p_operador_logico(p):
    '''operador_logico : AND
                       | OR'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('golang > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)