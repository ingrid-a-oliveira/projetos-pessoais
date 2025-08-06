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
    nome = str(input("Insira o nome da música: ")).title()
    artista = str(input("Insira o nome do artista/banda: ")).title()
    while True:
        ano_input = (input("Insira o ano de lançamento da música: "))
        if ano_input.isdigit():
            ano = int(ano_input)
            break
        else:
            print("Entrada inválida. Insira apenas valores numéricos no ano!")
    album = str(input("Insira o nome do álbum em que a música foi lançada: ")).title()
    genero = str(input("Insira o gênero da música: ")).title()

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
    busca = str(input("Digite o nome ou artista: ")).title()
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
        
def remover_musica():
    remover = input("Insira o nome da música que deseja excluir: ").strip().title()
    for musica in catalogo_musical:
        if musica.get("Nome") == remover:
            catalogo_musical.remove(musica)
            print(f"A música '{remover}' foi excluída com sucesso!")
            break
    else:
        print(f"A música '{remover}' não foi encontrada no catálogo.")
        
def menu():
    while True:
        print("\n==== Catálogo Musical ====")
        print("1 - Adicionar músicas")
        print("2 - Listar músicas")
        print("3 - Buscar")
        print("4 - Excluir")
        print("0 - Sair")
        
        opcao = input("Esolha uma opção: ")
        
        if opcao == "1":
            add_musica()
        
        elif opcao == "2":
            list_musica()
        
        elif opcao == "3":
            buscar_musicas()
            
        elif opcao == "4":
            remover_musica()
            
        elif opcao == "0":
            print("\nEncerrando...\n Até logo!")
            break
        
        else:
            print("\nOpção inválida. Selecione uma das opções disponíveis no menu!")
            
menu()