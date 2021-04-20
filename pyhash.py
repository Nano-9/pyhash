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

	opcoes_validas = list("ABCDEFX")
	valido = False
	arquivo = sys.argv[1]

	print("\033[1;31m[+] Verificando se a extensão do arquivo está correta...\033[m")
	time.sleep(2.5)
	if ".txt" in arquivo:
		if not funcoes.existe(arquivo):
			funcoes.criar(arquivo)
			boas_vindas = "     Seja bem vindo ao Pyhash!"
			boas_vindas2 = "      Criado por: Lucas-Dk"
			print("     \033[1;32m[+] MENSAGEM PARA VOCÊ [+]\033[m")
			print("\033[1;36m{--------------------------------------\033[m")
			for x in boas_vindas:
			  print("\033[1;34m{}\033[m".format(x),flush=True,end="")
			  time.sleep(0.1)
			print()
			for w in boas_vindas2:
			  print("\033[1;34m{}\033[m".format(w),flush=True,end="")
			  time.sleep(0.1)
			print("\n\033[1;36m---------------------------------------\033[m}")
			time.sleep(0.5)
			print("\n\033[1;91m[+] Deletando mensagem....\033[m")
			time.sleep(1.3)
			os.system("clear")
		if funcoes.existe(arquivo) == True:
			pass
		print("\033[92m[+] Extensão de arquivo válida!\033[m")
		time.sleep(1.5)
		os.system("clear")
		print("""\033[94m
 _______  __   __  __   __  _______  _______  __   __ 
|       ||  | |  ||  | |  ||   _   ||       ||  | |  |
|    _  ||  |_|  ||  |_|  ||  |_|  ||  _____||  |_|  |
|   |_| ||       ||       ||       || |_____ |       |
|    ___||_     _||       ||       ||_____  ||       |
|   |      |   |  |   _   ||   _   | _____| ||   _   |
|___|      |___|  |__| |__||__| |__||_______||__| |__|\033[m
                                                                    
> versão 1.0
> coded by: lucas-DK
> meu github: https://github.com/lucas-Dk


==================== MENU =======================\n
\033[91m[\033[m\033[34mA\033[m\033[91m]\033[m - Gerar senhas com 1 sílaba  \033[92m[RÁPIDO]\033[m
\033[91m[\033[m\033[34mB\033[m\033[91m]\033[m - Gerar senhas com 2 sílabas \033[92m[RÁPIDO]\033[m
\033[91m[\033[m\033[34mC\033[m\033[91m]\033[m - Gerar senhas com 4 sílabas \033[93m[LENTO]\033[m
\033[91m[\033[m\033[34mD\033[m\033[91m]\033[m - Gerar senhas com 6 sílabas \033[91m[MUITO LENTO]\033[m
\033[91m[\033[m\033[34mE\033[m\033[91m]\033[m - Gerar senhas com 8 sílabas \033[91m[MUITO LENTO]\033[m
\033[91m[\033[m\033[34mF\033[m\033[91m]\033[m - Gerar senhas aleatorias    \033[91m[MUITO LENTO]\033[m
\033[91m[\033[m\033[34mX\033[m\033[91m]\033[m - Fechar programa

=================================================\n
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

			if userop not in opcoes_validas:
				print("\033[1;31m[+] >> ATENÇÃO << Parece que o que você digitou não é uma")
				print("opção válida! Tente novamente...\033[m")
				sys.exit()
			else:
				if userop == "A":
					quantidade_senhas_geradas = 0
					print("\n\033[1;31m[+] Gerando as suas senhas...\033[m\n")
					print("\033[1;33m[+] Tempo estimado: 6.0 segundos\033[m")
					for z in palavra_para_senhas:
						quantidade_senhas_geradas += 1
						armazenar = z
						funcoes.adicionar(nomearq=arquivo,password=armazenar)
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))

				elif userop == "B":
					print("\033[1;31m[+] Gerando as suas senhas... [+]\033[m\n")
					print("\033[1;33m[+] Tempo estimado: 1.5 minutos\033[m")
					for x in palavra_para_senhas:
						for z in palavra_para_senhas:
							quantidade_senhas_geradas += 1
							armazenar = x+z
							funcoes.adicionar(nomearq=arquivo,password=armazenar)
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))

				elif userop == "C":
					print("\033[1;31m[+] Gerando as suas senhas, este processo pode demorar um pouco...\033[m\n")
					print("\033[1;33m[+] Tempo estimado: 7 minutos\033[m")
					for x in palavra_para_senhas:
						for z in palavra_para_senhas:
							for a in palavra_para_senhas:
								for b in palavra_para_senhas:
									quantidade_senhas_geradas += 1
									armazenar = x+z+a+b
									funcoes.adicionar(nomearq=arquivo,password=armazenar)
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))
					
				elif userop == "D":
					print("\033[1;31m[+] Gerando as suas senhas, este processo pode demorar...\033[m\n")
					print("\033[1;33m[+] Tempo estimado: 5 horas {depende do dispositivo}\033[m")	
					for x in palavra_para_senhas:
						for z in palavra_para_senhas:
							for a in palavra_para_senhas:
								for b in palavra_para_senhas:
									for c in palavra_para_senhas:
										for d in palavra_para_senhas:
											quantidade_senhas_geradas += 1
											armazenar = x+z+a+b+c+d
											funcoes.adicionar(nomearq=arquivo,password=armazenar)
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))
					
				elif userop == "E":
					print("\033[1;31m[+] Gerando as suas senhas, este processo pode demorar...\033[m\n")
					print("\033[1;33m[+] Tempo estimado: 6 horas {depende do dispositivo}\033[m")
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
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))
					
				elif userop == "F":
					print("\033[1;33m[+] Tempo estimado: 6 horas {depende do dispositivo}\033[m")
					time.sleep(1.4)
					print("\033[1;31m[+] Gerando as suas senhas, este processo pode demorar...\033[m\n")
					for x in palavra_aleatoria_para_senhas:
						for z in palavra_aleatoria_para_senhas:
							for a in palavra_aleatoria_para_senhas:
								for b in palavra_aleatoria_para_senhas:
									for c in palavra_aleatoria_para_senhas:
										for d in palavra_aleatoria_para_senhas:
											quantidade_senhas_geradas += 1
											armazenar = x+z+a+b+c+d
											funcoes.adicionar(nomearq=arquivo,password=armazenar)
					print("\n\033[32m[+] Status do arquivo \033[35m{}\033[m: \033[1;36mConcluído\033[m".format(arquivo))
					print("\033[32m[+] Quantidade de senhas no arquivo:\033[m {}".format(quantidade_senhas_geradas))
	else:
		print("A extensão do arquivo não é permitida!")
else:
	print("""
Para usar o programa use:


\033[91m[+] Use: python pyhash.py senha.txt\033[m


no lugar de senha.txt você pode colocar o nome que
desejar, desde que a extensão seja .txt

faça bom uso :)
 """)

# by: lucas-DK
