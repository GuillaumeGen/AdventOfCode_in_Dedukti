#! /usr/bin/env python3

import glob

char_dico = {}
for i in range(48, 58):
    char_dico[chr(i)] = chr(i)
for i in range(65, 91):
    char_dico[chr(i)] = chr(i)
for i in range(97, 123):
    char_dico[chr(i)] = chr(i)
char_dico[" "] = "space"
char_dico[","] = "comma"
char_dico[";"] = "semicolon"
char_dico[":"] = "colon"
char_dico["\n"] = "new_line"
char_dico["."] = "dot"
char_dico["-"] = "minus"
char_dico["["] = "open_sq"
char_dico["]"] = "close_sq"
char_dico["*"] = "asterisk"
char_dico["/"] = "slash"
char_dico["%"] = "percent"
char_dico["$"] = "dollar"
char_dico["#"] = "hash"
char_dico["@"] = "at"
char_dico["&"] = "and"
char_dico["+"] = "plus"
char_dico["="] = "equal"
char_dico["|"] = "pipe"

def deduktify(s):
    res = "def content := "
    for c in s:
        if c in char_dico:
            res += "String.cons Char." + char_dico[c] + " ("
        else:
            print("UNEXPECTED CHARACTER" + c)
    return (res + "String.end" + (")" * len(s)) + '.')

char_dk = open("Lib/Char.dk", 'w')
char_dk.write("""tt : Base.type.
TT : Type.
[] Base.El tt --> TT.

""")
for x in char_dico.values():
    char_dk.write(x + " : TT.\n")
char_dk.write("""

def eq : TT -> TT -> Bool.T.
""")
for x in char_dico.values():
    for y in char_dico.values():
        char_dk.write("[] eq " + x + " " + y + " --> Bool.")
        if x == y:
            char_dk.write("true.\n")
        else:
            char_dk.write("false.\n")
char_dk.write("""
def Eq : Eq.T tt := Eq.Cons tt eq.

def is_digit : TT -> Bool.T.
""")
for (k, x) in char_dico.items():
    char_dk.write("[] is_digit " + x + " --> Bool.")
    if ord(k) in range(48, 58):
        char_dk.write("true.\n")
    else:
        char_dk.write("false.\n")

all_files = glob.glob('*/Inputs/*.txt')
for f in all_files:
    content = open(f, "r")
    dk_filename = f[:-3] + "dk"
    dk_content = open(dk_filename, 'w')
    string_of_file = content.read()
    if string_of_file[-1] == "\n":
        string_of_file = string_of_file[:-1]
    dk_content.write(deduktify(string_of_file))
    content.close()
    dk_content.close()
