
  

# Teste de qualidade do sono Pittsburgh

  

A aplicação do **Teste de Qualidade do Sono de Pittsburgh (PSQI)** é uma ferramenta voltada para a avaliação da qualidade do sono em indivíduos. Com base em um questionário amplamente validado e utilizado na prática clínica e em pesquisas, a aplicação permite identificar padrões de sono, possíveis distúrbios e áreas que possam requerer intervenção para melhorar a saúde do sono.

  

#### Objetivo:

  

O PSQI foi desenvolvido para medir a qualidade do sono ao longo do último mês, analisando componentes como:

  

- Duração do sono

- Latência para dormir (tempo até pegar no sono)

- Eficiência do sono

- Perturbações durante a noite

- Uso de medicamentos para dormir

- Nível de sonolência durante o dia

  

#### Funcionalidades:

  

-  **Questionário interativo:** O usuário responde de uma forma leve a uma série de perguntas que avaliam diferentes aspectos do sono.

-  **Cálculo automático da pontuação:** Com base nas respostas fornecidas, o sistema gera automaticamente uma pontuação total e por componentes, que varia de 0 a 21 (quanto maior a pontuação, pior a qualidade do sono).

-  **Interpretação dos resultados:** A aplicação fornece uma análise simples do resultado, ajudando o usuário a identificar se apresenta um padrão de sono saudável ou se precisa de ajustes.

-  **Armazenamento de resultados:** Os dados podem ser armazenados para acompanhamento ao longo do tempo e comparação com testes anteriores.

  

***

# Instalação

  

-  **Clone este repositório**:

  

```bash

git  clone  https://github.com/gabrielssrufino/PSQI_test.git

```

-  **Navegue para a pasta do projeto**

  

-  **Navegue para a pasta "API"**

  

#### **Crie um ambiente virtual (opcional, mas recomendado)**:

  

-  **Windows**:

  

```bash

python  -m  venv  venv

```

  

-  **Linux**:

  

```bash

python3  -m  venv  venv

```

  

#### **Ativar ambiente virtual (caso tenha criado o ambiente)**:

  

-  **Windows**:

  

```bash

.\venv\Scripts\activate

```

  

-  **Linux**:

  

```bash

source venv/bin/activate

```

  

-  **Instale as dependências:**

  

```bash

pip install -r requirements.txt

```

***

# Como usar

  

-  **Ainda na pasta "API"**

  

1.  **Migre o banco de dados**

  

```bash

python manage.py migrate

```

  

2.  **Crie um super usuário(caso queira acessar o painel de administração)**

  

```bash

python manage.py createsuperuser

```

Sigas as instruções

  

3.  **Inicie o servidor**

  

```bash

python manage.py runserver

```

***

# Interação

  

1.  **Volte uma pasta**

  

2.  **Abra a pasta Frontend**

  

3.  **Abra o arquivo "index.html" diretamente no navegador e siga as instruções na tela.**

  
  

***

  
  

# Observações

**Você encontrará um arquivo chamado "PSQI.postman_collection.json" na raiz do projeto. Esse arquivo contém uma collection do Postman completa, dividida em pastas por assunto e explicando cada uso.**

### Como importar a collection no Postman:

1. Abra o Postman.

2. Clique em "Import" no canto superior esquerdo.

3. Selecione o arquivo `PSQI.postman_collection.json`.

4. A collection será importada e você poderá explorar as requisições configuradas.

***
# Fotos

<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1ZSsLRi9iRdlmOvkyI61jGTg30-RVCiyj">

<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1w1WdbviXifrjmtQZa9eyOn9_1HQCBFc0">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1w6ieUzrGoXNCesICcsORs0Wm3je-upRY">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1foDGsSDcKwgXq4v7hTF9_SMmRz6vAj6y">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1yfvtdvqPsm3vMb6lkWzDneA5wuOhohLF">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=13y6iltvzzNBLjdwsTQIGu27oSys6LSSJ">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=11pZM1AM4uFOgXFvcAwe2gfLNdyBoO4-U">
<img align="left" alt="Imagem" height="auto" width="85%" src="https://drive.google.com/uc?id=1ESDzlZvwFQEpSQWyUHkgFtMVe_zo2ia5">


