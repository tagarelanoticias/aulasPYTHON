pessoa = {
    'nome':'pep',
    'idade':55,
    'profissão':'dasanvolvedor'
}

novaChave = input('digite um novo campo')
novoValor = input('informe o valor do ponto novo')

pessoa[novaChave] = novoValor

for chave in pessoa:
    print(f'{chave}:{pessoa.get(chave)}')