# Criando-um-Validador-de-Bandeiras-de-Cart-o-de-Cr-dito-com-o-GitHub-Copilot

# 💳 Validador de Bandeiras de Cartão de Crédito

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Testes](https://img.shields.io/badge/testes-automatizados-green)

Projeto criado como parte do desafio da DIO para utilização prática do GitHub Copilot na construção de um validador de bandeiras de cartões de crédito.  
A proposta é identificar automaticamente se o número inserido pertence a bandeiras como **Visa**, **MasterCard**, **Amex**, **Discover**, entre outras.

---

## ✨ Funcionalidades

- 🔎 Identificação automática da bandeira do cartão com base no número
- 🤖 Sugestões assistidas por GitHub Copilot
- ✅ Testes automatizados com Pytest
- 🧠 Uso de expressões regulares para reconhecimento preciso

---

## 💡 Tecnologias Utilizadas

| Ferramenta | Descrição |
|------------|-----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Linguagem base |
| ![Regex](https://img.shields.io/badge/-Regex-E34F26?logo=regex&logoColor=white) | Validação de padrões |
| ![GitHub Copilot](https://img.shields.io/badge/-GitHub%20Copilot-000000?logo=github&logoColor=white) | Assistência IA |
| ![Pytest](https://img.shields.io/badge/-Pytest-6DB33F?logo=pytest&logoColor=white) | Testes automatizados |

---

## 🚀 Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/seuusuario/card-validator.git
cd card-validator
```

### 2. Execute o script principal

```bash
python main.py
```

Você verá:

```
Digite o número do cartão: 4111111111111111
Bandeira detectada: Visa
```

### 3. Execute os testes

```bash
pytest test_card_validator.py
```

---

## 🧪 Exemplos de Cartões de Teste

| Número de Teste | Bandeira Esperada     |
|-----------------|-----------------------|
| 4111111111111111| Visa                  |
| 5555555555554444| MasterCard            |
| 378282246310005 | American Express (Amex)|
| 6011111111111117| Discover              |
| 3530111333300000| JCB                   |

---

## 📁 Estrutura do Projeto

```
card-validator/
├── card_validator.py
├── main.py
├── test_card_validator.py
├── README.md

## 🧠 Aprendizados

- Como estruturar uma aplicação simples e eficaz com IA
- Aplicação prática do GitHub Copilot no dia a dia
- Domínio sobre expressões regulares e testes unitários
- Documentação clara e atrativa com Markdown
