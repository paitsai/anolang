#ifndef FRONT_H
#define FRONT_H

#include <iostream>
#include <vector>
#include <regex>
#include <string>

// Token类型枚举
enum class TokenType {
    FUNCTION,
    IDENTIFIER,
    LPAREN,
    RPAREN,
    LBRACE,
    RBRACE,
    COMMA,
    STRING_LITERAL,
    UNKNOWN,
    WHITESPACE
};

// Token结构体
struct Token {
    TokenType type;
    std::string value;
};

// Tokenizer类
class Tokenizer {
public:
    // 分词函数
    std::vector<Token> tokenize(std::string& input);

    // Token匹配规则（静态常量正则表达式）
    static const std::regex functionRegex;
    static const std::regex identifierRegex;
    static const std::regex lparenRegex;
    static const std::regex rparenRegex;
    static const std::regex lbraceRegex;
    static const std::regex rbraceRegex;
    static const std::regex commaRegex;
    static const std::regex stringLiteralRegex;
    static const std::regex whitespaceRegex;
    static const std::regex unknownRegex;
};

#endif // TOKENIZER_H
