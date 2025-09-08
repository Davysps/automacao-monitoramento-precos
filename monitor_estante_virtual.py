import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime  # Para registrar a data e hora

# Importações do Firebase
import firebase_admin
from firebase_admin import credentials, firestore

# --- INICIALIZAÇÃO DO FIREBASE ---
# O 'try...except' aqui garante que o script só continue se a conexão com o Firebase for bem-sucedida.
try:
    # Use o arquivo JSON que você baixou
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("[Firebase] Conexão com o Firestore estabelecida com sucesso!")
except Exception as e:
    print(f"[Firebase] Erro ao conectar com o Firebase: {e}")
    print("Verifique se o arquivo 'credentials.json' está na pasta correta.")
    exit()  # Encerra o script se não conseguir conectar
# --- FIM DA INICIALIZAÇÃO ---


# URL do produto a ser monitorado
url = "https://www.estantevirtual.com.br/livro/significado-nas-artes-visuais-00V-0508-000-BK"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"\nIniciando monitoramento para o produto: {url}\n")

try:
    # 1. FAZ A REQUISIÇÃO E EXTRAI OS DADOS (como no passo anterior)
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find(
        'script', {'type': 'application/ld+json', 'name': 'structured-pdp'})

    product_title = "Título não encontrado"
    price = "Preço não encontrado"

    if script_tag:
        json_data = json.loads(script_tag.string)
        product_info = json_data.get('@graph', [{}])[0]
        product_title = product_info.get('name')
        offers_info = product_info.get('offers', {})
        low_price = offers_info.get('lowPrice')

        if product_title and low_price:
            price = f"R$ {low_price.replace('.', ',')}"
            print("--- DADOS EXTRAÍDOS COM SUCESSO ---")
            print(f"Produto: {product_title}")
            print(f"Preço: {price}")
            print("-----------------------------------")

            # 2. SALVA OS DADOS NO FIRESTORE
            try:
                # Define a coleção 'produtos' e usa o título do produto como ID do documento
                doc_ref = db.collection('produtos').document(product_title)

                # Prepara os dados para salvar
                data_para_salvar = {
                    'preco': price,
                    'ultima_verificacao': datetime.now()  # Pega a data e hora atuais
                }

                # Usa .set() para criar o documento se não existir, ou sobrescrevê-lo se já existir
                doc_ref.set(data_para_salvar)

                print(
                    f"\n[Firebase] Dados salvos com sucesso no documento: '{product_title}'")

            except Exception as e:
                print(f"\n[Firebase] Erro ao salvar dados no Firestore: {e}")

        else:
            print("Não foi possível extrair título ou preço da página.")

    else:
        print("Tag de script com dados do produto não encontrada.")


except Exception as e:
    print(f"Ocorreu um erro geral no processo: {e}")
