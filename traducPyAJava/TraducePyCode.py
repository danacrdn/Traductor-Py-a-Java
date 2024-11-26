from pyToJavaListener import pyToJavaListener
from pyToJavaParser import *

class TraducePyCode(pyToJavaListener):
    def __init__(self):
        super().__init__()
        self.java_code = ""
        self.indentacion = 0
        self.function_names = []  #Para almacenar los nombres de las funciones
        self.print_statements = []  #Para almacenar los print

    def add_linea(self, line):
        self.java_code += "    " * self.indentacion + line + "\n"

    def enterFunctionDefinition(self, ctx: pyToJavaParser.FunctionDefinitionContext):
        function_name = ctx.ID().getText()
        self.function_names.append(function_name)  # Guardar el nombre de la función
        params = [param.getText() for param in ctx.parameters().parameter()]
        java_params = ", ".join([f"int {p}" for p in params])
        self.add_linea(f"    public static int {function_name}({java_params}) " + "{")
        self.indentacion += 2

    def exitFunctionDefinition(self, ctx: pyToJavaParser.FunctionDefinitionContext):
        self.indentacion -= 1
        self.add_linea("}")

    def enterAssignment(self, ctx: pyToJavaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expression = ctx.expression().getText()
        self.add_linea(f"int {var_name} = {expression};")

    def enterReturnStatement(self, ctx: pyToJavaParser.ReturnStatementContext):
        return_expression = ctx.expression().getText()
        self.add_linea(f"return {return_expression};")

    def enterPrintStatement(self, ctx: pyToJavaParser.PrintStatementContext):
        expression = ctx.expression().getText()
        self.print_statements.append(expression)  # Guardamos las expresiones de print

    # Método para generar las llamadas al main
    def generate_main_calls(self):
        main_calls = []
        for func_name in self.function_names:
            main_calls.append(f"        System.out.println({func_name}(5, 6));")

        return "\n".join(main_calls) + "\n"

    def generate_java_class(self):
        main_method = (
            "    public static void main(String[] args) {\n"
            + self.generate_main_calls()
            + "    }\n"
        )
        return (
            "public class Main {\n"
            + self.java_code
            + main_method
            + "}\n"
        )

