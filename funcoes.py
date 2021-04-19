# funções 

def existe(nomearq):
	foundfile = False
	try:
		file = open(nomearq, "rt")
	except:
		print("Arquivo não existe!")
		return foundfile
	else:
		foundfile = True
		return foundfile
def criar(nomearq):
	try:
		file = open(nomearq, "wt+")
	except:
		print("Erro ao criar o arquivo!")
	else:
		print("Arquivo de senha criado!")
def adicionar(nomearq,password):
	try:
		file = open(nomearq, "at")
	except:
		print("Erro ao abrir arquivo!")
	else:
		try:
			file.write("{}\n".format(password))
		except Exception as Error:
			print(Error)
		else:
			pass
