import ollama

# Ferramentas da calculadora
def somar(a: float, b: float) -> str:
    """Soma dois números."""
    return str(a + b)

def subtrair(a: float, b: float) -> str:
    """Subtrai b de a."""
    return str(a - b)

def multiplicar(a: float, b: float) -> str:
    """Multiplica dois números."""
    return str(a * b)

def dividir(a: float, b: float) -> str:
    """Divide a por b."""
    if b == 0:
        return "Erro: divisão por zero."
    return str(a / b)

ferramentas = {
    "somar": somar,
    "subtrair": subtrair,
    "multiplicar": multiplicar,
    "dividir": dividir,
}

# Loop de raciocínio do agente
def executar_agente(pergunta: str) -> str:
    mensagens = [{"role": "user", "content": pergunta}]

    resposta = ollama.chat(
        model="llama3.2",
        messages=mensagens,
        tools=list(ferramentas.values())
    )

    mensagens.append(resposta["message"])

    if resposta["message"].get("tool_calls"):
        for tool in resposta["message"]["tool_calls"]:
            nome = tool["function"]["name"]
            raw_args = tool["function"]["arguments"]

            # Converte os argumentos para float se vierem como string
            parsed_args = {}
            for chave, valor in raw_args.items():
                try:
                    parsed_args[chave] = float(valor)
                except (ValueError, TypeError):
                    parsed_args[chave] = valor

            resultado = ferramentas[nome](**parsed_args)
            print(f"-> {nome}({parsed_args}) = {resultado}")
            mensagens.append({"role": "tool", "content": resultado})

        resposta_final = ollama.chat(model="llama3.2", messages=mensagens)
        return resposta_final["message"]["content"]

    return resposta["message"]["content"]

if __name__ == "__main__":
    perguntas = [
        "Quanto é 1284 + 4919?",
        "Quanto é 100 - 37?",
        "Quanto é 12 vezes 8?",
        "Quanto é 144 dividido por 12?",
    ]

    for pergunta in perguntas:
        print(f"\nUsuário: {pergunta}")
        print(f"Resposta: {executar_agente(pergunta)}")