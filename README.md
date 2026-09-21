# 🤖 Agente Calculadora com Ollama

Um agente de IA local que interpreta perguntas matemáticas em linguagem natural e executa as operações correspondentes usando **function calling** com o modelo `llama3.2` via [Ollama](https://ollama.com/).

---

## 📋 Sobre o projeto

Este projeto demonstra o conceito de **agente de IA com ferramentas (tool use)**:

1. O usuário faz uma pergunta em linguagem natural
2. O LLM raciocina e decide qual ferramenta matemática usar
3. A função Python é executada localmente
4. O modelo sintetiza e retorna a resposta final

Nenhuma regra explícita é programada — o **modelo decide sozinho** qual operação executar.

---

## 🧰 Ferramentas disponíveis

| Ferramenta | Descrição |
|---|---|
| `somar(a, b)` | Soma dois números |
| `subtrair(a, b)` | Subtrai `b` de `a` |
| `multiplicar(a, b)` | Multiplica dois números |
| `dividir(a, b)` | Divide `a` por `b` (protegido contra divisão por zero) |

---

## ⚙️ Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com/) instalado e rodando localmente
- Modelo `llama3.2` baixado

---

## 🚀 Instalação

**1. Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd projAgentsAI
```

**2. Crie e ative o ambiente virtual:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / Mac
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Baixe o modelo no Ollama:**
```bash
ollama pull llama3.2
```

---

## ▶️ Como usar

**Certifique-se de que o Ollama está rodando:**
```bash
ollama serve
```

**Execute o agente:**
```bash
python agent_ollama.py
```

**Saída esperada:**
```
Usuário: Quanto é 1284 + 4919?
-> somar({'a': 1284, 'b': 4919}) = 6203
Resposta: O resultado da soma de 1284 e 4919 é 6203.

Usuário: Quanto é 100 - 37?
-> subtrair({'a': 100, 'b': 37}) = 63
Resposta: A resposta para 100 - 37 é 63.

Usuário: Quanto é 12 vezes 8?
-> multiplicar({'a': 12, 'b': 8}) = 96
Resposta: A resposta é 96.

Usuário: Quanto é 144 dividido por 12?
-> dividir({'a': 144, 'b': 12}) = 12.0
Resposta: A resposta é 12.
```

**Ou importe e use diretamente no Python:**
```python
from agent_ollama import executar_agente

resultado = executar_agente("Quanto é 50 mais 75?")
print(resultado)
```

---

### O que é testado

| Classe | O que cobre |
|---|---|
| `TestFerramentas` | Cada operação matemática isolada (somar, subtrair, multiplicar, dividir, divisão por zero) |
| `TestExecutarAgente` | Loop do agente com Ollama mockado (com e sem tool calls) |

---

## 📁 Estrutura do projeto

```
projAgentsAI/
├── agent_ollama.py       # Agente principal
├── requirements.txt      # Dependências Python
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Este arquivo
```

---

## 🏗️ Como funciona (fluxo do agente)

```
Pergunta do usuário
        │
        ▼
   ollama.chat() ──── lista de ferramentas disponíveis
        │
        ▼
  Modelo raciocina
        │
   ┌────┴─────────────┐
   │ tool_calls?       │
   │ Sim               │ Não
   ▼                   ▼
Executa função    Retorna resposta
Python local       diretamente
   │
   ▼
ollama.chat() ── com resultado da ferramenta
   │
   ▼
Resposta final sintetizada
```

---

## 📦 Dependências principais

| Pacote | Versão | Uso |
|---|---|---|
| `ollama` | ≥ 0.6.2 | Comunicação com o modelo local |


