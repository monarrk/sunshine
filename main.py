from lexer import Lexer
from parser import Parser
from codegen import CodeGen
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("flname")
parser.add_argument("export")
args = parser.parse_args()

fname = f"./{args.flname}"
export = f"./{args.export}"

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
codegen.save_ir(".output.ll")

bashCommand = "llc -filetype=obj .output.ll"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = f"gcc -no-pie .output.o -o {export}"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()