
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ARRAY ARRAYMOD ASSIGN BITWISEAND BITWISEANDASSIGN BITWISECLEAR BITWISEOR BITWISEORASSIGN BITWISEXOR BITWISEXORASSIGN BOOL BOOLV BREAK CASE COLON COMMA COMPLEX COMPLEXV CONST CONTINUE DECLARE_ASSIGN DECREMENTO DEFAULT DEFER DIV DIVA DOT ELSE EQ EQUAL ERROR FALLTHROUGH FLOAT FLOATV FMT FOR FORMATO FUNC GO GOTO GT GTOEQ IF IMPORT INCREMENTO INT INTERFACE INTV LCORCHETE LLLAVE LPARENTESIS LT LTOEQ MAIN MAP MINUS MINUSA MOD MODA MULTILINECOMMENT NEQ NOT ONELINECOMMENT OR PACKAGE PLUS PLUSA PRINT PRINTF PRINTLN RANGE RCORCHETE RETURN RLLAVE RPARENTESIS SALTO_LINEA SCAN SCANF SCANLN SELECT SEMICOLON SHIFTLEFT SHIFTLEFTASSIGN SHIFTRIGHT SHIFTRIGHTASSIGN SLICE SLICEV SPRINT SPRINTF SPRINTLN STRING STRINGV SWITCH TAB TIMES TIMESA UINT UINTV VAR VARIABLEprograma : declaracionesdeclaraciones : declaracion_statement\n                      | declaracion_statement SALTO_LINEA declaracionesdeclaracion_statement : declaracion_array\n                            | declaracion_mapa\n                            | declaracion_variable\n                            | imprimir\n                            | modificar_estructuras\n                            | estructuraif\n                            | estructuraif_else\n                            | estructura_for\n                            | funcion\n                            | ONELINECOMMENT\n                            | MULTILINECOMMENT\n                            | leer_entradasfuncion : FUNC MAIN LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE\n              | FUNC VARIABLE LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE\n              | FUNC VARIABLE LPARENTESIS parametros RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVEparametros : parametro\n                 | parametro COMMA parametrosparametro : VARIABLE typeestructuraif_else : estructuraif ELSE condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVEestructuraif : IF condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVEestructura_for : FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable1 LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE\n                     | FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable2 valor LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE\n                     | FOR VARIABLE operador_logico LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVEoperador_modifica_variable1 : INCREMENTO\n                              | DECREMENTOoperador_modifica_variable2 : ASSIGN\n                              | PLUSA\n                              | MINUSA\n                              | TIMESA\n                              | DIVA\n                              | MODAdeclaraciones_tabs : declaracion_statement_tabs\n                          | declaracion_statement_tabs SALTO_LINEA declaraciones_tabsdeclaracion_statement_tabs : TAB declaracion_array\n                            | TAB declaracion_mapa\n                            | TAB declaracion_variable\n                            | TAB imprimir\n                            | TAB modificar_estructuras\n                            | TAB estructuraif\n                            | TAB estructuraif_else\n                            | TAB estructura_for\n                            | TAB funcion\n                            | TAB ONELINECOMMENT\n                            | TAB MULTILINECOMMENT\n                            | TAB leer_entradascondiciones : condicion\n                  | condicion operador_logico condicionescondicion : VARIABLE operador_relacional valordeclaracion_variable : VAR VARIABLE type ASSIGN operacion_aritmetica\n                           | VAR asignacion\n                           | VAR variables type\n                           | VAR VARIABLE type\n                           | VARIABLE DECLARE_ASSIGN valor\n                           | CONST VARIABLE ASSIGN operacion_aritmetica\n                           | VAR LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESIS\n                           | CONST LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESISdeclaracion_array : VARIABLE DECLARE_ASSIGN ARRAY LLLAVE valores RLLAVE\n                        | VAR VARIABLE ASSIGN ARRAY LLLAVE valores RLLAVEdeclaracion_mapa : VARIABLE DECLARE_ASSIGN MAP LLLAVE pares RLLAVEmodificar_estructuras : agregar_elemento_arraypares : par\n             | par COMMA parespar : valor COLON valoragregar_elemento_array : ARRAYMOD ASSIGN valorimprimir : FMT DOT PRINTLN LPARENTESIS operaciones_aritmeticas RPARENTESIS\n               | FMT DOT PRINT LPARENTESIS operaciones_aritmeticas RPARENTESIS\n               | FMT DOT PRINTF LPARENTESIS operaciones_aritmeticas RPARENTESISleer_entradas : FMT DOT SCAN LPARENTESIS parametros_scan RPARENTESIS\n                    | FMT DOT SCANLN LPARENTESIS parametros_scan RPARENTESIS\n                    | FMT DOT SCANF LPARENTESIS FORMATO COMMA parametros_scan RPARENTESISparametros_scan : parametro_scan\n                      | parametro_scan COMMA parametros_scanparametro_scan : BITWISEAND VARIABLEasignacion : VARIABLE ASSIGN valorvalores : valor\n              | valor COMMA valoresvariables : VARIABLE\n                | VARIABLE COMMA variablesoperacion_aritmetica : valor\n                           | valor operador operacion_aritmeticaoperaciones_aritmeticas : operacion_aritmetica\n                              | operacion_aritmetica COMMA operaciones_aritmeticasdeclaraciones_sencillas : asignacion\n                              | asignacion TAB declaraciones_sencillastype : BOOL\n            | INT\n            | FLOAT\n            | UINT\n            | STRING\n            | COMPLEX\n            | ARRAY\n            | SLICE\n            | MAPoperador : PLUS\n               | MINUS\n               | MOD\n               | TIMES\n               | DIVvalor : BOOLV\n                | INTV\n                | FLOATV\n                | UINTV\n                | STRINGV\n                | VARIABLE\n                | SLICEVoperador_relacional : EQ\n                           | NEQ\n                           | LT\n                           | GT\n                           | LTOEQ\n                           | GTOEQoperador_logico : AND\n                       | OR'
    
