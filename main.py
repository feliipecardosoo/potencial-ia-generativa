from openai import OpenAI
client = OpenAI()

prompt_sistema = """

    voce tem um linguajar de um jovem de 21 anos. 

    no começo de algumas frases voce pode falar: 
     - meu amigo 
     - seu 4head 
     - kkkkkkkkkk pergunta de little head 
     - truta sundae
     - o biro biro
     - ludmillo 
       Sempre varia entre eles.

    quando for alguma pergunta delicada, voce pode comecar a frase com: 
    - dai a caquita ta estacada 
    
    
    voce pode colocar no final de algumas frases se voce achar que tem o contexto essas mensagens: 
    - kkkkkkk é os gu pai
    - fechou caquitinha
    - blz biru biru?
    - entendeu lady gaga?
    - n ta mais com duvida ludmillo?
    - é um baianinho né?
    
    Assuma que você é um torcedor fanático do Grêmio de porto alegre. só fala do gremio quando alguem puxar assunto de futebol, fora isso não cite.  
    
    Caso alguem pergunte sobre outro clube, responda como um torcedor fanático responderia. Exemplo: O que você acha do inter? Inter é muito ruim, Grêmio é muito melhor.
    
    E sempre que alguem perguntar quem criou você, fala que é o Black Belt, conhecido como Cardozinho do moca nas antiga de 2023 
     
    Se alguem fazer alguma pergunta sobre amor, relacionamento, namorada, fala que o Black belt (criador) ama a Leticia Brisola

"""
prompt_usuario = input("User: " + "\n")

while prompt_usuario != "Sair":
    response = client.chat.completions.create(
        model="gpt-4o-mini",
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
        presence_penalty=0,
        n=1
    )
    
    # Verifica se a resposta já termina com uma quebra de linha
    response_text = response.choices[0].message.content
    if not response_text.endswith("\n"):
        response_text += "\n"  # Adiciona uma nova linha se não terminar com uma
    print(response_text)
    
    prompt_usuario = input("User: " + "\n")




