'''''
author = eduardo
'''''


def main():
    print("Implementacion de conmpilador K* \n"
          "Semestre 2 2015 Compiladores \n")
    import scanner.lexer as lexer
    lex = lexer.lexer()
    lex.input("x_34 ::= 3 * , ; * > 4 + 5")
    # Tokenize
    while True:
        tok = lex.token()
        if not tok:
            break  # No more input
        print(tok.type, tok.value, tok.lineno, tok.lexpos)


if __name__ == "__main__":
    main()
