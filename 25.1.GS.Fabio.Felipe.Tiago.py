quantidade = int(input("Quantos desastres foram registrados? "))

for i in range(quantidade):
    print(f"\nDados do Desastre {i + 1}")

    tipo = input("Tipo de desastre: ")
    pais = input("Em qual país: ")
    cidade = input("Em qual cidade: ")
    bairro = input("Em qual bairro: ")
    rua = input("Em qual rua: ")

    while True:
        total = int(input("Quantidade TOTAL de pessoas afetadas: "))
        qtd_criancas_afet = int(input("Quantidade de crianças: "))
        qtd_adultos_afet = int(input("Quantidade de adultos: "))
        qtd_idosos_afet = int(input("Quantidade de idosos: "))
        qtd_mobilidade_afet = int(input("Quantidade de pessoas com mobilidade reduzida: "))
        qtd_feridos_afet = int(input("Quantidade de feridos: "))

        soma = qtd_criancas_afet + qtd_adultos_afet + qtd_idosos_afet + qtd_mobilidade_afet + qtd_feridos_afet

        if soma == total:
            print("Tudo certo")
        else:
            print("\nERRO: A soma das categorias NÃO corresponde ao total de pessoas afetadas.")
            print(f"\nSoma das categorias = {soma}, mas o total informado foi {total}")
            print("\nPor favor, preencha os dados corretamente")
            break






