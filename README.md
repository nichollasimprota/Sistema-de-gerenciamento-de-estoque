# 📦 Sistema de Gerenciamento de Estoque

Um sistema de linha de comando (CLI) desenvolvido em Python para gerenciamento de estoque de produtos, com operações completas de CRUD (Create, Read, Update, Delete) e validação robusta de dados.

## ✨ Funcionalidades

- ➕ **Adicionar produto** — cadastra um novo produto com nome e quantidade
- 📋 **Listar produtos** — exibe todos os produtos cadastrados, com suas quantidades
- ✏️ **Atualizar produto** — altera a quantidade de um produto já existente
- 🗑️ **Remover produto** — exclui um produto do estoque
- ✅ **Validação de dados** — impede nomes vazios e quantidades inválidas (não numéricas ou negativas)
- 🔤 **Normalização de entrada** — nomes são padronizados (sem espaços extras e sem diferenciar maiúsculas/minúsculas), evitando duplicatas como "Caneta" e "caneta"

## 🛠️ Tecnologias

- **Python 3** — sem dependências externas, apenas biblioteca padrão
- **VScode** - IDE usada para a construção do codigo
## 🚀 Como executar

**Pré-requisito:** Python 3 instalado na máquina.

```bash
git clone https://github.com/nichollasimprota/Sistema-de-gerenciamento-de-estoque.git
cd Sistema-de-gerenciamento-de-estoque
python main.py
```
## 🧠 Principais aprendizados

Este projeto foi construído como exercício de fundamentos de Python, com foco em:

- Manipulação de dicionários como estrutura de dados
- Validação de entrada do usuário
- Organização de código em funções com responsabilidade única
- Uso de boas práticas como `if __name__ == "__main__":` e comentários 

## 👤 Autor

**Nichollas Improta Monteiro**
- Estudante de Engenharia de Software (4° semestre)
- [GitHub](https://github.com/nichollasimprota)
