# Traductor de Python a Java
Este programa es una herramienta que convierte un código específico de Python a Java. Utiliza el análisis de un archivo Python mediante ANTLR para generar el código Java correspondiente, incluyendo la conversión de funciones, expresiones y sentencias print

## Uso
1. Prepara un archivo que quieras traducir, el cual debe contener el siguiente codigo:
    ![image](https://github.com/user-attachments/assets/867f004e-f520-4fe2-9bf9-a8707bc90c75)
2. En el archivo main.py puedes cambiar los archivos de entrada y de salida, input_file siendo el nombre del archivo que preparaste y output_file el archivo que será generado:
   ![image](https://github.com/user-attachments/assets/8bf0999f-3a91-4684-9075-7c7e1e04a71e)
3. Ejecuta el script Python que traduce el código a Java, main.py: ![image](https://github.com/user-attachments/assets/290c540c-e087-463d-b2dd-dcc0acdf11df)
4. El archivo .java será generado con el código equivalente del archivo Python en Java. Si usaste el código de ejemplo en multiply.py, el archivo Multiply.java generado será como esto:
 ![image](https://github.com/user-attachments/assets/03c9b09a-ecda-4eb5-8819-7be7188c1f9a)

Los valores de los parámetros en las llamadas a funciones se manejan de forma estática. El programa no extrae dinámicamente los valores de los argumentos de manera completa todavía.


