# Cinetox

Aplicação web desenvolvida em Python e Django 5 para consulta, filtragem e paginação de um catálogo de filmes, como atividade prática da disciplina de Programação para Internet.

## Integrantes da dupla

- Níkolas Feitoza Duarte
- Ana Ketelly Lopes Fernandes

## Tema escolhido

Catálogo de Filmes, gerenciado pelo app filmes com os modelos Filme, Diretor e Categoria.

## Funcionalidades e filtros implementados

- Listagem de filmes: exibe título, diretor, categoria e ano de lançamento a partir de consultas com o ORM do Django.
- Pesquisa textual (q): busca filmes pelo título usando titulo__icontains via método GET.
- Filtros dinâmicos (diretor e categoria): dois campos select enviados via GET que funcionam sozinhos ou combinados entre si e com a pesquisa textual.
- Paginação (page): exibição de 5 registros por página usando a classe Paginator do Django, após a aplicação dos filtros.
- Preservação dos filtros na paginação: os parâmetros ativos (q, diretor e categoria) são mantidos na URL ao navegar entre as páginas anterior e seguinte.

## Captura de tela

[Paginação](docs/pg1.png)
[Paginação](docs/pg2.png)
[Paginação](docs/pg3.png)

## Como executar localmente

```bash
git clone <url-do-repositorio>
cd cinetox
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver