# In this script we will try to compile a python script through various stages:
# 1. Lexical Ananlysis--->Semantic Analysis:Generates AST--->generating bytecode for AST
from io import StringIO
import tokenize
import ast
from visast import visualise
import dis

code = '''
def calculate(x):
    return x * 2
calculate(5)
'''

def show_tokens(code):
    for tok in tokenize.generate_tokens(StringIO(code).readline):
        token_name = tokenize.tok_name[tok.type]
        if not (token_name == "NL" or token_name == "NEWLINE"):
            print(f"{token_name:<12} {tok.string:<12} {tok.start} {tok.end}")

# 1. Tokenizer
show_tokens(code)

# 2. AST
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

visualise.graph(tree)

# 3. Bytecode
bytecode = compile(tree, '<string>', 'exec')
print(dis.dis(bytecode))