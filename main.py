from lexer import Lexer
from parser import Parser
from codegen import CodeGen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("flname")
args = parser.parse_args()

fname = f"./{args.flname}"

with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")

print("\nDone! Run\tllc -filetype=obj output.ll\tto build")
print(f"Run\tgcc -no-pie output.o -o output\tto compile")