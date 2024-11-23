import json
import zipfile
import os

# Exporta dados para quatro arquivos .json
#  users, stores, products e sales
#  Compata todos para um .zip e exclui
#  as versões não compactadas
def ExpDados(userDict, storeDict, productDict, salesDict):
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
        print(f"Erro ao exportar dados de produtos - {e}")
    try:
        with open(f'sales.json', 'w', encoding='utf-8') as f:
            json.dump(productDict, f, ensure_ascii=False, indent=4)
        print(f"Dados de vendas exportados com sucesso para {filename}(sales) :)")
    except Exception as e:
        print(f"Erro ao exportar dados de vendas - {e}")

    try:
        with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write('users.json', os.path.basename('users.json'))
            zipf.write('stores.json', os.path.basename('stores.json'))
            zipf.write('products.json', os.path.basename('products.json'))
            zipf.write('sales.json', os.path.basename('sales.json'))
        
        print(f"Arquivos exportados com sucesso para {filename} :)")
        
        os.remove('users.json')
        os.remove('stores.json')
        os.remove('products.json')
        os.remove('sales.json')
        
    except Exception as e:
        print(f"Erro ao criar o arquivo ZIP - {e}")

# Basicamente um Print específico para
#  quando é necessário reter alguma 
#  informação na tela antes sair dela
def wait_print(text):
    print(f"{text}\n")
    input("[ENTER PARA CONTINUAR...]")

