#include "frontend/front.h"



int main() {
    std::string input = R"(
        function test_fn() 
        {
            println("Hello, happy world! ");
        }
        )";

    try {
        Tokenizer tokenizer;
        std::vector<Token> tokens = tokenizer.tokenize(input);

        // 打印所有token
        for (const auto& token : tokens) {
            std::cout << "Type: ";
            switch (token.type) {
                case TokenType::FUNCTION: std::cout << "FUNCTION"; break;
                case TokenType::IDENTIFIER: std::cout << "IDENTIFIER"; break;
                case TokenType::LPAREN: std::cout << "LPAREN"; break;
                case TokenType::RPAREN: std::cout << "RPAREN"; break;
                case TokenType::LBRACE: std::cout << "LBRACE"; break;
                case TokenType::RBRACE: std::cout << "RBRACE"; break;
                case TokenType::COMMA: std::cout << "COMMA"; break;
                case TokenType::STRING_LITERAL: std::cout << "STRING_LITERAL"; break;
                case TokenType::UNKNOWN: std::cout << "UNKNOWN"; break;
                case TokenType::WHITESPACE: std::cout << "WHITESPACE"; break;
            }
            std::cout << ", Value: " << token.value << std::endl;
        }
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
    }

    return 0;
}