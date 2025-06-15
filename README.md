# E-commerce de computadores

Um projeto de e-commerce funcional para venda de computadores e acessórios, desenvolvido com Python (Flask), HTML, CSS e JavaScript. O objetivo é simular uma loja online completa com páginas dinâmicas e coleta pro carrinho.

## Funcionalidades

- Página inicial com destaques e direcionada a página produtos  
- Listagem de produtos com botões de compra  
- Carrinho dinâmico com persistência de dados via `localStorage`  
- Formulário de contato  
- Página de login simples (template estático)

## Estrutura de Páginas

1. **Início** – Apresentação do e-commerce e banners promocionais  
2. **Produtos** – Cards de produtos com botão “Comprar”  
3. **Carrinho** – Produtos adicionados e valor total  
4. **Contato** – Formulário de contato para clientes  
5. **Login** – Página de autenticação

## Tecnologias Utilizadas

- **Backend:** Python 3.x + Flask  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Templates:** Jinja2 (via Flask)  
- **Armazenamento de dados:** localmente via `localStorage`
- **Controle de versões:** Git + GitHub

## Como rodar o projeto localmente

```bash
-Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

-Instale as dependências
pip install -r requitements.txt

-Execute o servidor Flask 
python app.py

-Acesse o projeto
http://127.0.0.1:5000

```
### 1. Clone o repositório

```bash
git clone https://github.com/gabrielesequeira/ecommerce.git
cd ecommerce
```