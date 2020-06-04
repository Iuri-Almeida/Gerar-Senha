# Projeto Gera Senha - Python e PyTube
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 01/06/2020
# Descrição: Esse projeto foi escrito na linguagem Python. Ele gera uma senha
# 			 forte com caracteres aleatórios, com o usuários só precisando
# 			 passar o número de caracteres que deseja ter na senha.
# Forma de uso: python gera-senha.py


# Importações necessárias.
import random, argparse, string


# Gerando uma descrição do que o programa faz.
parser = argparse.ArgumentParser(description="Gera uma senha forte para você!")

# Adicionando uma 'flag' para o usuário passar o parâmetro em relação ao tamanho
# de senha que deseja pela linha de comando(terminal).
# Ex.: python gera-senha.py -t 34
parser.add_argument("-t", dest="tamanho", required = True, help="quantidade de caracteres da senha")

# Define uma váriavel que vai poder ser chamada para ter acesso aos dados que foram
# passados pela linha de comando (terminal).
args = parser.parse_args()


# Função repnsável por gerar as senhas.
def gera_Senha(): 

	# Definindo uma variável que irá receber a senha.
	senha = ""

	# Adicionando um local de onde poderei me basear para gerar caracteres.
	# Obs.: Esses caracteres foram baseados nas sugestões de senhas do Google Chrome,
	# 		que nos meus testes não apresentou caracteres como: }]{[|;<>
	dicionario = string.ascii_letters + "0123456789'" + '^!@#$%&*()_-+=./?:,"'

	# Para cada 'i' de 0 até o tamanho indicado pelo usuário no terminal, faça:
	for i in range(int(args.tamanho)):

		# Faça a concatenação do caracter gerado com a variável senha.
		senha = senha + random.choice(dicionario)

	print("")

	# Imprima na tela qual foi a senha gerada.
	print("A senha gerada foi -> {}".format(senha))


# Função principal, responsável por chamar as outras funções.
def main():

	# Chamando a função para gerar a senha.
	gera_Senha()


if __name__ == "__main__":
	main()