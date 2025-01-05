from openai import OpenAI
client = OpenAI()
modelo="gpt-4o-mini"

prompt_usuario = input("Apresente o nome de um produto: ")


def categoriza_produto(nome_produto, lista_categorias_possiveis):

  prompt_sistema = f"""
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas
    {lista_categorias_possiveis.split(",")}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída 
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes

  """

  response = client.chat.completions.create(
    model=modelo,
    messages=[
      {
        "role": "system",
        "content": prompt_sistema
      },
      {
          "role": "user",
          "content": nome_produto
      }
    ],
    response_format={
      "type": "text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].message.content

categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
  nome_produto = input("Digite o nome do produto: ")
  categoriza_produto(nome_produto, categorias_validas)