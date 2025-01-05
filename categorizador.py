from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": """
        Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou casa e de uma descrição da categoria.
       """
    },
    {
        "role": "user",
        "content": """
        Escova de dentes de bambu
        """
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
