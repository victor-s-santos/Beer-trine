# Beer-trine
Construção de uma api simples, utilizando django e django rest framework, para construímos uma vitrine de cervejas.


## Como rodar

* Através de VirtualEnv
    1. Clone o repositório
        - git clone https://github.com/victor-s-santos/Beer-trine.git

    2. Crie sua virtualenv
        - com o terminal na raíz do projeto, rodar python -m venv .venv

    3. Ative sua virtualenv
        - source .venv/bin/activate

    4. Instale as dependências
        - pip install -r requirements.txt

    5. Rode as migrações
        - python manage.py migrate

    6. Suba o servidor
        - python manage.py runserver
