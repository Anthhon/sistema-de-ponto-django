# Ponto Eletrônico

Este projeto foi criado com o intuito de **facilitar o registro de horários de entrada e saída de fácil e rápida!** O projeto tem como alvo programadores que estejam procurando implementar um sistema do tipo em empresa de pequeno a médio porte.

O sistema conta com aba de inicial onde será feita o registro de horários e uma aba de **gerenciamento de funcionários, exibição de histórico de horas e funcionários e etc.**

## Tecnologias utilizados

### Ferramentas

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Plugins

- [jazzmin:]() Usado para personalizar e estilizar a aba de administrador

## Como usar

### Clonando e organizando o repositório

Vá até o diretório onde deseja estar instalando o sistema e **clone o repositório com o comando:**

`git clone https://github.com/Anthhon/sistema-de-ponto-django.git`

Opcionalmente, caso não queira pode ir ao próximo passo, **crie um ambiente virtual para instalar os pacotes `pip`** que serão necessários com o seguinte comando:

`python -m venv /diretorio/do/novo/ambiente/nome_do_ambiente_virtual`

Em seguida ative o ambiente virtual com o comando:

`source nome_do_ambiente_virtual/bin/activate`

Veja mais sobre [clicando aqui.](https://docs.python.org/3/library/venv.html)

### Instalando as dependências

Agora antes de iniciar o projeto **é necessário que sejam instaladas todas as dependências `pip`,** as mesmas, se encontram listadas dentro do arquivo [requirements.txt](./requirements.txt), para isso, use o seguinte comando:

`pip install -r requirements.txt`

Veja mais sobre [clicando aqui.](https://stackoverflow.com/questions/41457612/how-to-fix-error-with-freetype-while-installing-all-packages-from-a-requirements)

### Rodando o projeto

Vá até o diretório onde se encontra o arquivo `manage.py` e rode os seguintes comandos para **realizar as migrações necessárias** para que o projeto funcione:

```
python manage.py makemigrations
python manage.py migrate 
```

Veja mais sobre [clicando aqui.](https://docs.djangoproject.com/en/4.2/topics/migrations/#:~:text=There%20are%20several%20commands%20which,have%20made%20to%20your%20models.)

Após isso, você já pode **rodar o projeto** com o comando:

`python manage.py runserver`

Se tudo ocorrer como deveria, **deve ser exibido pra você um IP local com o sistema funcionando.** Após isso, caso necessário, basta apenas fazer as personalizações pessoais que atendam a necessidade do seu projeto.

### Criando um super usuário

Para criar um usuário de administrador para acessar a aba `/admin` basta rodar o seguinte comando:

`python manage.py createsuperuser`

Veja mais sobre [clicando aqui.](https://www.educative.io/answers/how-to-create-a-superuser-in-django#:~:text=Start%20the%20terminal%20by%20clicking,a%20superuser%20will%20be%20created.)

## Screenshots

[![Dqig99.md.png](https://iili.io/Dqig99.md.png)](https://freeimage.host/i/Dqig99)
[![DqbP5l.md.png](https://iili.io/DqbP5l.md.png)](https://freeimage.host/i/DqbP5l)

## Desenvolvedores

- [@Anthony Silva](https://www.github.com/Anthhon)
- [@Jonathas David](https://github.com/Rip4568)

## Licença

Esse sistema é distribuido sobre a licensa do MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
