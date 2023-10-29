import json
import random
import os

if not os.path.exists("cadastros.json") : 
      with open("cadastros.json", "w") as file :
            json.dump([], file)
                 
if not os.path.exists("historicoJogos.json") : 
      with open("historicoJogos.json", "w") as file :
            json.dump([], file)
          
def clear() :
      os.system("cls")
      
def geraId() : 
      return int(random.randint(1000, 9999))
      
         
def lerCadastros() :
      with open("cadastros.json") as file : 
            cadastros = json.load(file)
            return cadastros
      
      
def attCadastros(perfil) : 
      object_json = json.dumps(perfil, indent=4, ensure_ascii=False)
      with open("cadastros.json", "w") as file : 
            file.write(object_json)
            

def lerHistorico() : 
      with open("historicoJogos.json") as file : 
            historico = json.load(file)
            return historico


def attHistorico(jogada) :
      object_json = json.dumps(jogada, indent=4, ensure_ascii=False)
      with open("historicoJogos.json", "w") as file :
            file.write(object_json)


def historicoUsuarios(id_usuario) :
      historico = lerHistorico()
      return historico.get(id_usuario, [])


while True : 
      
      clear()
      print("-" * 25, "BEM-VINDO AO JOGO DO BICHO! ", "-" * 25, "\n")
      print("     Escolha uma opção válida: \n")
      print("[1] - Criar Perfil")
      print("[2] - Login")
      print("[3] - Regras")
      print("[4] - Sair do programa \n")
      print("-" * 80, "\n")
      opt = int(input())
      
      if opt == 1 : 
            clear()
            print("***** CRIANDO PERFIL *****\n")
            nvNome = input("Escreva o seu nome: ")
            senha = int(input("Agora, insira sua senha: "))
            id = geraId()
            
            perfil = {
                  "id" : id,
                  "nome" : nvNome,
                  "senha": senha
            }
            
            cadastros = lerCadastros()
            cadastros.append(perfil)
            attCadastros(cadastros)
            
            clear()
            print("*" * 12," Um novo bicheiro foi cadastrado! ", "*" * 12)
            print(f"{nvNome}, seu ID para acessar o perfil é: {id}.\n")
            input("- Pressione 'Enter' para continuar.")
            
      if opt == 2 : 
            clear()
            print("*" * 10, " LOGIN ", "*" * 10)
            this_id = int(input("- Digite o seu ID: "))
            this_senha = int(input("- Agora, digite sua senha: "))
            
            cadastros = lerCadastros()
            idEncontrado = None
            
            for id in cadastros :
                  if id["id"] == this_id and id["senha"] == this_senha: 
                        idEncontrado = id
                        break
            
            if idEncontrado :
                  
                  while True : 
                        
                        clear()
                        print(f"------------------- [ Seja bem-vindo, {idEncontrado['nome']}! ] --------------------\n")
                        print("     O que deseja fazer hoje, meu bicheiro ? \n")
                        print("[1] - Fazer novo jogo")
                        print("[2] - Histórico de jogos")
                        print("[3] - Sair do perfil \n")
                        print("-" * 67, "\n")
                        optDois = int(input())
                        
                        if optDois == 1 : 
                              clear()
                              
                              print("-" * 50)
                              print("     Que tipo de jogo você quer apostar ? \n")
                              print("[1] - Dezena")
                              print("[2] - Sorteio de animal \n")
                              print("-" * 50, "\n")
                              jogo = int(input())
                              
                              if jogo == 1 :
                                    clear()                              
                                    dezenas = []
                                    
                                    print("***** Você pode escolher 3 números de 0 a 99 para serem sorteados. *****\n")
                                    
                                    for i in range(1,4) :
                                          num = int(input(f"Digite a {i}º dezena: "))
                                          dezenas.append(num)
                              
                                    valor = float(input("\n- Qual a quantia será apostada  ? \n"))
                                    
                                    sorteados = [random.randint(0, 99) for c in range(3)]
                                    
                                    dezenas_escolhidas = set(dezenas)
                                    dezenas_sorteadas = set(sorteados)
                                    
                                    acertos = len(dezenas_escolhidas.intersection(dezenas_sorteadas))
                                    
                                    lucro = (acertos * valor) * 15
                                    
                                    jogada = {
                                          "id" : idEncontrado["id"],
                                          "dezenas" : dezenas,
                                          "sorteados" : sorteados,
                                          "valor" : valor,
                                          "acertos" : acertos,
                                          "lucro" : lucro,
                                          "tipo" : 1      
                                    }
                                    
                                    historico = lerHistorico()
                                    historico.append(jogada)
                                    attHistorico(historico)
                                    
                                    if acertos > 0 : 
                                          
                                          clear()
                                          print("-" * 75)
                                          print(f"     Números jogados: {dezenas[0]}, {dezenas[1]} e {dezenas[2]}.")
                                          print(f"     Números sorteados: {sorteados[0]}, {sorteados[1]} e {sorteados[2]}.\n\n")
                                          print(f"Uau, você acertou {acertos} número(s)! \n\n")
                                          print(f"Valor retornado: R${lucro:.2f}.")
                                          print("-" * 75, "\n")
                                          input("- Pressione 'Enter' para continuar.")
                                    
                                    elif acertos == 0 : 
                                          
                                          clear()
                                          print("-" * 75)
                                          print(f"     Números jogados: {dezenas[0]}, {dezenas[1]} e {dezenas[2]}.")
                                          print(f"     Números sorteados: {sorteados[0]}, {sorteados[1]} e {sorteados[2]}.\n\n")
                                          print("     Nenhum número acertado hoje, campeão. Mais sorte na próxima vez!")
                                          print("-" * 75, "\n")
                                          input("- Pressione 'Enter' para continuar.")
                                          
                              
                              elif jogo == 2 : 
                                    clear()
                                    animais = [
                                          "Avestruz", "Águia", "Burro", "Borboleta", "Cachorro",
                                          "Cabra", "Carneiro", "Camelo", "Cobra", "Coelho", 
                                          "Cavalo", "Elefante", "Galo", "Gato", "Jacaré",
                                          "Leão", "Macaco", "Porco", "Pavão", "Peru",
                                          "Touro", "Tigre", "Urso", "Veado", "Vaca"
                                    ]
                                    
                                    print("Animais do Jogo do Bicho: \n")
                                    
                                    for i, animal in enumerate(animais) : 
                                          print(f"[{i}] : {animal}")
                                    
                                    escolha = int(input("\n - Digite o número do animal escolhido: "))
                                    valor = float(input("- Qual o valor a ser apostado ? \n"))
                                    lucro = 0
                                    
                                    num_sorteado = random.randint(0, 24)
                                    
                                    if escolha == num_sorteado : 
                                          lucro = valor * 7
                                          clear()
                                          print("-" * 60)
                                          print(f"    Você escolheu o animal: {animais[escolha]}")
                                          print(f"    O número sorteado foi: {num_sorteado} \n")
                                          print("     Parabéns meu champion, você acertou o animal! \n")
                                          print(f"     retornado: R${lucro:.2f}.")
                                          print("-" * 60, "\n")
                                          input("- Pressione 'Enter' para continuar.")
                                          
                                    else :
                                          
                                          clear()
                                          print("-" * 60)
                                          print(f"    Você escolheu o animal: {animais[escolha]}")
                                          print(f"    O número sorteado foi: {num_sorteado} \n")
                                          print("     Não foi dessa vez, campeão. Boa sorte da próxima vez!")
                                          print("-" * 60, "\n")
                                          input("- Pressione 'Enter' para continuar.")
                                    
                                    jogada = {
                                          "id" : idEncontrado["id"],
                                          "escolha" : escolha, 
                                          "num_sorteado" : num_sorteado,
                                          "valor" : valor,
                                          "lucro" : lucro,
                                          "tipo" : 2
                                    }
                                    
                                    historico = lerHistorico()
                                    historico.append(jogada)       
                                    attHistorico(historico) 
                                    
                                    
                        elif optDois == 2 :
                              clear()
                              print(f"Histórico de jogos do {idEncontrado['nome']}:\n")
                              
                              historico = lerHistorico()
                              temHistorico = False
                              
                              for id in historico :
                                    if id["id"] == this_id :
                                          
                                          temHistorico = True
                                          
                                          if id["tipo"] == 1 :
                                                print("-" * 40)
                                                print(f"Dezenas escolhidas: {id['dezenas'][0]}, {id['dezenas'][1]} e {id['dezenas'][2]}.")
                                                print(f"Dezenas sorteadas: {id['sorteados'][0]}, {id['sorteados'][1]} e {id['sorteados'][2]}.")
                                                print(f"Quantidade de acertos: {id['acertos']}.\n")
                                                print(f"Valor apostado: R${id['valor']:.2f}.")
                                                print(f"Retorno: R${id['lucro']:.2f}.")
                                                print("-" * 40)
                                                print("\n")
                                                
                                          elif id["tipo"] == 2 : 
                                                
                                                animais = [
                                                      "Avestruz", "Águia", "Burro", "Borboleta", "Cachorro",
                                                      "Cabra", "Carneiro", "Camelo", "Cobra", "Coelho", 
                                                      "Cavalo", "Elefante", "Galo", "Gato", "Jacaré",
                                                      "Leão", "Macaco", "Porco", "Pavão", "Peru",
                                                      "Touro", "Tigre", "Urso", "Veado", "Vaca"
                                                ]
                                                
                                                print("-" * 40)
                                                print(f"Animal escolhido: {animais[id['escolha']]}.")
                                                print(f"Animal sorteado: {animais[id['num_sorteado']]}.\n")
                                                print(f"Valor apostado: R${id['valor']:.2f}.")
                                                print(f"Retorno: R${id['lucro']:.2f}")
                                                print("-" * 40)
                                                print("\n")
                                          
                              if not temHistorico : 
                                    print("Nenhum histórico de jogos encontrado para este usuário.\n")
                                    input("- Pressione Enter para voltar ao menu.")
                                    
                              else : 
                                    input("- Pressione Enter para voltar ao menu.")  
                                    
                        elif optDois == 3 : 
                              break
                                                
                                                
            else : 
                  clear()
                  input("*** Usuário e/ou senha errados! Tente novamente da forma correta. ***")
                  
      if opt == 3 : 
            clear()
            print("""
                  ***************************************************** AVISO *************************************************************
                  
                  Esse código é apenas uma versão simplificada do popular Jogo do Bicho, e não segue exatamente como funciona na realidade.
                  
                  *************************************************************************************************************************
                  
                  \n """)
            input("""
            -------------------- REGRAS DO JOGO DO BICHO: --------------------
            
                  O jogo do bicho é uma forma popular de jogo de azar no Brasil. Embora o jogo do bicho seja ilegal em muitos lugares, ele ainda é amplamente jogado. Aqui estão as regras básicas do jogo do bicho:
                  
                  
            1. Escolha do Animal: No início do jogo, os jogadores escolhem um animal entre os 25 disponíveis, cada um associado a um número de 00 a 99. Alguns dos animais mais comuns incluem avestruz, águia, burro, cobra, elefante, leão, macaco, vaca, entre outros.

            2. Aposta: Os jogadores fazem suas apostas em um ou mais animais, indicando a quantia que desejam apostar. As apostas são feitas com base em números de dois dígitos, que correspondem ao número associado ao animal escolhido.

            3. Resultado do Sorteio: Em um horário predeterminado, é realizado um sorteio, geralmente usando um globo com 100 bolas numeradas de 00 a 99. Uma bola é retirada aleatoriamente, revelando o número vencedor.

            4. Pagamento: Para este programa, o vencedor levará 7x o valor que apostou caso acerte o animal ou 15x o valor caso acerte uma dezena.
            
            5. Variações: Existem várias variações do jogo do bicho, com regras e pagamentos ligeiramente diferentes em diferentes regiões do Brasil.
            
            
            OBS: Como esse programa é apenas um simulador simples, não haverão todas as possibilidades que um Jogo do Bicho real poderia trazer, para fins de simplificação e elucidação do código.
            
            -------------------------------------------------------------------
                  """)
            
      if opt == 4 :
           clear()
           print("Obrigado por testar esse pequeno sistema! Partiu virar bicheiro!")
           print("Ass: Jor-El.")
           break