def criar_conta(contas):
    codigo = input('Código: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    saldo = float(input('Saldo inicial: '))
    ano_nasc = input('Data de Nascimento (dd/mm/aaaa): ')
    cpf = input('CPF: ')
    cep = input('CEP: ')
    chave_pix = input('Chave PIX: ')
    contas.append((codigo, nome, idade, saldo, ano_nasc, cpf, cep, chave_pix))
    return contas

def alterar_dados(contas):
    codigo_desejado = input('Qual o Código?')
    for i, conta in enumerate(contas):
        codigo, nome, idade, saldo, ano_nasc, cpf, cep, chave_pix = conta
        if codigo == codigo_desejado:
            print(f'Conta: {codigo}, Nome: {nome}, Idade: {idade}, Saldo: {saldo}, Data de Nascimento: {ano_nasc}, CPF: {cpf}, CEP: {cep}, Chave PIX: {chave_pix}')  # Mostrando chave_pix
            novonome = input('Digite seu novo nome: ')
            novoCep = input('Digite Seu novo endereço: ')

            confirma = int(input('Para alterar, digite 1 ou 0 para ignorar? '))
            if confirma == 1:
                contas[i] = (codigo, novonome, idade, saldo, ano_nasc, cpf, novoCep, chave_pix)
                print('Dados Alterados com Sucesso!')
                print(f'Conta: {codigo}, Nome: {novonome}, Idade: {idade}, Saldo: {saldo}, Data de Nascimento: {ano_nasc}, CPF: {cpf}, CEP: {novoCep}, Chave PIX: {chave_pix}')
            break
    else:
        print(f'Conta com o código {codigo_desejado} não foi encontrada')
    return contas

def excluir_conta(contas):
    codigo_desejado = input('Qual o Código?')
    for i, conta in enumerate(contas):
        codigo, nome, idade, saldo, ano_nasc, cpf, cep, chave_pix = conta  
        if codigo == codigo_desejado:
            print(f'Conta: {codigo}, Nome: {nome}, Idade: {idade}, Saldo: {saldo}, Data de Nascimento: {ano_nasc}, CPF: {cpf}, CEP: {cep}, Chave PIX: {chave_pix}')
            excluir = int(input('Para excluir, digite 1 ou 0 para ignorar? '))
            if excluir == 1:
                del contas[i]
                print(f'Conta com o código {codigo} excluída com sucesso!')
            break
    else:
        print(f'Conta com o código {codigo_desejado} não foi encontrada')
    return contas

def consultar_conta(contas):
    codigo_desejado = input('Qual o Código?')
    for conta in contas:
        codigo, nome, idade, saldo, ano_nasc, cpf, cep, chave_pix = conta
        if codigo == codigo_desejado:
            print(f'Conta: {codigo}, Nome: {nome}, Idade: {idade}, Saldo: {saldo}, Data de Nascimento: {ano_nasc}, CPF: {cpf}, CEP: {cep}, Chave PIX: {chave_pix}')
            excluir = int(input('Para alterar, digite 1 ou 0 para ignorar? '))
    else:
        print(f'Conta com o código {codigo_desejado} não foi encontrada')
    return contas

def listar_contas(contas):
    if len(contas) == 0:
        print('Nenhuma pessoa cadastrada!')
    else:
        for conta in contas:
            codigo, nome, idade, saldo, ano_nasc, cpf, cep, chave_pix = conta  
            print(f'Conta: {codigo}, Nome: {nome}, Idade: {idade}, Saldo: {saldo}, Data de Nascimento: {ano_nasc}, CPF: {cpf}, CEP: {cep}, Chave PIX: {chave_pix}')
    return contas

def visualizar_saldo(contas):
    codigo_desejado = input('Qual o Código da Conta? ')
    for conta in contas:
        codigo, _, _, saldo, _, _, _, _ = conta  
        if codigo == codigo_desejado:
            print(f'Saldo da conta {codigo}: R${saldo:.2f}')
            return contas
    print(f'Conta com o código {codigo_desejado} não foi encontrada')
    return contas


def transferencia_pix(contas):
    origem = input('Digite o código da conta de origem: ')
    destino = input('Digite o código da conta de destino: ')
    valor = float(input('Digite o valor a ser transferido: '))

    conta_origem = None
    conta_destino = None

    # Procurar contas de origem e destino
    for conta in contas:
        codigo, *_ = conta
        if codigo == origem:
            conta_origem = conta
        elif codigo == destino:
            conta_destino = conta

    # Verificar se ambas as contas foram encontradas
    if conta_origem is None or conta_destino is None:
        print('Conta de origem ou destino não encontrada.')
        return contas

    # Desempacotando informações das contas
    _, nome_origem, _, saldo_origem, *_ = conta_origem
    _, nome_destino, _, saldo_destino, *_ = conta_destino

    # Verificar saldo da conta de origem
    if saldo_origem < valor:
        print('Saldo insuficiente.')
        return contas

    # Realizar a transferência
    novo_saldo_origem = saldo_origem - valor
    novo_saldo_destino = saldo_destino + valor

    # Atualizar saldos nas contas
    contas[contas.index(conta_origem)] = (origem, nome_origem, novo_saldo_origem)
    contas[contas.index(conta_destino)] = (destino, nome_destino, novo_saldo_destino)

    print(f'Transferência de R${valor:.2f} realizada com sucesso de {nome_origem} para {nome_destino}.')
    return contas

def main():
    contas_list = []
    opcao = 1
    while opcao != 0:
        print('''Escolha uma opcao:
        0. Sair do Sistema
        1. Criar Conta
        2. Alterar Dados
        3. Excluir Conta
        4. Consultar Conta
        5. Mostrar Contas
        6. Visualizar Saldo
        7. Pix''')
        opcao = int(input('Digite a opcao desejada: '))
        if opcao == 1:
            contas_list = criar_conta(contas_list)
        elif opcao == 2:
            contas_list = alterar_dados(contas_list)
        elif opcao == 3:
            contas_list = excluir_conta(contas_list)
        elif opcao == 4:
            contas_list = consultar_conta(contas_list)
        elif opcao == 5:
            listar_contas(contas_list)
        elif opcao == 6:
            contas_list = visualizar_saldo(contas_list)
        elif opcao == 7:
            contas_list = transferencia_pix(contas_list)
        else:
            print('Obrigado por acessar nosso sistema!')
            break

if __name__ == "__main__":
    main()