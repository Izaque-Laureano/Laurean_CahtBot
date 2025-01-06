<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Interativo com Python</title>
</head>
<body>

    <h1>Chatbot Interativo com Python</h1>

    <p>Este é um chatbot interativo desenvolvido utilizando Python, Streamlit, LangChain, LangGraph, e a API da Groq. O chatbot é projetado para aprender continuamente com as interações dos usuários e armazenar informações em uma base de dados vetorial.</p>

    <h2>Instalação</h2>
    <p>Para rodar o projeto localmente, siga os seguintes passos:</p>
    
    <h3>1. Clonando o Repositório</h3>
    <pre>
    <code>
    git clone https://github.com/usuario/chatbot_project.git
    cd chatbot_project
    </code>
    </pre>

    <h3>2. Instalando as Dependências</h3>
    <p>O projeto utiliza algumas bibliotecas. Para instalá-las, execute o seguinte comando:</p>
    <pre>
    <code>
    pip install -r requirements.txt
    </code>
    </pre>

    <h3>3. Executando o Projeto</h3>
    <p>Depois de instalar as dependências, execute o seguinte comando para iniciar o chatbot localmente:</p>
    <pre>
    <code>
    docker run -d -p 8501:8501 --name chatbot_container chatbot_project
    </code>
    </pre>

    <h2>Exemplo de Uso</h2>
    <p>Depois de rodar o projeto, acesse a interface do chatbot em <a href="http://localhost:8501" target="_blank">http://localhost:8501</a>.</p>

    <h2>Configurações Necessárias</h2>
    <ul>
        <li>Configuração do Docker para executar a aplicação no contêiner.</li>
        <li>Chave da API da Groq configurada no código.</li>
        <li>Banco de dados vetorial configurado com Docker.</li>
    </ul>

    <h2>Git Ignore</h2>
    <p>Crie um arquivo .gitignore para evitar o versionamento de arquivos desnecessários, como ambientes virtuais e arquivos temporários:</p>
    <pre>
    <code>
    # Ignorar arquivos Python compilados
    *.pyc
    *.pyo
    *.pyd
    __pycache__/

    # Ignorar ambiente virtual
    venv/
    env/

    # Ignorar arquivos de log
    *.log

    # Ignorar banco de dados SQLite
    *.db
    *.sqlite3

    # Ignorar arquivos de configuração da IDE
    .vscode/
    .idea/
    </code>
    </pre>

</body>
</html>
