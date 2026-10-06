# ==============================================================================
# ESTRUTURA DE DADOS (LISTAS PARALELAS)
# Cada índice (0, 1, 2...) em todas as listas corresponde ao mesmo atendimento.
# Exemplo: clientes[0], servicos[0] e valores[0] pertencem ao 1º atendimento.
# ==============================================================================
clientes = []
servicos = []
valores = []
situacoes = []

# ==============================================================================
# PROGRAMA PRINCIPAL - LOOP DO MENU
# O 'while True' mantém o sistema rodando continuamente até o usuário escolher '0'.
# ==============================================================================
while True:
    # Exibição visual do menu de opções
    print("\n" + "="*35)
    print("       MENU DE OPÇÕES")
    print("="*35)
    print("1 - Cadastrar atendimento")
    print("2 - Listar atendimentos e resumo")
    print("3 - Inserir atendimento por posição")
    print("4 - Remover registro por nome")
    print("5 - Remover registro por posição")
    print("6 - Verificar quantidade de elementos")
    print("0 - Sair")
    print("="*35)

    # Captura a opção do usuário. O .strip() remove espaços vazios acidentais.
    opcao = input("Escolha uma opção: ").strip()

    # --------------------------------------------------------------------------
    # OPÇÃO 1: CADASTRAR ATENDIMENTO (Adiciona ao final das listas)
    # --------------------------------------------------------------------------
    if opcao == '1':
        print("\n--- CADASTRAR ATENDIMENTO ---")
        
        # Validação do Nome: garante que não fique em branco
        nome = input("Nome do cliente: ").strip()
        while not nome:
            print(" O nome do cliente não pode estar vazio.")
            nome = input("Nome do cliente: ").strip()

        # Validação do Serviço: garante que não fique em branco
        servico = input("Tipo de serviço realizado (ex: Formatação, Limpeza): ").strip()
        while not servico:
            print(" O tipo de serviço não pode estar vazio.")
            servico = input("Tipo de serviço realizado: ").strip()

        # Validação do Valor: usa 'try/except' para evitar erros de digitação (ex: letras)
        while True:
            try:
                val = float(input("Valor do serviço (R$): "))
                if val < 0:
                    print(" O valor não pode ser negativo.")
                    continue  # Volta para o início deste mini-loop
                break  # Sai do mini-loop se o valor for um número válido
            except ValueError:
                # Captura o erro caso o usuário digite texto no lugar de números
                print(" Entrada inválida! Digite um número válido para o valor.")

        # Validação da Situação: aceita apenas 1 (Concluído) ou 0 (Não concluído)
        while True:
            try:
                sit_num = int(input("Situação do serviço (1 - Concluído | 0 - Não concluído): "))
                if sit_num in [0, 1]:
                    # Converte o número 1 ou 0 para o texto correspondente
                    sit_str = "Concluído" if sit_num == 1 else "Não concluído"
                    break  # Opção válida, sai do mini-loop
                else:
                    print(" Digite apenas 1 para Concluído ou 0 para Não concluído.")
            except ValueError:
                print(" Entrada inválida! Digite apenas o número 1 ou 0.")

        # O método .append() insere os novos dados no final de cada lista correspondente
        clientes.append(nome)
        servicos.append(servico)
        valores.append(val)
        situacoes.append(sit_str)

        print("\n Atendimento cadastrado com sucesso!")

    # --------------------------------------------------------------------------
    # OPÇÃO 2: LISTAR ATENDIMENTOS E EXIBIR RESUMO (Explicação Detalhada)
    # --------------------------------------------------------------------------
    elif opcao == '2':
        print("\n" + "="*60)
        print("LISTA DE ATENDIMENTOS (ATUALIZADA)")
        print("="*60)

        # Verifica se a lista está vazia
        if not clientes:
            print("Nenhum registro encontrado.")
            print("="*60)
        else:
            # 1. IMPRESSÃO DO CABEÇALHO DA TABELA
            # Os comandos ':<largura' alinham o texto à esquerda reservando um espaço fixo:
            # - '{'#':<3}'  -> Reserva 3 caracteres para a coluna do número da linha (#)
            # - '{'Cliente':<15}' -> Reserva 15 caracteres para o nome do cliente
            # - '{'Serviço':<20}' -> Reserva 20 caracteres para a descrição do serviço
            # - '{'Valor':<10}'   -> Reserva 10 caracteres para o valor do serviço
            print(f"{'#':<3} | {'Cliente':<15} | {'Serviço':<20} | {'Valor':<10} | {'Situação'}")
            print("-" * 60)  # Imprime uma linha horizontal separadora com 60 traços

            # 2. INICIALIZAÇÃO DOS ACUMULADORES E CONTADORES
            total_servicos = 0.0  # ACUMULADOR: guardará a soma de todos os valores ($)
            concluidos = 0        # CONTADOR: contaremos quantas entregas foram 'Concluído'
            nao_concluidos = 0    # CONTADOR: contaremos quantas entregas foram 'Não concluído'

            # 3. LOOP 'FOR' PARA PERCORRER TODAS AS LISTAS SIMULTANEAMENTE
            # len(clientes) retorna o total de cadastros (ex: 3).
            # range(3) gera a sequência de índices: 0, 1, 2.
            for i in range(len(clientes)):
                
                # Exibe a linha do cliente 'i' mantendo a mesma largura do cabeçalho:
                # - 'i + 1': Mostra 1, 2, 3... em vez de 0, 1, 2... para o usuário
                # - 'valores[i]:<7.2f': Formata o valor com 2 casas decimais (ex: 80.00)
                print(f"{i+1:<3} | {clientes[i]:<15} | {servicos[i]:<20} | R$ {valores[i]:<7.2f} | {situacoes[i]}")
                
                # ACUMULADOR: Adiciona o valor da linha atual ao total geral acumulado
                # Equivalente a: total_servicos = total_servicos + valores[i]
                total_servicos += valores[i]
                
                # CONTADOR: Analisa a situação atual e incrementa o contador correspondente em +1
                if situacoes[i] == "Concluído":
                    concluidos += 1
                else:
                    nao_concluidos += 1

            # 4. IMPRESSÃO DO RESUMO E ESTATÍSTICAS FINAIS
            print("-" * 60)
            print(f"Total de atendimentos : {len(clientes)}")      # Total de elementos
            print(f"Total de serviços     : R$ {total_servicos:.2f}") # Resultado do acumulador
            print(f"Serviços concluídos   : {concluidos}")          # Resultado do contador 1
            print(f"Serviços não concluídos: {nao_concluidos}")      # Resultado do contador 2
            print("="*60)

    # --------------------------------------------------------------------------
    # OPÇÃO 3: INSERIR EM UMA POSIÇÃO ESPECÍFICA (.insert)
    # --------------------------------------------------------------------------
    elif opcao == '3':
        print("\n--- INSERIR ATENDIMENTO EM POSIÇÃO ESPECÍFICA ---")
        
        if len(clientes) == 0:
            print("Nenhum atendimento cadastrado. O registro será inserido na posição 1.")
            posicao = 0
        else:
            # Pede a posição e garante que esteja dentro dos limites da lista
            while True:
                try:
                    pos = int(input(f"Digite a posição desejada (1 a {len(clientes) + 1}): "))
                    if 1 <= pos <= len(clientes) + 1:
                        posicao = pos - 1  # Subtrai 1 para converter a posição humana em índice (0, 1, 2...)
                        break
                    else:
                        print(f" Posição fora do intervalo! Informe um valor entre 1 e {len(clientes) + 1}.")
                except ValueError:
                    print(" Por favor, digite um número inteiro válido.")

        # Solicitação dos dados para inserção
        nome = input("Nome do cliente: ").strip()
        while not nome:
            nome = input("Nome do cliente não pode ser vazio: ").strip()

        servico = input("Tipo de serviço realizado: ").strip()
        while not servico:
            servico = input("Tipo de serviço não pode ser vazio: ").strip()

        while True:
            try:
                val = float(input("Valor do serviço (R$): "))
                if val >= 0:
                    break
                print(" O valor não pode ser negativo.")
            except ValueError:
                print(" Entrada inválida!")

        while True:
            try:
                sit_num = int(input("Situação (1 - Concluído | 0 - Não concluído): "))
                if sit_num in [0, 1]:
                    sit_str = "Concluído" if sit_num == 1 else "Não concluído"
                    break
                print(" Opção inválida!")
            except ValueError:
                print(" Entrada inválida!")

        # O método .insert(índice, valor) coloca o elemento exatamente na posição solicitada
        # e "empurra" os itens seguintes uma posição para trás.
        clientes.insert(posicao, nome)
        servicos.insert(posicao, servico)
        valores.insert(posicao, val)
        situacoes.insert(posicao, sit_str)

        print(f"\n Atendimento inserido na posição {posicao + 1} com sucesso!")

    # --------------------------------------------------------------------------
    # OPÇÃO 4: REMOVER REGISTRO POR NOME (.index, .remove e .pop)
    # --------------------------------------------------------------------------
    elif opcao == '4':
        print("\n--- REMOVER REGISTRO POR NOME DO CLIENTE ---")
        if not clientes:
            print(" A lista está vazia! Não há registros para remover.")
        else:
            nome_busca = input("Digite o nome do cliente a ser removido: ").strip()

            try:
                # O .index() busca em qual posição (índice) o nome está guardado
                idx = clientes.index(nome_busca)
            except ValueError:
                # Disparado se o nome digitado não for encontrado na lista 'clientes'
                print(f" Cliente '{nome_busca}' não foi encontrado na lista.")
            else:
                # O bloco 'else' executa SOMENTE SE o try não disparou erro (nome foi encontrado!)
                clientes.remove(nome_busca) # Remove o nome pelo próprio texto
                servicos.pop(idx)          # Remove do mesmo índice nas outras listas
                valores.pop(idx)           # Remove do mesmo índice nas outras listas
                situacoes.pop(idx)         # Remove do mesmo índice nas outras listas
                print(f" Registro do cliente '{nome_busca}' removido com sucesso!")
            finally:
                # O 'finally' roda SEMPRE ao final, encontrando ou não o cliente
                print("Operação de busca/remoção por nome concluída.")

    # --------------------------------------------------------------------------
    # OPÇÃO 5: REMOVER REGISTRO POR POSIÇÃO (.pop)
    # --------------------------------------------------------------------------
    elif opcao == '5':
        print("\n--- REMOVER REGISTRO POR POSIÇÃO ---")
        if not clientes:
            print(" A lista está vazia! Não há registros para remover.")
        else:
            try:
                pos = int(input(f"Digite a posição do registro a ser removido (1 a {len(clientes)}): "))
                idx = pos - 1  # Converte a posição digitada para o índice da lista (começando do 0)
                
                # O método .pop(índice) remove o elemento do índice e devolve o valor removido
                cliente_removido = clientes.pop(idx)
                servicos.pop(idx)
                valores.pop(idx)
                situacoes.pop(idx)
                
                print(f" Registro na posição {pos} (Cliente: {cliente_removido}) foi removido com sucesso!")
            except IndexError:
                # Disparado se o usuário digitar uma posição que não existe (ex: digitar 10 quando só há 2 itens)
                print(" Erro: A posição informada não existe na lista!")
            except ValueError:
                # Disparado se digitar letras ou caracteres especiais
                print(" Erro: Digite um número inteiro válido para a posição!")
                
    # --------------------------------------------------------------------------
    # OPÇÃO 6: REMOVER REGISTRO POR VALOR
    # --------------------------------------------------------------------------
    elif opcao == '6':
        print("\n--- REMOVER VALOR ---")
        print(f"Valores:{valores}")

        valor_remover = float(input("Valor para remoção: "))
        if not valor_remover:
            print("Nenhum registro por valor encontrado.")
        else:
            if valor_remover in valores:
                valor_removido = valores.pop(valor_removido)
                servicos.pop(idx)
                valores.pop(idx)
                situacoes.pop(idx)
                valor_total -= valor_remover
                print("\nParabéns, o registro foi removido com sucesso!")
                print(f"Valores registrados atualizados: {valores}\n")
    
    # --------------------------------------------------------------------------
    # OPÇÃO 7: VERIFICAR QUANTIDADE DE ELEMENTOS (len)
    # --------------------------------------------------------------------------
    elif opcao == '6':
        print("\n" + "="*40)
        # O método len() conta o total de elementos existentes na lista
        print(f" Quantidade atual de registros cadastrados: {len(clientes)}")
        print("="*40)

    # --------------------------------------------------------------------------
    # OPÇÃO 0: SAIR DO SISTEMA
    # --------------------------------------------------------------------------
    elif opcao == '0':
        print("\nEncerrando o sistema... Até logo!")
        break  # O 'break' interrompe o ciclo 'while True' e finaliza o programa

    # TRATAMENTO DE OPÇÕES INVÁLIDAS DO MENU
    else:
        print("\n Opção inválida! Por favor, escolha um número do menu de 0 a 6.")
