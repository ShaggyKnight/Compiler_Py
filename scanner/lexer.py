'''''
author = eduardo
'''''

# ----------------------------------------------------------------
# lexer.py
#
# Contiene las declaraciones de tokens para el lenguaje
# k*
# ----------------------------------------------------------------

import ply.lex as lex

# Lista de Tokens
tokens = (
    'LETRA',
    'DIGITO',
    'NUMERO',
    'INT',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'VOID',
    'RETURN',
    'SALTO',
    'COMENTARIO',
    'ERROR',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'EXPONENCIACION_2',
    'ASSIGN',
    'PARENT_IZQ',
    'PARENT_DER',
    'CORCH_IZQ',
    'CORCH_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'MENOR',
    'MENIGUAL',
    'MAYOR',
    'MAYIGUAL',
    'IGUALIGUAL',
    'DISTINTO',
    'PUNTOCOMA',
    'COMA',
    'WHITESPACE'
)

# Tokens
# el prefijo t_ indica que define un token
t_LETRA = r'[a-zA-z]'
t_DIGITO = r'[0-9]'
t_NUMERO = r'{DIGITO} | [1-9]{DIGITO}*'
t_ELSE = r'[eE][lL][sS][eE]'
t_IF = r'([iI])([fF])'
t_INT = r'([iI])([nN])([tT])'
t_VOID = r'([vV])([oO])([iI])([dD])'
t_RETURN = r'([rR])([eE])([tT])([uU])([rR])([nN])'
t_WHILE = r'([wW])([hH])([iI])([lL])([eE])'
t_FOR = r'([fF])([oO])([rR])'
t_SALTO = r'\n | \r | \r\n'
InputCharacter = r'[^\n\r]'
multiComment = r'"/#"[^#]~"#/" | "/#" "#"+ "/"  /* "/#"~"#/" */'
lineComment = r'"%" {InputCharacter}* {SALTO}?'
t_WHITESPACE = r'\s'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_ASSIGN = r'\::='
t_PARENT_IZQ = r'\('
t_PARENT_DER = r'\)'
t_CORCH_IZQ = r'\['
t_CORCH_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PUNTOCOMA = r'\;'
t_COMA = r'\,'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MENIGUAL = r'<='
t_MAYIGUAL = r'>='
t_IGUALIGUAL = r'=='
t_DISTINTO = r'!='

# ignorar espacios en blanco
t_ignore = ' {WHITESPACE}'


def t_identificador(t):
    r'([a-z]){LETRA}*_?{LETRA}*{DIGITO}*'
    return (t)


def t_error(t):
    raise SyntaxError("Simbolo desconocido %r" % (t.value[0],))
    print("saltando....", repr(t.value[0]))
    t.lexer.skip(1)


def lexer():
    '''
    Constructor
    :return: lexer compilado
    '''
    return lex.lex()
