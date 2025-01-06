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
	<p>Um chatbot interativo criado com Python, utilizando tecnologias modernas como LangChain, LangGraph, e a API Groq, com o objetivo de responder perguntas, aprender com interações e armazenar informações relevantes. 🚀</p>
	<div class="chatbot">
		<img src="GIF-chatbot.gif" alt="GIF animado">
	</div>
	<h2> 💬Funcionalidades </h2>
	<ul>
		<li>Respostas precisas baseadas em inteligência artificial.</li>
		<li>Aprendizado contínuo com base nas interações dos usuários.</li>
		<li>Armazenamento inteligente de dados em um banco vetorial via Docker.</li>
		<li>Interface amigável desenvolvida em Streamlit.</li>
	</ul>
	
	<h2>🛠️Tecnologias Utilizadas</h2>
	<ul>
		<li><strong>🖥️Python 3.9+</strong></li>
        	<li><strong>🛠️ Streamlit</strong> para a interface do usuário</li>
        	<li><strong>🛠️ LangChain</strong> para orquestração de agentes e modelos de linguagem</li>
        	<li><strong>🛠️ LangGraph</strong> para integração com gráficos de conhecimento</li>
        	<li><strong>🤖 GROQ</strong> para utilizar o modelo de linguagem 'llama-3.3-70b-versatile'</li>
        	<li><strong>📂 SQLite</strong> para armazenamento de dados de aprendizado</li>
        	<li><strong>📂 Docker</strong> para containerização do ambiente</li>
	</ul>
 	<h2>📄Instruções de Instalação</h2>
	<ol>
		<li>Clone o repositório:
			<code>git clone https://github.com/usuario/chatbot_project.git</code>
		</li>
		<li>Entre no diretório do projeto:
			<code>cd chatbot_project</code>
		</li>
		<li>Instale as dependências:
			<code>pip install -r requirements.txt</code>
		</li>
		<li>Configure o arquivo `.env` com os seguintes valores:
			<code>
				api_base=https://api.groq.com/openai/v1<br>
				api_key=sua_chave_api
			</code>
		</li>
		<li>Certifique-se de que o Docker está rodando e execute o contêiner:
			<code>docker run -d -p 8501:8501 --name chatbot_container chatbot_project</code>
		</li>
		<li>Acesse o chatbot em:
			<a href="http://localhost:8501" target="_blank">http://localhost:8501</a>
		</li>
	</ol>
	<h2>📜Configurações Importantes</h2>
	<p>Certifique-se de que o Docker está configurado para suportar contêineres com bases de dados vetoriais.</p>
	
</body>
</html>
