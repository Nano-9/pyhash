# arquivo de log que mostra o ano o dia e a hora que o usuário está rodando o script principal

import datetime


def data_abertura_programa_principal():
	"""
	data : Armazena a hora certa que o arquivo foi aberto
	pelo usuário
	"""
	data = datetime.datetime.now().time()


def adicionar_dados_ao_arquivo(name,dados):
	"""
	Essa função tem como objetivo armazenar os dados
	da função acima dentro de um arquivo de log
	"""
	try:
		filelog = open(name, "at")
	except Exception as e:
		print("Erro Lucas")
		print(e)
	else:
		try:
			filelog.write("[+] Script iniciado as : {} \n".format(dados[0:8]))
		except Exception as er:
			print("Erro dois lucas")
			print(er)
		else:
			pass
