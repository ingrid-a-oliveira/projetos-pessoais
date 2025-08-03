catalogo_musical = [
    {
    "Nome" : "nome",
    "Artista" : "artista",
    "Ano" : "ano",
    "Álbum" : "album",
     "Gênero" : "genero"
    },
    {
    "Nome" : "nome",
    "Artista" : "artista",
    "Ano" : "ano",
    "Álbum" : "album",
     "Gênero" : "genero"
    },
    {
    "Nome" : "nome",
    "Artista" : "artista",
    "Ano" : "ano",
    "Álbum" : "album",
     "Gênero" : "genero"
    },
    {
    "Nome" : "nome",
    "Artista" : "artista",
    "Ano" : "ano",
    "Álbum" : "album",
     "Gênero" : "genero"
    }
]

def add_musica():
    nome = str(input("Insira o nome da música: ")).capitalize()
    artista = str(input("Insira o nome do artista/banda: ")).capitalize()
    while True:
        ano_input = (input("Insira o ano de lançamento da música: "))
        if ano_input.isdigit():
            ano = int(ano_input)
            break
        else:
            print("Entrada inválida. Insira apenas valores numéricos no ano!")
    album = str(input("Insira o nome do álbum em que a música foi lançada: ")).capitalize()
    genero = str(input("Insira o gênero da música: ")).capitalize()

    musica = {
        "Nome" : nome,
        "Artista" : artista,
        "Ano" : ano,
        "Álbum" : album,
        "Gênero" : genero
        }
    
    catalogo_musical.append(musica)
    print(f"\n A música {nome} - {artista} foi adicionada ao catálogo com sucesso!\n")

def list_musica():
    if not catalogo_musical:
        print("Não há músicas cadastradas no catálogo!")
        return
    else:
        print("\nMúsicas cadastradas: \n")
        for musica in catalogo_musical:
            print(f"{musica['Nome']} - {musica['Artista']} | Lançamento: {musica['Ano']} | Álbum: {musica['Álbum']}")
            
def buscar_musicas():
    busca = str(input("Digite o nome ou artista: ")).capitalize()
    resultados = [
        result for result in catalogo_musical
        if busca in result['Nome'] or busca in result['Artista']
    ]
    if resultados:
        print("\nResultados Encontrados: \n")
        for busca in resultados:
            print(f"{busca['Nome']} - {busca['Artista']}")
    else:
        print("Não foram encontrados resultados para a busca!")
        
"""add_musica()"""
list_musica()
buscar_musicas()