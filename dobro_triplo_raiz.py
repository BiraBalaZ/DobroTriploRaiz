nomeAluno = str(input('Digite aqui o nome do aluno:\n>>>'))

n1 = float(input('Digite a primeira nota do aluno {}: \n >>>'.format(nomeAluno)))
n2 = float(input('Digite a segunda nota do aluno {}: \n >>>'.format(nomeAluno)))
n3 = float(input('Digite a terceira nota do aluno {}: \n >>>'.format(nomeAluno)))
n4 = float(input('Digite a quarta nota do aluno {}: \n >>>'.format(nomeAluno)))

media = [(n1 + n2 + n3 + n4) / 2]

print(f'Com as notas {n1}, {n2}, {n3} e {n4}; A média do aluno {nomeAluno} é {media}')