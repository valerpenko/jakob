def line_compile(line):
    i=line.find("//")
    if i!=-1:
        [left,right]=line.split("//")
        new_line = left.replace("->", ".")
        new_line = new_line + "//" + right
    else:
        new_line=line.replace("->", ".")
    return new_line
line=input()
while line!="":
    print(line_compile(line)
    line=input()