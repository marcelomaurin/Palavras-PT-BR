def ler_arquivo(nome_arquivo):
    lista = []
    #with open(nome_arquivo, 'r') as arquivo:  #modifiquei aqui
    with open(nome_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
        for linha in arquivo:
            palavra = linha.strip().strip("'")
            lista.append(palavra)
    return lista

def remover_duplicatas(lista):
    return list(set(lista))

#pequena modificacao na funcao
def salvar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write('\n'.join(conteudo))

# Lista de arquivos a serem somados
arquivos = ['palavras1.txt', 'palavras2.txt', 'palavras3.txt', 'palavras4.txt', 'palavras5.txt']

# Lista para armazenar todas as palavras
todas_palavras = []

# Ler o conteúdo de cada arquivo e adicionar à lista todas_palavras
for arquivo in arquivos:
    todas_palavras.extend(ler_arquivo(arquivo))

# Remover duplicatas
palavras_sem_duplicatas = remover_duplicatas(todas_palavras)

# Opcional: ordenar a lista resultante
palavras_sem_duplicatas.sort()

# Salvar o resultado em um novo arquivo
salvar_arquivo('dicionario_PT-BR.txt', palavras_sem_duplicatas)

print("Palavras únicas salvas no arquivo 'dicionario_PT-BR.txt'.")
