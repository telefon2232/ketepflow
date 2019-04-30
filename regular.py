def handler_line(text):
    line_mas=[]
    for line in text:
        line = line.split('/')
        line = line[-1]
        line = line.split('.')[0]
        line_mas.append(line)
    if line_mas[-1]=='':
        line_mas=line_mas[:-1]
    return line_mas