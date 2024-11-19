import json

## 5. EXPORTA OS DADOS PARA UM ARQUIVO .json ##
def ExpDados(Produtos):
    if not Produtos:
        print("Nenhum produto cadastrado para exportar...")
        return
    
    filename = input("Digite o nome do arquivo: (Sem extensão)\n") + ".json"

    prod_dic = [prod._asdict() for prod in Produtos]

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(prod_dic, f, ensure_ascii=False, indent=4)
        print(f"Dados exportados com sucesso para {filename} :)")
    except Exception as e:
        print(f"Erro ao exportar dados - {e}")

# Basicamente um Print específico para
#  quando é necessário reter alguma 
#  informação na tela antes sair dela
def wait_print(text):
    print(f"{text}\n")
    input("[ENTER PARA CONTINUAR...]")