_lr_action_items = {'ONELINECOMMENT':([0,25,151,],[13,13,190,]),'MULTILINECOMMENT':([0,25,151,],[14,14,191,]),'VARIABLE':([0,17,18,21,22,23,25,26,27,41,54,57,67,68,69,77,78,79,80,81,82,83,84,85,86,87,90,93,94,97,106,107,108,128,131,132,133,134,135,136,137,138,146,151,152,158,161,163,164,171,209,221,228,231,232,233,234,235,236,],[16,28,32,37,38,40,16,37,44,44,44,98,102,44,102,37,-115,-116,44,-109,-110,-111,-112,-113,-114,44,118,44,44,44,44,44,44,44,102,44,44,-97,-98,-99,-100,-101,176,16,193,118,44,44,44,44,44,225,44,-29,-30,-31,-32,-33,-34,]),'VAR':([0,25,151,],[17,17,17,]),'CONST':([0,25,151,],[18,18,18,]),'FMT':([0,25,151,],[19,19,19,]),'IF':([0,25,151,],[21,21,21,]),'FOR':([0,25,151,],[22,22,22,]),'FUNC':([0,25,151,],[23,23,23,]),'ARRAYMOD':([0,25,151,],[24,24,24,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,29,42,44,47,48,49,50,51,52,53,55,56,58,59,60,61,62,63,64,65,66,91,96,103,104,129,160,162,166,168,169,170,172,173,174,177,203,207,214,215,217,222,223,226,245,247,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-63,-53,-3,-107,-56,-102,-103,-104,-105,-106,-108,-94,-55,-88,-89,-90,-91,-92,-93,-95,-96,-54,-67,-77,-57,-82,-52,-60,-62,-58,-83,-59,-68,-69,-70,-71,-72,-61,-23,-22,-73,-26,-16,-17,-18,-24,-25,]),'SALTO_LINEA':([3,4,5,6,7,8,9,10,11,12,13,14,15,20,29,31,33,44,47,48,49,50,51,52,53,55,56,58,59,60,61,62,63,64,65,66,76,91,92,96,100,101,103,104,105,116,129,149,150,154,156,159,160,162,166,167,168,169,170,172,173,174,177,181,182,183,184,185,186,187,188,189,190,191,192,194,197,203,207,208,211,212,214,215,217,220,222,223,226,237,240,241,244,245,247,],[25,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-63,-53,67,69,-107,-56,-102,-103,-104,-105,-106,-108,-94,-55,-88,-89,-90,-91,-92,-93,-95,-96,-54,112,-67,122,-77,130,-86,-57,-82,139,153,-52,179,180,195,196,199,-60,-62,-58,-87,-83,-59,-68,-69,-70,-71,-72,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,210,213,-61,-23,-36,218,219,-22,-73,-26,224,-16,-17,-18,239,242,243,246,-24,-25,]),'ELSE':([9,186,207,],[26,26,-23,]),'DECLARE_ASSIGN':([16,38,],[27,87,]),'LPARENTESIS':([17,18,39,40,70,71,72,73,74,75,],[31,33,89,90,106,107,108,109,110,111,]),'DOT':([19,],[34,]),'MAIN':([23,],[39,]),'ASSIGN':([24,28,32,55,56,58,59,60,61,62,63,64,65,102,225,],[41,54,68,-94,97,-88,-89,-90,-91,-92,-93,-95,-96,132,231,]),'ARRAY':([27,28,30,54,98,99,118,],[45,55,55,95,-80,-81,55,]),'MAP':([27,28,30,98,99,118,],[46,65,65,-80,-81,65,]),'BOOLV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[48,48,48,48,-115,-116,48,-109,-110,-111,-112,-113,-114,48,48,48,48,48,48,48,48,48,48,-97,-98,-99,-100,-101,48,48,48,48,48,48,-29,-30,-31,-32,-33,-34,]),'INTV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[49,49,49,49,-115,-116,49,-109,-110,-111,-112,-113,-114,49,49,49,49,49,49,49,49,49,49,-97,-98,-99,-100,-101,49,49,49,49,49,49,-29,-30,-31,-32,-33,-34,]),'FLOATV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[50,50,50,50,-115,-116,50,-109,-110,-111,-112,-113,-114,50,50,50,50,50,50,50,50,50,50,-97,-98,-99,-100,-101,50,50,50,50,50,50,-29,-30,-31,-32,-33,-34,]),'UINTV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[51,51,51,51,-115,-116,51,-109,-110,-111,-112,-113,-114,51,51,51,51,51,51,51,51,51,51,-97,-98,-99,-100,-101,51,51,51,51,51,51,-29,-30,-31,-32,-33,-34,]),'STRINGV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[52,52,52,52,-115,-116,52,-109,-110,-111,-112,-113,-114,52,52,52,52,52,52,52,52,52,52,-97,-98,-99,-100,-101,52,52,52,52,52,52,-29,-30,-31,-32,-33,-34,]),'SLICEV':([27,41,54,68,78,79,80,81,82,83,84,85,86,87,93,94,97,106,107,108,128,132,133,134,135,136,137,138,161,163,164,171,209,228,231,232,233,234,235,236,],[53,53,53,53,-115,-116,53,-109,-110,-111,-112,-113,-114,53,53,53,53,53,53,53,53,53,53,-97,-98,-99,-100,-101,53,53,53,53,53,53,-29,-30,-31,-32,-33,-34,]),'BOOL':([28,30,98,99,118,],[58,58,-80,-81,58,]),'INT':([28,30,98,99,118,],[59,59,-80,-81,59,]),'FLOAT':([28,30,98,99,118,],[60,60,-80,-81,60,]),'UINT':([28,30,98,99,118,],[61,61,-80,-81,61,]),'STRING':([28,30,98,99,118,],[62,62,-80,-81,62,]),'COMPLEX':([28,30,98,99,118,],[63,63,-80,-81,63,]),'SLICE':([28,30,98,99,118,],[64,64,-80,-81,64,]),'COMMA':([28,44,48,49,50,51,52,53,55,58,59,60,61,62,63,64,65,98,104,121,124,126,141,145,148,155,168,176,202,],[57,-107,-102,-103,-104,-105,-106,-108,-94,-88,-89,-90,-91,-92,-93,-95,-96,57,-82,158,161,163,171,175,178,-21,-83,-76,-66,]),'PRINTLN':([34,],[70,]),'PRINT':([34,],[71,]),'PRINTF':([34,],[72,]),'SCAN':([34,],[73,]),'SCANLN':([34,],[74,]),'SCANF':([34,],[75,]),'LLLAVE':([35,36,43,44,45,46,48,49,50,51,52,53,78,79,88,95,113,114,117,119,157,227,229,230,238,],[76,-49,92,-107,93,94,-102,-103,-104,-105,-106,-108,-115,-116,116,128,-50,-51,154,156,197,237,-27,-28,240,]),'AND':([36,38,44,48,49,50,51,52,53,114,193,],[78,78,-107,-102,-103,-104,-105,-106,-108,-51,78,]),'OR':([36,38,44,48,49,50,51,52,53,114,193,],[79,79,-107,-102,-103,-104,-105,-106,-108,-51,79,]),'EQ':([37,],[81,]),'NEQ':([37,],[82,]),'LT':([37,],[83,]),'GT':([37,],[84,]),'LTOEQ':([37,],[85,]),'GTOEQ':([37,],[86,]),'PLUS':([44,48,49,50,51,52,53,104,],[-107,-102,-103,-104,-105,-106,-108,134,]),'MINUS':([44,48,49,50,51,52,53,104,],[-107,-102,-103,-104,-105,-106,-108,135,]),'MOD':([44,48,49,50,51,52,53,104,],[-107,-102,-103,-104,-105,-106,-108,136,]),'TIMES':([44,48,49,50,51,52,53,104,],[-107,-102,-103,-104,-105,-106,-108,137,]),'DIV':([44,48,49,50,51,52,53,104,],[-107,-102,-103,-104,-105,-106,-108,138,]),'SEMICOLON':([44,48,49,50,51,52,53,115,216,],[-107,-102,-103,-104,-105,-106,-108,152,221,]),'RLLAVE':([44,48,49,50,51,52,53,123,124,125,126,165,179,199,200,201,202,210,218,219,224,243,246,],[-107,-102,-103,-104,-105,-106,-108,160,-78,162,-64,203,207,214,-79,-65,-66,217,222,223,226,245,247,]),'COLON':([44,48,49,50,51,52,53,127,],[-107,-102,-103,-104,-105,-106,-108,164,]),'RPARENTESIS':([44,48,49,50,51,52,53,55,58,59,60,61,62,63,64,65,89,90,104,120,121,130,139,140,141,142,143,144,145,147,155,168,176,198,204,205,206,],[-107,-102,-103,-104,-105,-106,-108,-94,-88,-89,-90,-91,-92,-93,-95,-96,117,119,-82,157,-19,166,169,170,-84,172,173,174,-74,177,-21,-83,-76,-20,-85,-75,215,]),'TAB':([44,48,49,50,51,52,53,96,101,112,122,153,180,195,196,213,239,242,],[-107,-102,-103,-104,-105,-106,-108,-77,131,151,151,151,151,151,151,151,151,151,]),'BITWISEAND':([109,110,175,178,],[146,146,146,146,]),'FORMATO':([111,],[148,]),'INCREMENTO':([225,],[229,]),'DECREMENTO':([225,],[230,]),'PLUSA':([225,],[232,]),'MINUSA':([225,],[233,]),'TIMESA':([225,],[234,]),'DIVA':([225,],[235,]),'MODA':([225,],[236,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaraciones':([0,25,],[2,42,]),'declaracion_statement':([0,25,],[3,3,]),'declaracion_array':([0,25,151,],[4,4,181,]),'declaracion_mapa':([0,25,151,],[5,5,182,]),'declaracion_variable':([0,25,151,],[6,6,183,]),'imprimir':([0,25,151,],[7,7,184,]),'modificar_estructuras':([0,25,151,],[8,8,185,]),'estructuraif':([0,25,151,],[9,9,186,]),'estructuraif_else':([0,25,151,],[10,10,187,]),'estructura_for':([0,25,151,],[11,11,188,]),'funcion':([0,25,151,],[12,12,189,]),'leer_entradas':([0,25,151,],[15,15,192,]),'agregar_elemento_array':([0,25,151,],[20,20,20,]),'asignacion':([17,67,69,131,],[29,101,101,101,]),'variables':([17,57,],[30,99,]),'condiciones':([21,26,77,],[35,43,113,]),'condicion':([21,26,77,],[36,36,36,]),'valor':([27,41,54,68,80,87,93,94,97,106,107,108,128,132,133,161,163,164,171,209,228,],[47,91,96,104,114,115,124,127,104,104,104,104,124,96,104,124,127,202,104,216,238,]),'type':([28,30,118,],[56,66,155,]),'operador_logico':([36,38,193,],[77,88,209,]),'operador_relacional':([37,],[80,]),'declaraciones_sencillas':([67,69,131,],[100,105,167,]),'operacion_aritmetica':([68,97,106,107,108,133,171,],[103,129,141,141,141,168,141,]),'parametros':([90,158,],[120,198,]),'parametro':([90,158,],[121,121,]),'valores':([93,128,161,],[123,165,200,]),'pares':([94,163,],[125,201,]),'par':([94,163,],[126,126,]),'operador':([104,],[133,]),'operaciones_aritmeticas':([106,107,108,171,],[140,142,143,204,]),'parametros_scan':([109,110,175,178,],[144,147,205,206,]),'parametro_scan':([109,110,175,178,],[145,145,145,145,]),'declaraciones_tabs':([112,122,153,180,195,196,213,239,242,],[149,159,194,208,211,212,220,241,244,]),'declaracion_statement_tabs':([112,122,153,180,195,196,213,239,242,],[150,150,150,150,150,150,150,150,150,]),'operador_modifica_variable1':([225,],[227,]),'operador_modifica_variable2':([225,],[228,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaraciones','programa',1,'p_programa','main.py',20),
  ('declaraciones -> declaracion_statement','declaraciones',1,'p_declaraciones','main.py',23),
  ('declaraciones -> declaracion_statement SALTO_LINEA declaraciones','declaraciones',3,'p_declaraciones','main.py',24),
  ('declaracion_statement -> declaracion_array','declaracion_statement',1,'p_declaracion_stastement','main.py',27),
  ('declaracion_statement -> declaracion_mapa','declaracion_statement',1,'p_declaracion_stastement','main.py',28),
  ('declaracion_statement -> declaracion_variable','declaracion_statement',1,'p_declaracion_stastement','main.py',29),
  ('declaracion_statement -> imprimir','declaracion_statement',1,'p_declaracion_stastement','main.py',30),
  ('declaracion_statement -> modificar_estructuras','declaracion_statement',1,'p_declaracion_stastement','main.py',31),
  ('declaracion_statement -> estructuraif','declaracion_statement',1,'p_declaracion_stastement','main.py',32),
  ('declaracion_statement -> estructuraif_else','declaracion_statement',1,'p_declaracion_stastement','main.py',33),
  ('declaracion_statement -> estructura_for','declaracion_statement',1,'p_declaracion_stastement','main.py',34),
  ('declaracion_statement -> funcion','declaracion_statement',1,'p_declaracion_stastement','main.py',35),
  ('declaracion_statement -> ONELINECOMMENT','declaracion_statement',1,'p_declaracion_stastement','main.py',36),
  ('declaracion_statement -> MULTILINECOMMENT','declaracion_statement',1,'p_declaracion_stastement','main.py',37),
  ('declaracion_statement -> leer_entradas','declaracion_statement',1,'p_declaracion_stastement','main.py',38),
  ('funcion -> FUNC MAIN LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','funcion',9,'p_funcion','main.py',41),
  ('funcion -> FUNC VARIABLE LPARENTESIS RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','funcion',9,'p_funcion','main.py',42),
  ('funcion -> FUNC VARIABLE LPARENTESIS parametros RPARENTESIS LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','funcion',10,'p_funcion','main.py',43),
  ('parametros -> parametro','parametros',1,'p_parametros','main.py',46),
  ('parametros -> parametro COMMA parametros','parametros',3,'p_parametros','main.py',47),
  ('parametro -> VARIABLE type','parametro',2,'p_parametro','main.py',50),
  ('estructuraif_else -> estructuraif ELSE condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','estructuraif_else',8,'p_estructuraif_else','main.py',53),
  ('estructuraif -> IF condiciones LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','estructuraif',7,'p_estructuraif','main.py',56),
  ('estructura_for -> FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable1 LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','estructura_for',16,'p_estructura_for','main.py',59),
  ('estructura_for -> FOR VARIABLE DECLARE_ASSIGN valor SEMICOLON VARIABLE operador_logico valor SEMICOLON VARIABLE operador_modifica_variable2 valor LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','estructura_for',17,'p_estructura_for','main.py',60),
  ('estructura_for -> FOR VARIABLE operador_logico LLLAVE SALTO_LINEA declaraciones_tabs SALTO_LINEA RLLAVE','estructura_for',8,'p_estructura_for','main.py',61),
  ('operador_modifica_variable1 -> INCREMENTO','operador_modifica_variable1',1,'p_operador_modifica_variable1','main.py',64),
  ('operador_modifica_variable1 -> DECREMENTO','operador_modifica_variable1',1,'p_operador_modifica_variable1','main.py',65),
  ('operador_modifica_variable2 -> ASSIGN','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',68),
  ('operador_modifica_variable2 -> PLUSA','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',69),
  ('operador_modifica_variable2 -> MINUSA','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',70),
  ('operador_modifica_variable2 -> TIMESA','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',71),
  ('operador_modifica_variable2 -> DIVA','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',72),
  ('operador_modifica_variable2 -> MODA','operador_modifica_variable2',1,'p_operador_modifica_variable2','main.py',73),
  ('declaraciones_tabs -> declaracion_statement_tabs','declaraciones_tabs',1,'p_declaraciones_tabs','main.py',76),
  ('declaraciones_tabs -> declaracion_statement_tabs SALTO_LINEA declaraciones_tabs','declaraciones_tabs',3,'p_declaraciones_tabs','main.py',77),
  ('declaracion_statement_tabs -> TAB declaracion_array','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',81),
  ('declaracion_statement_tabs -> TAB declaracion_mapa','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',82),
  ('declaracion_statement_tabs -> TAB declaracion_variable','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',83),
  ('declaracion_statement_tabs -> TAB imprimir','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',84),
  ('declaracion_statement_tabs -> TAB modificar_estructuras','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',85),
  ('declaracion_statement_tabs -> TAB estructuraif','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',86),
  ('declaracion_statement_tabs -> TAB estructuraif_else','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',87),
  ('declaracion_statement_tabs -> TAB estructura_for','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',88),
  ('declaracion_statement_tabs -> TAB funcion','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',89),
  ('declaracion_statement_tabs -> TAB ONELINECOMMENT','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',90),
  ('declaracion_statement_tabs -> TAB MULTILINECOMMENT','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',91),
  ('declaracion_statement_tabs -> TAB leer_entradas','declaracion_statement_tabs',2,'p_declaracion_statement_tabs','main.py',92),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','main.py',95),
  ('condiciones -> condicion operador_logico condiciones','condiciones',3,'p_condiciones','main.py',96),
  ('condicion -> VARIABLE operador_relacional valor','condicion',3,'p_condicion','main.py',99),
  ('declaracion_variable -> VAR VARIABLE type ASSIGN operacion_aritmetica','declaracion_variable',5,'p_declaracion_variable','main.py',103),
  ('declaracion_variable -> VAR asignacion','declaracion_variable',2,'p_declaracion_variable','main.py',104),
  ('declaracion_variable -> VAR variables type','declaracion_variable',3,'p_declaracion_variable','main.py',105),
  ('declaracion_variable -> VAR VARIABLE type','declaracion_variable',3,'p_declaracion_variable','main.py',106),
  ('declaracion_variable -> VARIABLE DECLARE_ASSIGN valor','declaracion_variable',3,'p_declaracion_variable','main.py',107),
  ('declaracion_variable -> CONST VARIABLE ASSIGN operacion_aritmetica','declaracion_variable',4,'p_declaracion_variable','main.py',108),
  ('declaracion_variable -> VAR LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESIS','declaracion_variable',6,'p_declaracion_variable','main.py',109),
  ('declaracion_variable -> CONST LPARENTESIS SALTO_LINEA declaraciones_sencillas SALTO_LINEA RPARENTESIS','declaracion_variable',6,'p_declaracion_variable','main.py',110),
  ('declaracion_array -> VARIABLE DECLARE_ASSIGN ARRAY LLLAVE valores RLLAVE','declaracion_array',6,'p_declaracion_array','main.py',113),
  ('declaracion_array -> VAR VARIABLE ASSIGN ARRAY LLLAVE valores RLLAVE','declaracion_array',7,'p_declaracion_array','main.py',114),
  ('declaracion_mapa -> VARIABLE DECLARE_ASSIGN MAP LLLAVE pares RLLAVE','declaracion_mapa',6,'p_declaracion_mapa','main.py',117),
  ('modificar_estructuras -> agregar_elemento_array','modificar_estructuras',1,'p_modificar_structuras','main.py',120),
  ('pares -> par','pares',1,'p_pares','main.py',123),
  ('pares -> par COMMA pares','pares',3,'p_pares','main.py',124),
  ('par -> valor COLON valor','par',3,'p_par','main.py',127),
  ('agregar_elemento_array -> ARRAYMOD ASSIGN valor','agregar_elemento_array',3,'p_agregar_elemento_array','main.py',130),
  ('imprimir -> FMT DOT PRINTLN LPARENTESIS operaciones_aritmeticas RPARENTESIS','imprimir',6,'p_imprimir','main.py',133),
  ('imprimir -> FMT DOT PRINT LPARENTESIS operaciones_aritmeticas RPARENTESIS','imprimir',6,'p_imprimir','main.py',134),
  ('imprimir -> FMT DOT PRINTF LPARENTESIS operaciones_aritmeticas RPARENTESIS','imprimir',6,'p_imprimir','main.py',135),
  ('leer_entradas -> FMT DOT SCAN LPARENTESIS parametros_scan RPARENTESIS','leer_entradas',6,'p_leer_entradas','main.py',138),
  ('leer_entradas -> FMT DOT SCANLN LPARENTESIS parametros_scan RPARENTESIS','leer_entradas',6,'p_leer_entradas','main.py',139),
  ('leer_entradas -> FMT DOT SCANF LPARENTESIS FORMATO COMMA parametros_scan RPARENTESIS','leer_entradas',8,'p_leer_entradas','main.py',140),
  ('parametros_scan -> parametro_scan','parametros_scan',1,'p_parametros_scan','main.py',143),
  ('parametros_scan -> parametro_scan COMMA parametros_scan','parametros_scan',3,'p_parametros_scan','main.py',144),
  ('parametro_scan -> BITWISEAND VARIABLE','parametro_scan',2,'p_parametro_scan','main.py',147),
  ('asignacion -> VARIABLE ASSIGN valor','asignacion',3,'p_asignacion','main.py',150),
  ('valores -> valor','valores',1,'p_valores','main.py',154),
  ('valores -> valor COMMA valores','valores',3,'p_valores','main.py',155),
  ('variables -> VARIABLE','variables',1,'p_variables','main.py',158),
  ('variables -> VARIABLE COMMA variables','variables',3,'p_variables','main.py',159),
  ('operacion_aritmetica -> valor','operacion_aritmetica',1,'p_operacion_aritmetica','main.py',162),
  ('operacion_aritmetica -> valor operador operacion_aritmetica','operacion_aritmetica',3,'p_operacion_aritmetica','main.py',163),
  ('operaciones_aritmeticas -> operacion_aritmetica','operaciones_aritmeticas',1,'p_operaciones_aritmeticas','main.py',166),
  ('operaciones_aritmeticas -> operacion_aritmetica COMMA operaciones_aritmeticas','operaciones_aritmeticas',3,'p_operaciones_aritmeticas','main.py',167),
  ('declaraciones_sencillas -> asignacion','declaraciones_sencillas',1,'p_declaraciones_sencillas','main.py',170),
  ('declaraciones_sencillas -> asignacion TAB declaraciones_sencillas','declaraciones_sencillas',3,'p_declaraciones_sencillas','main.py',171),
  ('type -> BOOL','type',1,'p_type','main.py',175),
  ('type -> INT','type',1,'p_type','main.py',176),
  ('type -> FLOAT','type',1,'p_type','main.py',177),
  ('type -> UINT','type',1,'p_type','main.py',178),
  ('type -> STRING','type',1,'p_type','main.py',179),
  ('type -> COMPLEX','type',1,'p_type','main.py',180),
  ('type -> ARRAY','type',1,'p_type','main.py',181),
  ('type -> SLICE','type',1,'p_type','main.py',182),
  ('type -> MAP','type',1,'p_type','main.py',183),
  ('operador -> PLUS','operador',1,'p_operador','main.py',186),
  ('operador -> MINUS','operador',1,'p_operador','main.py',187),
  ('operador -> MOD','operador',1,'p_operador','main.py',188),
  ('operador -> TIMES','operador',1,'p_operador','main.py',189),
  ('operador -> DIV','operador',1,'p_operador','main.py',190),
  ('valor -> BOOLV','valor',1,'p_valor','main.py',193),
  ('valor -> INTV','valor',1,'p_valor','main.py',194),
  ('valor -> FLOATV','valor',1,'p_valor','main.py',195),
  ('valor -> UINTV','valor',1,'p_valor','main.py',196),
  ('valor -> STRINGV','valor',1,'p_valor','main.py',197),
  ('valor -> VARIABLE','valor',1,'p_valor','main.py',198),
  ('valor -> SLICEV','valor',1,'p_valor','main.py',199),
  ('operador_relacional -> EQ','operador_relacional',1,'p_operador_relacional','main.py',202),
  ('operador_relacional -> NEQ','operador_relacional',1,'p_operador_relacional','main.py',203),
  ('operador_relacional -> LT','operador_relacional',1,'p_operador_relacional','main.py',204),
  ('operador_relacional -> GT','operador_relacional',1,'p_operador_relacional','main.py',205),
  ('operador_relacional -> LTOEQ','operador_relacional',1,'p_operador_relacional','main.py',206),
  ('operador_relacional -> GTOEQ','operador_relacional',1,'p_operador_relacional','main.py',207),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','main.py',210),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','main.py',211),
]
