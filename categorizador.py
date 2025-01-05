from openai import OpenAI
client = OpenAI()
modelo="gpt-4o-mini"

prompt_sistema = """
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas
    - Moda Sustentável
    - Produtos para o Lar 
    - Beleza Natural
    - Eletrônicos Verdes 

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída 
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes

"""

prompt_usuario = input("Apresente o nome de um produto: ")

response = client.chat.completions.create(
  model=modelo,
  messages=[
    {
      "role": "system",
      "content": prompt_sistema
    },
    {
        "role": "user",
        "content": prompt_usuario
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

print(response.choices[0].message.content)
