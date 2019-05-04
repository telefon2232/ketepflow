def handler_line(text):
    mas_line=[]
    text=text.split('\n')
    for line in text:
        line=line.split('/')

        line=line[-1]
        line=line.split('.')
        line=line[0]
        mas_line.append(line)
    return mas_line
