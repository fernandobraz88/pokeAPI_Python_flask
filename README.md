# Documentação da API de Times de Pokémon
## Introdução
Esta API permite aos usuários criar e gerenciar times de Pokémon. Utilizando a PokeAPI para buscar informações detalhadas sobre cada Pokémon, os usuários podem registrar times, listar todos os times existentes, e buscar times por usuário. Esta documentação fornece todas as informações necessárias para começar a usar a API, incluindo detalhes sobre os endpoints disponíveis, exemplos de uso e instruções para rodar a aplicação em um container Docker.

## Configuração do Ambiente
Para utilizar esta API, você precisa ter Python e Flask instalados em seu ambiente. Siga os passos abaixo para configurar seu ambiente:

* Certifique-se de ter o Python 3.8 ou superior instalado em seu sistema.
* Use o pip para instalar Flask e Requests. __(pip install Flask requests)__
* Clone o código fonte da API do repositório Git para seu ambiente local.

## Uso da API

### Endpoints Disponíveis

1. Listar Todos os Times
* __Método__: GET
* __Endpoint__: /api/teams
* __Descrição__: Retorna uma lista de todos os times registrados.

2. Buscar Time por Usuário
* __Método__: GET
* __Endpoint__: /api/teams/{user}
* __Descrição__: Busca um time registrado pelo nome do usuário.

3. Criar um Novo Time
* __Método__: POST
* __Endpoint__: /api/teams
* __Descrição__: Registra um novo time com base em uma lista de Pokémons fornecida.
* __Corpo da Requisição__:(JSON)
{  
  "user": "nome_do_usuario",  
  "team": ["pokemon1", "pokemon2", "pokemon3", "pokemon4", "pokemon5", "pokemon6"]  
}
## Manipulação de Erros
A API usa códigos de status HTTP padrão para indicar o sucesso ou falha de uma requisição.  Por exemplo, um código 404 é retornado quando um Pokémon específico não é encontrado, e um código 400 é retornado quando a requisição está malformada ou faltando dados necessários.

### Possiveis Erros:
1. Buscando time por usuário:
* __"Team not found"__: Usuario procurado não cadastrado.

2. Criando Times:
* __"User and team are required"__: Necessário repassar um usuário e um time de pokemons, caso contrário esse erro é retornado.
* __"Pokemon {name} not found"__: O pokemon não existe ou seu nome está escrito de forma incorreta.

## Utilizando a API em container Docker:
Utilizando o terminal no diretório criado:  
Execute o comando: __docker-compose up --build__
