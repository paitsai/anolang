# Generated from ./antlrgen/Anolang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AnolangParser import AnolangParser
else:
    from AnolangParser import AnolangParser

# This class defines a complete generic visitor for a parse tree produced by AnolangParser.

class AnolangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AnolangParser#ano_program.
    def visitAno_program(self, ctx:AnolangParser.Ano_programContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#definition.
    def visitDefinition(self, ctx:AnolangParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#ival.
    def visitIval(self, ctx:AnolangParser.IvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#statement.
    def visitStatement(self, ctx:AnolangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#nullstmt.
    def visitNullstmt(self, ctx:AnolangParser.NullstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#expressionstmt.
    def visitExpressionstmt(self, ctx:AnolangParser.ExpressionstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#blockstmt.
    def visitBlockstmt(self, ctx:AnolangParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#returnstmt.
    def visitReturnstmt(self, ctx:AnolangParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#gotostmt.
    def visitGotostmt(self, ctx:AnolangParser.GotostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#switchstmt.
    def visitSwitchstmt(self, ctx:AnolangParser.SwitchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#whilestmt.
    def visitWhilestmt(self, ctx:AnolangParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#ifstmt.
    def visitIfstmt(self, ctx:AnolangParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#casestmt.
    def visitCasestmt(self, ctx:AnolangParser.CasestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#externsmt.
    def visitExternsmt(self, ctx:AnolangParser.ExternsmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#autosmt.
    def visitAutosmt(self, ctx:AnolangParser.AutosmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#rvalue.
    def visitRvalue(self, ctx:AnolangParser.RvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#ternary.
    def visitTernary(self, ctx:AnolangParser.TernaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#comparison.
    def visitComparison(self, ctx:AnolangParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#assignment.
    def visitAssignment(self, ctx:AnolangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#expression.
    def visitExpression(self, ctx:AnolangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#functioninvocation.
    def visitFunctioninvocation(self, ctx:AnolangParser.FunctioninvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#functionparameters.
    def visitFunctionparameters(self, ctx:AnolangParser.FunctionparametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#assign.
    def visitAssign(self, ctx:AnolangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#incdec.
    def visitIncdec(self, ctx:AnolangParser.IncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#unary.
    def visitUnary(self, ctx:AnolangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#binary.
    def visitBinary(self, ctx:AnolangParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#lvalue.
    def visitLvalue(self, ctx:AnolangParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#constant.
    def visitConstant(self, ctx:AnolangParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnolangParser#identity.
    def visitIdentity(self, ctx:AnolangParser.IdentityContext):
        return self.visitChildren(ctx)



del AnolangParser