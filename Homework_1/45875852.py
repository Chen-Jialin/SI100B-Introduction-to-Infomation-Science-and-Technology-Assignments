import sys
string = sys.stdin.read()
lis = string.split('\n')
matrix = []
for i in lis:
    matrix.append(i.split())

def horizontal(matrix):
    line = 0
    line_menber = 0
    for i in range(len(matrix)):
        for l in matrix[i]:
            if l == 'x':
                line_menber += 1
                if line_menber == 2:
                    line += 1
            else:
                line_menber = 0
        line_menber = 0
    line_menber = 0
    return line

def vertical(matrix):
    line = 0
    line_menber = 0
    for i in range(len(matrix[1])):
        for l in range(len(matrix)):
            if matrix[l][i] == 'x':
                line_menber += 1
                if line_menber == 2:
                    line += 1
            else:
                line_menber = 0
        line_menber = 0
    line_menber = 0
    return line

if string == '':
    print('0 0')
else:
    print(str(horizontal(matrix)) + ' ' + str(vertical(matrix)))
#print(str(lines_horizontal(matrix)))
