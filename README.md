#
<!DOCTYPE html>
<html>
<header>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laurean Chatbot Interativo com Python 🤖💬</title>
</header>
<body>

    <h1>Laurean Chatbot Interativo com Python 🤖💬</h1>

    <p>Bem-vindo ao projeto do Laurean Chatbot! Este chatbot é construído com Python e utiliza a API da Groq, Streamlit, LangChain e LangGraph para proporcionar uma experiência interativa única. O chatbot aprende com cada interação e armazena informações de forma eficiente em um banco de dados vetorial. 🚀</p>

    <h2>📦 Instalação</h2>
    <p>Para rodar este projeto localmente, siga os passos abaixo:</p>
    
    <h3>1. Clonando o Repositório 🔽</h3>
    <pre>
    <code>
    git clone https://github.com/usuario/chatbot_project.git
    cd chatbot_project
    </code>
    </pre>

    <h3>2. Instalando as Dependências 🛠️</h3>
    <p>O projeto utiliza algumas bibliotecas. Instale todas as dependências executando:</p>
    <pre>
    <code>
    pip install -r requirements.txt
    </code>
    </pre>

    <h3>3. Executando o Projeto 🚀</h3>
    <p>Após a instalação das dependências, execute o seguinte comando para rodar o chatbot em seu computador:</p>
    <pre>
    <code>
    docker run -d -p 8501:8501 --name chatbot_container chatbot_project
    </code>
    </pre>
    <p>Isso irá rodar o chatbot em um contêiner Docker, acessível via <a href="http://localhost:8501" target="_blank">http://localhost:8501</a>. 🖥️</p>

    <h2>💬 Exemplo de Uso</h2>
    <p>Após rodar o projeto, acesse a interface do chatbot em <a href="http://localhost:8501" target="_blank">http://localhost:8501</a> e comece a interagir com ele! Você pode fazer perguntas e o chatbot irá aprender com suas respostas. 🤓</p>

    <h2>⚙️ Configurações Necessárias</h2>
    <ul>
        <li>Certifique-se de que o Docker está configurado corretamente em sua máquina. 🐳</li>
        <li>Configure a chave da API da Groq no código. 🔑</li>
        <li>O banco de dados vetorial precisa estar configurado com Docker. 💾</li>
    </ul>

    <h2>📝 Git Ignore</h2>
    <p>Crie um arquivo <code>.gitignore</code> para evitar o versionamento de arquivos desnecessários, como ambientes virtuais e arquivos temporários:</p>
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

    <h2>👨‍💻 Contribuindo</h2>
    <p>Se você deseja contribuir para o projeto, fique à vontade para abrir issues ou pull requests. Juntos podemos melhorar ainda mais este chatbot! 💡</p>

    <h2>📄 Licença</h2>
    <p>Este projeto é licenciado sob a MIT License - veja o arquivo <a href="LICENSE" target="_blank">LICENSE</a> para mais detalhes. 📃</p>

</body>
</html>
