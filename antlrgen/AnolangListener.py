# Generated from ./antlrgen/Anolang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AnolangParser import AnolangParser
else:
    from AnolangParser import AnolangParser

# This class defines a complete listener for a parse tree produced by AnolangParser.
class AnolangListener(ParseTreeListener):

    # Enter a parse tree produced by AnolangParser#ano_program.
    def enterAno_program(self, ctx:AnolangParser.Ano_programContext):
        pass

    # Exit a parse tree produced by AnolangParser#ano_program.
    def exitAno_program(self, ctx:AnolangParser.Ano_programContext):
        pass


    # Enter a parse tree produced by AnolangParser#definition.
    def enterDefinition(self, ctx:AnolangParser.DefinitionContext):
        pass

    # Exit a parse tree produced by AnolangParser#definition.
    def exitDefinition(self, ctx:AnolangParser.DefinitionContext):
        pass


    # Enter a parse tree produced by AnolangParser#ival.
    def enterIval(self, ctx:AnolangParser.IvalContext):
        pass

    # Exit a parse tree produced by AnolangParser#ival.
    def exitIval(self, ctx:AnolangParser.IvalContext):
        pass


    # Enter a parse tree produced by AnolangParser#statement.
    def enterStatement(self, ctx:AnolangParser.StatementContext):
        pass

    # Exit a parse tree produced by AnolangParser#statement.
    def exitStatement(self, ctx:AnolangParser.StatementContext):
        pass


    # Enter a parse tree produced by AnolangParser#nullstmt.
    def enterNullstmt(self, ctx:AnolangParser.NullstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#nullstmt.
    def exitNullstmt(self, ctx:AnolangParser.NullstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#expressionstmt.
    def enterExpressionstmt(self, ctx:AnolangParser.ExpressionstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#expressionstmt.
    def exitExpressionstmt(self, ctx:AnolangParser.ExpressionstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#blockstmt.
    def enterBlockstmt(self, ctx:AnolangParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#blockstmt.
    def exitBlockstmt(self, ctx:AnolangParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#returnstmt.
    def enterReturnstmt(self, ctx:AnolangParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#returnstmt.
    def exitReturnstmt(self, ctx:AnolangParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#gotostmt.
    def enterGotostmt(self, ctx:AnolangParser.GotostmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#gotostmt.
    def exitGotostmt(self, ctx:AnolangParser.GotostmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#switchstmt.
    def enterSwitchstmt(self, ctx:AnolangParser.SwitchstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#switchstmt.
    def exitSwitchstmt(self, ctx:AnolangParser.SwitchstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#whilestmt.
    def enterWhilestmt(self, ctx:AnolangParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#whilestmt.
    def exitWhilestmt(self, ctx:AnolangParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#ifstmt.
    def enterIfstmt(self, ctx:AnolangParser.IfstmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#ifstmt.
    def exitIfstmt(self, ctx:AnolangParser.IfstmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#casestmt.
    def enterCasestmt(self, ctx:AnolangParser.CasestmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#casestmt.
    def exitCasestmt(self, ctx:AnolangParser.CasestmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#externsmt.
    def enterExternsmt(self, ctx:AnolangParser.ExternsmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#externsmt.
    def exitExternsmt(self, ctx:AnolangParser.ExternsmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#autosmt.
    def enterAutosmt(self, ctx:AnolangParser.AutosmtContext):
        pass

    # Exit a parse tree produced by AnolangParser#autosmt.
    def exitAutosmt(self, ctx:AnolangParser.AutosmtContext):
        pass


    # Enter a parse tree produced by AnolangParser#rvalue.
    def enterRvalue(self, ctx:AnolangParser.RvalueContext):
        pass

    # Exit a parse tree produced by AnolangParser#rvalue.
    def exitRvalue(self, ctx:AnolangParser.RvalueContext):
        pass


    # Enter a parse tree produced by AnolangParser#ternary.
    def enterTernary(self, ctx:AnolangParser.TernaryContext):
        pass

    # Exit a parse tree produced by AnolangParser#ternary.
    def exitTernary(self, ctx:AnolangParser.TernaryContext):
        pass


    # Enter a parse tree produced by AnolangParser#comparison.
    def enterComparison(self, ctx:AnolangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by AnolangParser#comparison.
    def exitComparison(self, ctx:AnolangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by AnolangParser#assignment.
    def enterAssignment(self, ctx:AnolangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AnolangParser#assignment.
    def exitAssignment(self, ctx:AnolangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AnolangParser#expression.
    def enterExpression(self, ctx:AnolangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AnolangParser#expression.
    def exitExpression(self, ctx:AnolangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AnolangParser#functioninvocation.
    def enterFunctioninvocation(self, ctx:AnolangParser.FunctioninvocationContext):
        pass

    # Exit a parse tree produced by AnolangParser#functioninvocation.
    def exitFunctioninvocation(self, ctx:AnolangParser.FunctioninvocationContext):
        pass


    # Enter a parse tree produced by AnolangParser#functionparameters.
    def enterFunctionparameters(self, ctx:AnolangParser.FunctionparametersContext):
        pass

    # Exit a parse tree produced by AnolangParser#functionparameters.
    def exitFunctionparameters(self, ctx:AnolangParser.FunctionparametersContext):
        pass


    # Enter a parse tree produced by AnolangParser#assign.
    def enterAssign(self, ctx:AnolangParser.AssignContext):
        pass

    # Exit a parse tree produced by AnolangParser#assign.
    def exitAssign(self, ctx:AnolangParser.AssignContext):
        pass


    # Enter a parse tree produced by AnolangParser#incdec.
    def enterIncdec(self, ctx:AnolangParser.IncdecContext):
        pass

    # Exit a parse tree produced by AnolangParser#incdec.
    def exitIncdec(self, ctx:AnolangParser.IncdecContext):
        pass


    # Enter a parse tree produced by AnolangParser#unary.
    def enterUnary(self, ctx:AnolangParser.UnaryContext):
        pass

    # Exit a parse tree produced by AnolangParser#unary.
    def exitUnary(self, ctx:AnolangParser.UnaryContext):
        pass


    # Enter a parse tree produced by AnolangParser#binary.
    def enterBinary(self, ctx:AnolangParser.BinaryContext):
        pass

    # Exit a parse tree produced by AnolangParser#binary.
    def exitBinary(self, ctx:AnolangParser.BinaryContext):
        pass


    # Enter a parse tree produced by AnolangParser#lvalue.
    def enterLvalue(self, ctx:AnolangParser.LvalueContext):
        pass

    # Exit a parse tree produced by AnolangParser#lvalue.
    def exitLvalue(self, ctx:AnolangParser.LvalueContext):
        pass


    # Enter a parse tree produced by AnolangParser#constant.
    def enterConstant(self, ctx:AnolangParser.ConstantContext):
        pass

    # Exit a parse tree produced by AnolangParser#constant.
    def exitConstant(self, ctx:AnolangParser.ConstantContext):
        pass


    # Enter a parse tree produced by AnolangParser#identity.
    def enterIdentity(self, ctx:AnolangParser.IdentityContext):
        pass

    # Exit a parse tree produced by AnolangParser#identity.
    def exitIdentity(self, ctx:AnolangParser.IdentityContext):
        pass



del AnolangParser