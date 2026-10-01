'''
Python Architecture:
    ->it explains how python executes our program (.py file into output)

1)Source file(.py)->Program written in plain text(types characters using keyboard)

2)Lexing/Tokenisation->breaks the source code into a sequence of Tokens
                     ->Tokens are individual unit of code(identifier,keyword,literal,operator,seprator)
3)parsing ->checks if seq of tokens is Gramatically valid or not
          ->if valid -> its builds AST(abstract syntax tree)
          ->AST Representation of our code in tree like structure
4)Compilation ->process of converting into AST into Bytecode
              ->Cpython stores bytecoode(.pyc files) inside folder named as  __pycache__
              ->later it helps in faster loading on same machine and same python version
5)module loading (import system):
             ->During execution/importing, module loader loads .py file or .pyc file and creates "code objects" in memory
             ->Code obj=(compiled bytecode +metadata) which is executed by PVM
6)PVM ->





                    
'''