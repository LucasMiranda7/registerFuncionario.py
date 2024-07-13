print('Bem vindo a Empresa do Lucas Miranda da Silva') #Mensagem de boas vindas
lista_funcionarios = [] #Lista para adicionar funcionarios
id_global = 4695697 #Valor inicial do ID global de funcionarios. 

#função de cadastrar funcionarios
def cadastrar_funcionario(id): 
  try: #Tentar
    print('-' * 50)
    print('-' * 10, 'MENU CADASTRAR FUNCIONÁRIO', '-' * 12)
    print(f'Id do Funcionário: {id_global}')
    nome = str(input('Por favor entre com o nome do Funcionário: '))
    setor = str(input('Por favor entre com o setor do Funcionário: '))
    salario = float(input('Por favor entre com o salário do Funcionário: '))
    dicionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario} #dicionario/lista
    lista_funcionarios.append(dicionario.copy()) #Adicionar e copiar itens da lista
    print('Funcionário cadastrado com Sucesso!')
    print()
  except: #Execessão, caso algo der errado
    print('Opps! Digite respostas válida. [Nome/Setor/Salário]')
 
#função de consultar funcionarios
def consultar_funcionarios():
  while True:
    print('-' * 50)
    print('-' * 10, 'MENU CONSULTAR FUNCIONÁRIO', '-' * 12)
    print('Escolha a opção desejada:')
    print('1 - Consultar Todos os Funcionários')
    print('2 - Consultar Funcionário por id')
    print('3 - Consultar Funcionário(s) por setor')
    print('4 -Retornar')

    escolha_op = input('>>')
    try: 
      if escolha_op == '1': #Opção 1
        if lista_funcionarios: 
          print('-' * 15)
          for funcionario in lista_funcionarios: #Loop de procura funcionario e sua caractere dentro da Lista.
            print(f'id: {funcionario['id']}')
            print(f'nome: {funcionario['nome']}')
            print(f'setor: {funcionario['setor']}')
            print(f'salário: {funcionario['salario']}')
            print()
            continue #Continua no laço do Painel de consultar.
          print('-' * 15)
        else:
          print('Não há Funcionários cadastrados')

      elif escolha_op == '2': #Opção 2
        id_funcionario = int(input('Digite o id do Funcionario: '))
        print('-'*15)
        for funcionario in lista_funcionarios: #Loop para indetificar o funcionario na lista pelo 'ID'
          if funcionario['id'] == id_funcionario: #indetificar pelo 'ID'
              print(f'id: {funcionario['id']}')
              print(f'nome: {funcionario['nome']}')#Prints: puxa todos os dados do funcionario pelo ID
              print(f'setor: {funcionario['setor']}')
              print(f'salário: {funcionario['salario']}')
              print('-' * 15)
              break #Para e continua no menu de consultar
          return #Retorna os valores
        else:
           print('Id inválido.')
           continue

      elif escolha_op == '3': #Opção 3
        setor_consultar = input('Digite o setor do(s) funcionários(s): ')
        print('-'*15)
        for funcionario in lista_funcionarios: #Loop para indetificar funcionario da lista pelo 'Setor'
         if funcionario['setor'] == setor_consultar: #indetificar pelo 'Setor'
            print(f'id: {funcionario['id']}')
            print(f'nome: {funcionario['nome']}')#Prints:puxa todos os dados do funcionario pelo Setor
            print(f'setor: {funcionario['setor']}')
            print(f'salário: {funcionario['salario']}')
            print()
        if len([funcionario for funcionario in lista_funcionarios if funcionario['setor'] == setor_consultar]) == 0: #Busca todos que são do mesmo setor buscado.
          print('Nenhum funcionário encontrado nesse setor.')
          print('-'*15)
          return #Retorna os valores
        
      elif escolha_op == '4':
        return #Retorna para o menu principal
      else:
        print('Opção inválida.')
      continue
    except:
      print('Opção Inexistente')

#função de remover cadastros de funcionarios
def remover_funcionario():
  try:
   print('-' * 50)
   print('-' *10, 'MENU REMOVER FUNCIONÁRIO', '-' *14)
   id_remover = int(input('Digite o id do funcionario a ser removido:'))
   for funcionario in lista_funcionarios: #Loop para entrar na lista e identificar os funcionarios.
    if funcionario['id'] == id_remover: #Indetificador de ID
      lista_funcionarios.remove(funcionario) #Remove funcionario pelo id.
      print('Funcionario removido com sucesso!')
      return #Retorna o resultado
  except:
   print('Funcionário não indentificado!')

#Menu Principal
while True:
  print('-' * 50)
  print('-' * 17, 'MENU PRINCICPAL', '-' * 16)
  print('Escolha a opção desejada: ')
  print('1 - Cadastrar Funcionários')
  print('2 - Consultar Funcionários(s)')
  print('3 - Remover Funcionário')
  print('4 - Sair')
  opcoes = input('>>')

  if opcoes == '1':
    cadastrar_funcionario(id_global)
    id_global += 1 # A cada 1 novo funcionario, aumenta 1 numero no 'ID'
  elif opcoes == '2':
    consultar_funcionarios()
  elif opcoes == '3':
    remover_funcionario()
  elif opcoes == '4':
    print('Programa Encerrado!')
    break
  else:
    print('Opção inválida. Escolha entre as opções: [1/2/3/4]')