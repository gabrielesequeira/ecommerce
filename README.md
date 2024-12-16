# E-commerce
## Descrição do Sistema

### Um e-commerce onde os usuários podem:
- Navegar por categorias de produtos.
- Adicionar e remover itens do carrinho.
- Finalizar compras.
- Pesquisar produtos por nome.
- Ver recomendações personalizadas.

### Componentes Essenciais

- Banco de Dados Simulado (Estruturas de Dados)
- Interface do Usuário (Front-end)
- Lógica de Negócio (Back-end)
- Algoritmos de Busca e Recomendação

### Arquivos do Projeto e Tecnologias / Conceitos Usados

1. backend/app.py
Descrição: É o ponto de entrada para o back-end, gerencia o servidor Flask e inicializa a aplicação.
Tecnologias Usadas:
Flask: Framework para construir aplicações web no back-end.
Conceitos Usados:
Arquitetura cliente-servidor.
Roteamento de URLs para lidar com diferentes solicitações (ex.: /products, /cart).
APIs RESTful para a comunicação entre front-end e back-end.
2. backend/database.py
Descrição: Configura o banco de dados da aplicação, incluindo a conexão e operações básicas.
Tecnologias Usadas:
SQLAlchemy (ou qualquer ORM): Facilita a interação entre o código Python e o banco de dados.
Conceitos Usados:
Persistência de dados.
Modelo relacional, organizando informações como usuários, produtos e pedidos em tabelas.
Estruturas de dados (listas e dicionários, para simulações locais).
3. backend/models.py
Descrição: Define os modelos (classes) que representam as tabelas do banco de dados.
Tecnologias Usadas:
SQLAlchemy ou similar para mapear modelos Python em tabelas.
Conceitos Usados:
Mapeamento Objeto-Relacional (ORM) para vincular classes Python a tabelas no banco de dados.
Estruturas de dados, como listas e dicionários, para representar registros em memória.
4. backend/routes.py
Descrição: Define as rotas da API, conectando as requisições do cliente à lógica do back-end.
Tecnologias Usadas:
Flask (Blueprints para modularizar rotas).
Conceitos Usados:
APIs RESTful para comunicação eficiente entre front-end e back-end.
Lógica de controle para validar e processar requisições.
5. backend/__init__.py
Descrição: Faz o diretório backend ser reconhecido como um módulo Python, permitindo importações organizadas.
Tecnologias Usadas:
Python.
Conceitos Usados:
Modularidade no desenvolvimento de software.
6. frontend/index.html
Descrição: Define a estrutura da interface visual principal do e-commerce.
Tecnologias Usadas:
HTML.
Conceitos Usados:
Semântica e organização para uma experiência de navegação clara.
Conexão com os arquivos CSS e JavaScript para estilização e funcionalidade.
7. frontend/styles.css
Descrição: Estiliza os elementos visuais da página, controlando layout, cores e fontes.
Tecnologias Usadas:
CSS.
Conceitos Usados:
Box Model para organização de elementos.
Responsividade com Media Queries.
Design visual para melhorar a experiência do usuário.
8. frontend/app.js
Descrição: Gerencia a lógica do lado do cliente, como eventos de cliques, chamadas para a API e manipulação do DOM.
Tecnologias Usadas:
JavaScript.
Conceitos Usados:
Manipulação de eventos e DOM para criar uma interface interativa.
Comunicação assíncrona com o back-end usando Fetch API ou Axios.
9. .gitignore
Descrição: Lista arquivos e diretórios que não devem ser enviados ao repositório Git.
Tecnologias Usadas:
Git.
Conceitos Usados:
Boas práticas de controle de versão, ignorando arquivos desnecessários como configurações locais, caches e bibliotecas instaladas.
10. requirements.txt
Descrição: Lista as bibliotecas necessárias para rodar a aplicação.
Tecnologias Usadas:
Python (pip para gerenciar dependências).
Conceitos Usados:
Gerenciamento de dependências para garantir consistência entre os ambientes de desenvolvimento e produção.