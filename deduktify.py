import glob

def deduktify(s):
    res = "def content := "
    end = ""
    for c in s:
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
            res += "String.cons Char." + c + " ("
            end += ")"
        elif c == " ":
            res += "String.cons Char.space ("
            end += ")"
        elif c == ",":
            res += "String.cons Char.comma ("
            end += ")"
        elif c == ";":
            res += "String.cons Char.semicolon ("
            end += ")"
        elif c == ":":
            res += "String.cons Char.colon ("
            end += ")"
        elif c == "\n":
            res += "String.cons Char.new_line ("
            end += ")"
        elif c == ".":
            res += "String.cons Char.dot ("
            end += ")"
        elif c == "-":
            res += "String.cons Char.minus ("
            end += ")"
        elif c == "[":
            res += "String.cons Char.open_sq ("
            end += ")"
        elif c == "]":
            res += "String.cons Char.close_sq ("
            end += ")"
        else:
            print("UNEXPECTED CHARACTER" + c)
    return (res + "String.end" + end + '.')

all_files = glob.glob('*.txt')
for f in all_files:
    content = open(f, "r")
    dk_filename = f[:-3] + "dk"
    dk_content = open(dk_filename, 'w')
    string_of_file = content.read()
    dk_content.write(deduktify(string_of_file))
    content.close()
    dk_content.close()
