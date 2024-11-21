import json
import keyboard
import zipfile
import os

## 5. EXPORTA OS DADOS PARA UM ARQUIVO .json ##
def ExpDados(userDict, storeDict, productDict):
    if not productDict and not storeDict and not userDict:
        print("Nenhum produto cadastrado para exportar...")
        return
    
    filename = input("| Digite o nome do arquivo:\n"
                     "| (Sem extensão)\n"
                     "| ") + ".zip"
    
    try:
        with open(f'users.json', 'w', encoding='utf-8') as f:
            json.dump(userDict, f, ensure_ascii=False, indent=4)
        print(f"Dados de usuários exportados com sucesso para {filename}(users) :)")
    except Exception as e:
        print(f"Erro ao exportar dados de usuários - {e}")
    try:
        with open(f'stores.json', 'w', encoding='utf-8') as f:
            json.dump(storeDict, f, ensure_ascii=False, indent=4)
        print(f"Dados de lojas exportados com sucesso para {filename}(stores) :)")
    except Exception as e:
        print(f"Erro ao exportar dados de lojas - {e}")
    try:
        with open(f'products.json', 'w', encoding='utf-8') as f:
            json.dump(productDict, f, ensure_ascii=False, indent=4)
        print(f"Dados de produtos exportados com sucesso para {filename}(products) :)")
    except Exception as e:
        print(f"Erro ao exportar dados de produtos- {e}")

    try:
        with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write('users.json', os.path.basename('users.json'))
            zipf.write('stores.json', os.path.basename('stores.json'))
            zipf.write('products.json', os.path.basename('products.json'))
        
        print(f"Arquivos exportados com sucesso para {filename} :)")
        
        os.remove('users.json')
        os.remove('stores.json')
        os.remove('products.json')
        
    except Exception as e:
        print(f"Erro ao criar o arquivo ZIP - {e}")

# Basicamente um Print específico para
#  quando é necessário reter alguma 
#  informação na tela antes sair dela
def wait_print(text):
    print(f"{text}\n")
    input("[ENTER PARA CONTINUAR...]")

# Lógica usada para fazer o menu selecionável 
# (up, down)
#  basicamente pega o Length de uma lista
#  e retorna o elemento selecionado com
#  base no tamanho da lista, nunca 
#  ultrapassando nem para cima, nem para baixo
def listMenuSelect(selected, listLength):
    key = keyboard.read_event(suppress=True)

    if key.name == "up" and key.event_type == "down":
        return (selected - 1) % listLength
    elif key.name == "down" and key.event_type == "down":
        return (selected + 1) % listLength
    elif key.name == "enter" and key.event_type == "down":
        return None
    else:
        return selected

