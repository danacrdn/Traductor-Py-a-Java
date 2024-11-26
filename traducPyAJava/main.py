# Ejercicio de Tradctor Python a Java
# Dana Paola Cardeña Aranda

from antlr4 import *
from pyToJavaLexer import pyToJavaLexer
from pyToJavaParser import pyToJavaParser
from TraducePyCode import TraducePyCode

# Archivos de entrada y salida
input_file = "multiply.py"
output_file = "Multiply.java"

try:
    input_stream = FileStream(input_file)
    lexer = pyToJavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = pyToJavaParser(token_stream)
    tree = parser.program()

    # Se hace uso del listener paara traducir
    listener = TraducePyCode()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #Genera el codigo en Java
    java_code = listener.generate_java_class()

    # Escribir el resultado en el archivo de salida
    with open(output_file, "w") as java_file:
        java_file.write(java_code)

    print(f"Codigo Java generado y guardado en {output_file}")

except FileNotFoundError:
    print(f"Error: El archivo {input_file} no existe.")
except Exception as e:
    print(f"Ocurrió un error durante la conversión: {e}")
