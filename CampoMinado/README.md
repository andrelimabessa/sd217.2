1. Setup Inicial
    #Linux
    pip install virtualenv
    virtualenv myvenv
    source myvenv/bin/activate

    #Windows
    pip install virtualenv
    virtualenv myvenv
    myvenv\Scripts\activate

    #Comandos Gerais
    pip install django

2. Criar projeto

    #Linux
    django-admin startproject mysite

    #Windows
    python myvenv\Scripts\django-admin.py startproject mysite .

3. Ajustando TIME_ZONE

    #Referência
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    #Comandos Gerais
    Abra o arquivo "settings.py" dentro da pasta "projeto"
    Altere TIME_ZONE para TIME_ZONE = 'America/Fortaleza'

4. Criando APP

    #Entre na pasta projeto e vamos criar uma aplicação dentro de projeto
    python manage.py startapp app

    Abra o arquivo "settings.py" dentro da pasta "projeto"
    Adicione:

        'app',

    no final de :
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app'
        ]

------------------------------> Model <----------------------------------------

5. Criando Models

    #Referência
    https://docs.djangoproject.com/pt-br/1.10/topics/db/models/

    #Comandos Gerais
    Abra o arquivo "models.py" dentro da pasta "app"
    Adicionar:

        from django.db import models
        from django.utils import timezone

        class Jogada(models.Model):
            linha = models.CharField(max_length=2)
            coluna = models.CharField(max_length=2)
            created_date = models.DateTimeField(default=timezone.now)


6. Criando Banco

    #Comandos Gerais
    Abra o arquivo "settings.py" dentro da pasta "projeto"
    Confirme:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

7. Criando migration da app

    #Comandos Gerais
    python manage.py makemigrations app
    python manage.py migrate

8. Subindo o servidor de aplicação

    #Comandos Gerais
    python manage.py runserver

    No navegador entre com a url http://127.0.0.1:8000/


------------------------------> View <----------------------------------------


9. Tratando arquivos estáticos

    #Comandos Gerais
    Abra o arquivo "settings.py" dentro da pasta "projeto"
    A baixo de  STATIC_URL adicione:

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    Crie a pasta "static" dentro da pasta "app"
    Crie as pastas "css" dentro da pasta "app/static"
    Crie as pastas "js" dentro da pasta "app/static"
    ... assim por diante

10. Tratar URL

    #Comandos Gerais
    Abra o arquivo "url.py" dentro da pasta "projeto"
    Observe a expressão regular REGEX:

        url(r'^admin/', admin.site.urls),

        Notação REGEX:

            ^  : para o início do texto
            $  : para o final do texto
            \d : para um dígito
            +  : para indicar que o item anterior deve ser repetido pelo menos uma vez
            () : para capturar parte do padrão

   Altetar :

        from django.conf.urls import url, include
        from django.contrib import admin

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'', include('app.urls')),
        ]

    Criar o arquivo "urls.py" dentro da pasta "app"
    Adicionar:

        from django.conf.urls import include, url
        from . import views

        urlpatterns = [

        ]

11. Criar View

    #Comandos Gerais
    Criar a pasta "templates" dentro de "app"
    Criar o arquivo "base.html" dentro de "app/templates"
    Abra o arquivo 'base.html'
    Adicione:

        {% load staticfiles %}
        <html>
            <head>
                <title>Bessalha Naval</title>
                <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
                <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
                <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            </head>
            <body>
                <div class="page-header">
                    <h1><a href="/">Campo Minado</a></h1>
                </div>

                <div class="content container">
                    <div class="row">
                        <div class="col-md-8">
                        {% block content %}
                        {% endblock %}
                        </div>
                    </div>
                </div>
            </body>
        </html>

    Criar o arquivo "post_list.html" dentro de "app/templates"
    Abra o arquivo 'post_list.html'
    Adicione:

        {% extends 'base.html' %}

        {% block content %}

            <p>Funcionando</p>

        {% endblock %}

    Abra o arquivo "views.py" dentro da pasta "app"
    Adicione:

        def post_list(request):
            return render(request, 'post_list.html', {})        

    Abri o arquivo "urls.py" dentro da pasta "app"
    Adicionar:

        from django.conf.urls import include, url
        from . import views

        urlpatterns = [
            url(r'teste/$', views.post_list),    
        ]

12. Django QuerySet

    #Comandos Gerais
    Shell de acesso ao banco de dados:

        python manage.py shell

    Import o model que deseja pesquisar:

        from app.models import Jogada

    Teste as seguintes consultas :

        Obter todos os registros da tabela "Jogada":
            Jogada.objects.all()

        Criar uma nova "Jogada"

            Jogada.objects.create( linha='1', coluna='1')

        Buscar com filtro:

            Jogada.objects.filter(linha='1')
            Jogada.objects.get(id=1)


------------------------------> Forms <----------------------------------------

14. Criar um Form para Enviar Jogadas

    #Comandos Gerais
    Crie o arquivo "forms.py" dentro da pasta "app"
    Abra o arquivo "forms.py" dentro da pasta "app"
    Adicionar:

        from django import forms
        from .models import Jogada

        class JogadaForm(forms.ModelForm):

            class Meta:
                model = Jogada
                fields = ('linha','coluna')

    Abra o arquivo "views.py" dentro da pasta "app"
    Altere:

        def post_list(request):
            form = JogadaForm()
            return render(request, 'post_list.html', {'form': form})

    Abra o arquivo "post_list.html" dentro da pasta "templates"
    Altere:

        {% extends 'base.html' %}

        {% block content %}

            <h1>Nova Jogada</h1>
            <form method="POST" class="post-form">{% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="save btn btn-default">salvar</button>
            </form>

        {% endblock %}

16. Salvar a Jogada

    #Comandos Gerais
    Abra o arquivo "views.py" dentro da pasta "app"
    Altere:

        def post_list(request):

            if request.method == "POST":
                form = JogadaForm(request.POST)
                if form.is_valid():
                    jogada = form.save(commit=False)
                    jogada.created_date = timezone.now()
                    jogada.save()
            else:
                form = JogadaForm()

            return render(request, 'post_list.html', {'form': form})

17. Exibir Jogadas Salvas

    #Comandos Gerais

    Abra o arquivo "views.py" dentro da pasta "app"
    Altere:

        def post_list(request):
        if request.method == "POST":
            form = JogadaForm(request.POST)
            if form.is_valid():
                jogada = form.save(commit=False)
                jogada.created_date = timezone.now()
                jogada.save()
        else:
            form = JogadaForm()

        jogadas = Jogada.objects.all()

        return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})

    Abra o arquivo "post_list.html" dentro da pasta "templates"
    Altere o "block content" para ficar assim:

        <h1>Nova Jogada</h1>
        <form method="POST" class="post-form">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-default">Jogar</button>
        </form>

        <div class="box-body">
            <table>
                <thead>
                    <tr>
                        <th>Linha </th>
                        <th>Coluna </th>
                    </tr>
                </thead>
                <tbody>
                    {% for jogada in jogadas %}
                    <tr>
                        <td>{{ jogada.linha }}</td>
                        <td>{{ jogada.coluna }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

    https://docs.djangoproject.com/en/1.11/topics/forms/
