<!DOCTYPE html>
<html>
<header>
	<link rel="stylesheet" type="text/css" href="/style.css">
	<div class="Titulo">
		<img src="Gif-Titulo.gif" alt="GIF animado">
	</div>
</header>
<body>
	<h1>🤖Laurean Chatbot</h1>
	<p>Um chatbot interativo criado com Python, utilizando tecnologias modernas como LangChain, LangGraph, e a API Groq. O objetivo é responder perguntas, aprender com interações e armazenar informações relevantes. 🚀</p>
	<div class="chatbot">
		<img src="GIF-chatbot.gif" alt="GIF animado">
	</div>
	<h2>🛠️Pré-requisitos</h2>
	<ul>
		<li>🐍 Python 3.8 ou superior instalado (<a href="https://www.python.org/downloads/" target="_blank">Baixar Python</a>).</li>
		<li>🐋 Docker Desktop instalado (<a href="https://www.docker.com/products/docker-desktop" target="_blank">Baixar Docker</a>).</li>
		<li>📦 Git instalado (<a href="https://git-scm.com/downloads" target="_blank">Baixar Git</a>).</li>
		<li>🖥️ Conexão com a internet para baixar dependências e acessar a API Groq.</li>
	</ul>
	<h2>📄Instruções de Instalação</h2>
	<ol>
		<li>Clone o repositório:
			<code>git clone https://github.com/Izaque-Laureano/Laurean_CahtBot.git</code>
		</li>
		<li>Entre no diretório do projeto:
			<code>cd Laurean_CahtBot</code>
		</li>
		<li>Crie um ambiente virtual:
			<code>python -m venv venv</code>
		</li>
		<li>Ative o ambiente virtual:
			<ul>
				<li>Windows:
					<code>venv\Scripts\activate</code>
				</li>
				<li>Linux/Mac:
					<code>source venv/bin/activate</code>
				</li>
			</ul>
		</li>
		<li>Instale as dependências:
			<code>pip install -r requirements.txt</code>
		</li>
		<li>Configure o arquivo `.env` com as credenciais da API Groq:
			<code>
				api_base=https://api.groq.com/openai/v1<br>
				api_key=sua_chave_api
			</code>
		<li>
		Baixe a imagem docker com o nome chatbot_project:
			<code>docker build -t chatbot_project . </code>
		</li>
		</li>
		<li>Certifique-se de que o Docker está rodando e execute o contêiner:
			<code>docker run -d -p 8501:8501 --name chatbot_container chatbot_project</code>
		</li>
		<li>Acesse o chatbot em:
			<a href="http://localhost:8501" target="_blank">http://localhost:8501</a>
		</li>
	</ol>
	<h2>🕹️Exemplo de Uso</h2>
	<ol>
		<li>Inicie a aplicação e faça uma pergunta no campo de texto.</li>
		<li>Receba uma resposta do Laurean ChatBot baseada na inteligência artificial.</li>
		<li>Interaja com o chatbot para verificar o aprendizado contínuo.</li>
	</ol>
	<h2>🛠️Tecnologias Utilizadas</h2>
	<ul>
		<li>🖥️ Linguagem: Python</li>
		<li>📚 Frameworks e Bibliotecas: Streamlit, LangChain, LangGraph</li>
		<li>📂 Banco de Dados: SQLite e base vetorial em contêiner Docker</li>
		<li>🤖 Modelo de Linguagem: API da Groq</li>
	</ul>
	<h2>📜Configurações Importantes</h2>
	<p>Certifique-se de que o Docker está configurado para suportar contêineres com bases de dados vetoriais.</p>
	
</body>
</html>
