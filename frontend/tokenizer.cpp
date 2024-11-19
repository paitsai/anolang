#include <iostream>
#include <vector>
#include <regex>
#include <string>
#include "front.h"

std::vector<Token> Tokenizer::tokenize(std::string& input){
        
        std::vector<Token> tokens;  // 存储分词结果
        std::smatch match;
        std::string content = input;

        // 尝试匹配每一种Token
        while (!content.empty()) {
            // std::cout << "THE REST: " << content << std::endl;
            // 匹配function关键字
            if (std::regex_search(content, match, functionRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::FUNCTION, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配标识符
            if (std::regex_search(content, match, identifierRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::IDENTIFIER, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配左括号
            if (std::regex_search(content, match, lparenRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::LPAREN, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配右括号
            if (std::regex_search(content, match, rparenRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::RPAREN, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配左大括号
            if (std::regex_search(content, match, lbraceRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::LBRACE, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配右大括号
            if (std::regex_search(content, match, rbraceRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::RBRACE, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配逗号
            if (std::regex_search(content, match, commaRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::COMMA, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配字符串字面量
            if (std::regex_search(content, match, stringLiteralRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::STRING_LITERAL, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 匹配空白字符
            if (std::regex_search(content, match, whitespaceRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    content = match.suffix().str();  // 忽略空白字符
                    continue;
                }
            }
            // 匹配未知字符
            if (std::regex_search(content, match, unknownRegex)) {
                auto tmp = match.suffix().str();
                if(content.length() - tmp.length() == match.length()){
                    tokens.push_back({TokenType::UNKNOWN, match.str()});
                    content = match.suffix().str();
                    continue;
                }
            }
            // 如果没有匹配到任何模式，跳出循环
            else {
                break;
            }
        }

        return tokens;
    

}

// Token匹配的正则表达式
const std::regex Tokenizer::functionRegex(R"(\bfunction\b)");
const std::regex Tokenizer::identifierRegex(R"([a-zA-Z_][a-zA-Z0-9_]*)");
const std::regex Tokenizer::lparenRegex(R"(\()");
const std::regex Tokenizer::rparenRegex(R"(\))");
const std::regex Tokenizer::lbraceRegex(R"(\{)");
const std::regex Tokenizer::rbraceRegex(R"(\})");
const std::regex Tokenizer::commaRegex(R"(,)");
const std::regex Tokenizer::stringLiteralRegex(R"("\"[^\"]*\"")");
const std::regex Tokenizer::whitespaceRegex(R"(\s+)");
const std::regex Tokenizer::unknownRegex(R"(.)");

