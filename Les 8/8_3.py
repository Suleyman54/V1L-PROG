def code(invoerstring):
    code = ""
    for x in invoerstring:
        z = ord(x) + 3
        code += chr(z)
    return code
print(code('RutteAlkmaarDen Helder'))