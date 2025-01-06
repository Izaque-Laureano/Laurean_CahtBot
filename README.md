<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Interativo com Aprendizado Contínuo</title>
</head>
<body>
    <h1>Chatbot Interativo com Aprendizado Contínuo</h1>

    <p>Este projeto é um chatbot interativo desenvolvido em Python com aprendizado contínuo, utilizando as bibliotecas <strong>GROQ</strong>, <strong>Streamlit</strong>, <strong>LangChain</strong>, <strong>LangGraph</strong>, e uma base de dados vetorial em <strong>SQLite</strong> para armazenar as interações e aprendizados. O chatbot responde a perguntas e aprende/adapta-se com base nas interações do usuário.</p>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python 3.9+</strong></li>
        <li><strong>Streamlit</strong> para a interface do usuário</li>
        <li><strong>LangChain</strong> para orquestração de agentes e modelos de linguagem</li>
        <li><strong>LangGraph</strong> para integração com gráficos de conhecimento</li>
        <li><strong>GROQ</strong> para utilizar o modelo de linguagem 'llama-3.3-70b-versatile'</li>
        <li><strong>SQLite</strong> para armazenamento de dados de aprendizado</li>
        <li><strong>Docker</strong> para containerização do ambiente</li>
    </ul>

    <h2>Pré-requisitos</h2>
    <p>Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:</p>
    <ul>
        <li><a href="https://www.python.org/downloads/">Python 3.9+</a></li>
        <li><a href="https://www.docker.com/products/docker-desktop">Docker</a></li>
        <li><a href="https://git-scm.com/downloads">Git</a></li>
    </ul>

    <h2>Instalação</h2>
    <h3>Passo 1: Clone o Repositório</h3>
    <pre><code>git clone https://github.com/seu-usuario/chatbot-project.git
cd chatbot-project</code></pre>

    <h3>Passo 2: Crie e Ative um Ambiente Virtual</h3>
    <p>Recomenda-se o uso de um ambiente virtual para evitar conflitos de dependências.</p>
    <pre><code>python -m venv venv
source venv/bin/activate  # Para Linux/MacOS
venv\Scripts\activate     # Para Windows</code></pre>

    <h3>Passo 3: Instale as Dependências</h3>
    <pre><code>pip install -r requirements.txt</code></pre>
    <p>Isso irá instalar todas as bibliotecas necessárias para o funcionamento do chatbot.</p>

    <h3>Passo 4: Configuração do Groq</h3>
    <p>No seu arquivo de configuração (<code>config.py</code> ou no código principal), adicione as credenciais da <strong>API do GROQ</strong>:</p>
    <pre><code>api_base = "https://api.groq.com/openai/v1"
api_key = "seu-api-key-aqui"</code></pre>
    <p>Caso não tenha a chave de API, crie uma conta no site da <strong>Groq</strong> e gere a chave.</p>

    <h3>Passo 5: Construindo e Rodando o Docker (opcional)</h3>
    <h4>1. Construir a imagem do Docker:</h4>
    <pre><code>docker build -t chatbot_project .</code></pre>

    <h4>2. Rodar o contêiner:</h4>
    <pre><code>docker run -d -p 8501:8501 --name chatbot_container chatbot_project</code></pre>
    <p>A aplicação estará acessível em <a href="http://localhost:8501" target="_blank">http://localhost:8501</a>.</p>

    <h2>Executando a Aplicação Localmente</h2>
    <p>Para rodar a aplicação localmente, basta executar o seguinte comando:</p>
    <pre><code>streamlit run app.py</code></pre>
    <p>Isso abrirá a interface do Streamlit em seu navegador.</p>

    <h2>Exemplos de Uso</h2>
    <h3>Interação com o Chatbot</h3>
    <p>Na interface do Streamlit, basta digitar uma pergunta ou mensagem e o chatbot responderá com base no seu conhecimento atual. O modelo irá aprender com cada interação, adaptando-se ao longo do tempo.</p>

    <h3>Exemplos de Perguntas</h3>
    <ul>
        <li><strong>Qual é a capital da França?</strong></li>
        <li><strong>Me explique como funciona o aprendizado contínuo no chatbot.</strong></li>
        <li><strong>Quais são os conceitos de LangChain?</strong></li>
    </ul>
    <p>O chatbot irá fornecer uma resposta com base no conhecimento que possui até o momento.</p>

    <h2>Configurações Necessárias</h2>
    <h3>Banco de Dados</h3>
    <p>O projeto utiliza o <strong>SQLite</strong> para armazenar dados de interações e aprendizados. As interações dos usuários serão armazenadas em um banco de dados vetorial, que pode ser acessado para análises posteriores.</p>
    <p>Se for necessário alterar a configuração do banco de dados, você pode modificar a variável de conexão com o banco de dados no arquivo <code>db_config.py</code>.</p>

    <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções de bugs, sinta-se à vontade para abrir um <strong>Pull Request</strong> ou <strong>Issue</strong>.</p>
    <ol>
        <li>Faça um fork deste repositório.</li>
        <li>Crie uma nova branch (<code>git checkout -b minha-contribuicao</code>).</li>
        <li>Realize as modificações.</li>
        <li>Envie o Pull Request.</li>
    </ol>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a <strong>MIT License</strong> - consulte o arquivo <code>LICENSE</code> para mais detalhes.</p>
</body>
</html>
