# criador de senhas em python
# by: lucas-DK 
import sys
import os
import time
import funcoes
from dados import *

# programa principal

logar = sys.argv

if len(logar) == 2:
	
	valido = False
	arquivo = sys.argv[1]

	print("Verificando se a extensão do arquivo está correta...")
	time.sleep(2)
	if ".txt" in arquivo:
		if not funcoes.existe(arquivo):
			funcoes.criar(arquivo)
		if funcoes.existe(arquivo) == True:
			pass
		print("\033[92mExtensão de arquivo válida!\033[m")
		time.sleep(1.2)
		os.system("clear")
		print("""\033[94m
                           _                  
   __ _  ___ _ __ __ _  __| | ___  _ __       
  / _` |/ _ \ '__/ _` |/ _` |/ _ \| '__|      
 | (_| |  __/ | | (_| | (_| | (_) | |         
  \__, |\___|_|  \__,_|\__,_|\___/|_|       _ 
  |___/  __ _ ___ _____      _____  _ __ __| |
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
 | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
 |_|\033[m

	versão 1.0
	coded by -> Lucas Walker

Menu
\033[91m[\033[m\033[32mA\033[m\033[91m]\033[m - Gerar senhas com 1 sílaba
\033[91m[\033[m\033[32mB\033[m\033[91m]\033[m - Gerar senhas com 2 sílabas 
\033[91m[\033[m\033[32mC\033[m\033[91m]\033[m - Gerar senhas com 4 sílabas
\033[91m[\033[m\033[32mD\033[m\033[91m]\033[m - Gerar senhas com 6 sílabas 
\033[91m[\033[m\033[32mE\033[m\033[91m]\033[m - Gerar senhas com 8 sílabas 
\033[91m[\033[m\033[32mF\033[m\033[91m]\033[m - Gerar senhas aleatorias
\033[91m[\033[m\033[32mX\033[m\033[91m]\033[m - Fechar programa
			""")
		try:
			userop = str(input("O que você deseja: ")).upper()[0]
		except KeyboardInterrupt:
			print("Saiu...")
			sys.exit()
		except ValueError: #aqui não daria esse erro porque tudo seria uma string, mas é só pra precaver mesmo
			print("Hm, você usou um valor errado!")
			print("Fechando...")
			sys.exit()
		except IndexError:
			print("Essa parte não pode ficar sem nada! Saindo...")
			sys.exit()
		else:
			quantidade_senhas_geradas = 0
			palavra_para_senhas = dados
			palavra_aleatoria_para_senhas = dadoos

			if userop == "A":
				quantidade_senhas_geradas = 0
				print("\033[31mGerando as suas senhas...\033[m\n")
				for z in palavra_para_senhas:
					quantidade_senhas_geradas += 1
					armazenar = z
					funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))
				

			elif userop == "B":
				print("\033[31mGerando as suas senhas...\033[m")
				for x in palavra_para_senhas:
					for z in palavra_para_senhas:
						quantidade_senhas_geradas += 1
						armazenar = x+z
						funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))
				

			elif userop == "C":
				print("\033[31mGerando as suas senhas, este processo pode demorar um pouco...\033[m\n")
				for x in palavra_para_senhas:
					for z in palavra_para_senhas:
						for a in palavra_para_senhas:
							for b in palavra_para_senhas:
								quantidade_senhas_geradas += 1
								armazenar = x+z+a+b
								funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))

			elif userop == "D":
				print("\033[31mGerando as suas senhas, este processo pode demorar...\033[m\n")	
				for x in palavra_para_senhas:
					for z in palavra_para_senhas:
						for a in palavra_para_senhas:
							for b in palavra_para_senhas:
								for c in palavra_para_senhas:
									for d in palavra_para_senhas:
										quantidade_senhas_geradas += 1
										armazenar = x+z+a+b+c+d
										funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))

			elif userop == "E":
				print("\033[31mGerando as suas senhas, este processo pode demorar...\033[m\n")
				for x in palavra_para_senhas:
					for z in palavra_para_senhas:
						for a in palavra_para_senhas:
							for b in palavra_para_senhas:
								for c in palavra_para_senhas:
									for d in palavra_para_senhas:
										for e in palavra_para_senhas:
											for f in palavra_para_senhas:
												quantidade_senhas_geradas += 1
												armazenar = x+z+a+b+c+d+e+f
												funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))

			elif userop == "F":
				print("\033[31m[ATENÇÃO]: Essa função por padrão, gera senhas com 6 caracteres!\033[m")
				time.sleep(1.4)
				os.system("clear")
				print("\033[31mGerando as suas senhas, este processo pode demorar...\033[m\n")
				for x in palavra_aleatoria_para_senhas:
					for z in palavra_aleatoria_para_senhas:
						for a in palavra_aleatoria_para_senhas:
							for b in palavra_aleatoria_para_senhas:
								for c in palavra_aleatoria_para_senhas:
									for d in palavra_aleatoria_para_senhas:
										quantidade_senhas_geradas += 1
										armazenar = x+z+a+b+c+d
										funcoes.adicionar(nomearq=arquivo,password=armazenar)
				print("\033[32mSeu arquivo >>>\033[m \033[35m{}\033[m \033[32m<<< foi criado e contém {} senhas!\033[m".format(arquivo,quantidade_senhas_geradas))
	else:
		print("A extensão do arquivo não é permitida!")
else:
	print("""
Para usar o programa use:

\033[91mpython gerador.py senha.txt\033[m

no lugar de senha.txt você pode colocar o nome que
desejar, desde que a extensão seja .txt

faça bom uso :)
		""")
