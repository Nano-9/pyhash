# funções 

def existe(nomearq):
	foundfile = False
	try:
		file = open(nomearq, "rt")
	except:
		foundfile = False
		return foundfile
	else:
		foundfile = True
		return foundfile
def criar(nomearq):
	file1 = False
	try:
		file = open(nomearq, "wt+")
	except:
		print("\033[91mErro ao criar o arquivo!\033[m")
	else:
		file1 = True
		return file1
def adicionar(nomearq,password):
	try:
		file = open(nomearq, "at")
	except:
		print("Erro ao abrir arquivo!")
	else:
		try:
			file.write("{}\n".format(password))
		except:
			print("\033[91mErro ao abrir arquivo\033[m")
		else:
			pass
