'''
python architecture:
    -it explains how python executes our program within (.py) file into
     output.

     1.Source files(.py):
         program written in plain text(types character using keyword)
         
     2.lexical/tokenisation:
         -breaks the source code intp a sequence of tokens
         -tokens are individual unit of code(identifier,keyword,literal,
          operator,seprator)
          
     3.paring
         -checks if seq of tokens is gramatically valid or not
         -if valid->its builds AST(abstract syntax tree)
     4.Compilation:
         process of converting into AST into Bytecode
         ->cpython stores bytecode(.py files) inside folder names as _pycache_
         ->later it helps in faster loading on same machine and same python
          version
          
     5.module loading(import system):
         -during the execution/importing, module loader loads .py file
          or .pyc files and creates "code objects" in memory.
         -code obj=(compiled bytecode +metadatta) which os executed by PVM.
         
     6.PVM-python vertual machine:
         -executes engine that runs bytecode
         -and generates the output.
          
    python is platform indeppendent?
        the same .py file can be run on windows, linux, mac or android but
        they shud have installed python interpreter.

--------------------------------------------------------------------------------------
Package Attecture->explains how python files,folders are structed into a package

    MODULE->single .py file
          ->contains variables, function, classes
          ->represents a reusable unit of code

    2 types:
        -Inbuilt modules
        eg:keyword, math, random, os, json, pickle

        -Userdefined modules:
        eg:sample.py demo.py

----------------------------------------------------------------------------------
PACKAGES->A folder that contains multiple modules and it contains __init__.py
          Note1:__init__.py file indicates that a particular folder is to bee treated as a python package(highly recommended)

          Note2:When a package or module of that package is imported to another module,__init__.py file will be the 1st thing to be executed
          or
          When the module of that package id directly executed, __init__.py will be executed first

          Note3:Any package level initialisation , configurations, importing can be written in __init__.py
==================================================================================
'''
