import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
import ply.lex as lex
import ply.yacc as yacc
from datetime import datetime
from lexico import tokens, lexer  # Importar los tokens y lexer definidos en lexico.py
from main import parser  # Importar el parser definido en main.py

# Crear carpeta de logs si no existe
if not os.path.exists("Logs"):
    os.makedirs("Logs")

# Función para ejecutar el análisis léxico
def analizar_lexico(input_text):
    lexer.input(input_text)  # Procesar el texto con el lexer
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    # Guardar resultados en archivo
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"Logs/lexico-{fecha_hora}.txt"
    with open(log_filename, "w") as log_file:
        for token in tokens:
            log_file.write(str(token) + "\n")
    return tokens

# Función para ejecutar el análisis sintáctico
def analizar_sintactico(input_text):
    try:
        result = parser.parse(input_text)  # Procesar el texto con el parser
        # Guardar resultados en archivo
        fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
        log_filename = f"Logs/sintactico-{fecha_hora}.txt"
        with open(log_filename, "w") as log_file:
            log_file.write(str(result))
        return result
    except Exception as e:
        return f"Error en análisis sintáctico: {e}"

# Función para ejecutar el análisis semántico (este es un ejemplo básico, puedes ampliarlo según tus reglas)
def analizar_semantico(input_text):
    # En este ejemplo, solo verificamos que no haya variables no definidas
    errors = []
    variables = {'var1': 'int', 'var2': 'float'}  # Simulamos un conjunto de variables definidas
    for word in input_text.split():
        if word not in variables and word.isidentifier():
            errors.append(f"Variable no definida: {word}")
    if errors:
        return "\n".join(errors)
    return "No se encontraron errores semánticos."

# Clase para la interfaz gráfica
class EditorGoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editor de Código Go")
        self.setGeometry(100, 100, 900, 700)  # Tamaño de la ventana
        self.setStyleSheet("background-color: white;")  # Fondo blanco

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Etiqueta de instrucciones
        label = QLabel("Editor de Código (Go):")
        label.setStyleSheet("font-size: 12pt; color: black;")
        layout.addWidget(label)

        # Cuadro de entrada de texto (editor de código)
        self.text_input = QPlainTextEdit()
        self.text_input.setStyleSheet("background-color: white; color: black; font-family: Consolas; font-size: 12pt;")
        self.text_input.setPlaceholderText("Escribe tu código Go aquí...")
        layout.addWidget(self.text_input)

        # Botón para procesar código
        btn_analizar = QPushButton("Procesar Código")
        btn_analizar.setStyleSheet("background-color: #007acc; color: white; font-size: 12pt;")
        btn_analizar.clicked.connect(self.procesar_codigo)
        layout.addWidget(btn_analizar)

        # Resultados de los tres análisis
        self.resultados_label = QLabel("Resultados del Análisis:")
        self.resultados_label.setStyleSheet("font-size: 12pt; color: black;")
        layout.addWidget(self.resultados_label)

        # Título y cuadro de resultados del análisis léxico
        self.resultados_lexico_label = QLabel("Resultado Léxico (Tokens generados):")
        self.resultados_lexico_label.setStyleSheet("font-size: 12pt; color: black;")
        layout.addWidget(self.resultados_lexico_label)
        self.resultados_lexico = QPlainTextEdit()
        self.resultados_lexico.setStyleSheet("background-color: #f0f0f0; color: black; font-family: Consolas; font-size: 12pt;")
        self.resultados_lexico.setReadOnly(True)
        layout.addWidget(self.resultados_lexico)

        # Título y cuadro de resultados del análisis sintáctico
        self.resultados_sintactico_label = QLabel("Resultado Sintáctico (Estructura del código):")
        self.resultados_sintactico_label.setStyleSheet("font-size: 12pt; color: black;")
        layout.addWidget(self.resultados_sintactico_label)
        self.resultados_sintactico = QPlainTextEdit()
        self.resultados_sintactico.setStyleSheet("background-color: #f0f0f0; color: black; font-family: Consolas; font-size: 12pt;")
        self.resultados_sintactico.setReadOnly(True)
        layout.addWidget(self.resultados_sintactico)

        # Título y cuadro de resultados del análisis semántico
        self.resultados_semantico_label = QLabel("Resultado Semántico (Errores de variables no definidas):")
        self.resultados_semantico_label.setStyleSheet("font-size: 12pt; color: black;")
        layout.addWidget(self.resultados_semantico_label)
        self.resultados_semantico = QPlainTextEdit()
        self.resultados_semantico.setStyleSheet("background-color: #f0f0f0; color: black; font-family: Consolas; font-size: 12pt;")
        self.resultados_semantico.setReadOnly(True)
        layout.addWidget(self.resultados_semantico)

        # Establecer el layout en la ventana principal
        self.setLayout(layout)

    # Función de procesamiento (todos los análisis)
    def procesar_codigo(self):
        input_text = self.text_input.toPlainText()
        if input_text.strip():
            # Análisis léxico
            tokens = analizar_lexico(input_text)
            self.resultados_lexico.setPlainText("\n".join([str(token) for token in tokens]))

            # Análisis sintáctico
            resultado_sintactico = analizar_sintactico(input_text)
            self.resultados_sintactico.setPlainText(str(resultado_sintactico))

            # Análisis semántico
            resultado_semantico = analizar_semantico(input_text)
            self.resultados_semantico.setPlainText(resultado_semantico)
        else:
            self.resultados_lexico.setPlainText("Por favor, ingresa texto en el editor.")
            self.resultados_sintactico.setPlainText("Por favor, ingresa texto en el editor.")
            self.resultados_semantico.setPlainText("Por favor, ingresa texto en el editor.")


# Crear la aplicación y la ventana
app = QApplication(sys.argv)
window = EditorGoApp()
window.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
