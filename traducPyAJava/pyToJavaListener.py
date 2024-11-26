# Generated from pyToJava.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pyToJavaParser import pyToJavaParser
else:
    from pyToJavaParser import pyToJavaParser

# This class defines a complete listener for a parse tree produced by pyToJavaParser.
class pyToJavaListener(ParseTreeListener):

    # Enter a parse tree produced by pyToJavaParser#program.
    def enterProgram(self, ctx:pyToJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#program.
    def exitProgram(self, ctx:pyToJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:pyToJavaParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:pyToJavaParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#parameters.
    def enterParameters(self, ctx:pyToJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#parameters.
    def exitParameters(self, ctx:pyToJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#parameter.
    def enterParameter(self, ctx:pyToJavaParser.ParameterContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#parameter.
    def exitParameter(self, ctx:pyToJavaParser.ParameterContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#block.
    def enterBlock(self, ctx:pyToJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#block.
    def exitBlock(self, ctx:pyToJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#statement.
    def enterStatement(self, ctx:pyToJavaParser.StatementContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#statement.
    def exitStatement(self, ctx:pyToJavaParser.StatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#assignment.
    def enterAssignment(self, ctx:pyToJavaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#assignment.
    def exitAssignment(self, ctx:pyToJavaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#returnStatement.
    def enterReturnStatement(self, ctx:pyToJavaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#returnStatement.
    def exitReturnStatement(self, ctx:pyToJavaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#printStatement.
    def enterPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#printStatement.
    def exitPrintStatement(self, ctx:pyToJavaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#IntExpression.
    def enterIntExpression(self, ctx:pyToJavaParser.IntExpressionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#IntExpression.
    def exitIntExpression(self, ctx:pyToJavaParser.IntExpressionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#IdExpression.
    def enterIdExpression(self, ctx:pyToJavaParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#IdExpression.
    def exitIdExpression(self, ctx:pyToJavaParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#SubExpression.
    def enterSubExpression(self, ctx:pyToJavaParser.SubExpressionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#SubExpression.
    def exitSubExpression(self, ctx:pyToJavaParser.SubExpressionContext):
        pass


    # Enter a parse tree produced by pyToJavaParser#MulExpression.
    def enterMulExpression(self, ctx:pyToJavaParser.MulExpressionContext):
        pass

    # Exit a parse tree produced by pyToJavaParser#MulExpression.
    def exitMulExpression(self, ctx:pyToJavaParser.MulExpressionContext):
        pass


