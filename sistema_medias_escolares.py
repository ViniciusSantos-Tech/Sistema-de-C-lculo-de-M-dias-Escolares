import pandas as pd

Notas = {
    'Materias': ["Portugues", "Matemática", "Geometria", "Geografia"],
    '1 Bimestre': ["6.0", "7.0", "9.0", "10.0"],
    '2 Bimestre': ["5.0", "6.0", "4.0", "7.0"],
    '3 Bimestre': ["1.0", "8.0", "6.0", "6.9"],
    '4 Bimestre': ["7.0", "9.0", "7.5", "5.0"],
}

Planilha = pd.DataFrame(Notas)

for bimestre in ['1 Bimestre', '2 Bimestre', '3 Bimestre', '4 Bimestre']:
    Planilha[bimestre] = Planilha[bimestre].astype(float)


Planilha['Média Final'] = Planilha[['1 Bimestre', '2 Bimestre', '3 Bimestre', '4 Bimestre']].mean(axis=1)

print(Planilha)

#Feito por Vinicius Santos-Tech
