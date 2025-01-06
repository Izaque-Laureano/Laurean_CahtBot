<!DOCTYPE html>
<html>
<header>
	<link rel="stylesheet" type="text/css" href="/style.css">
	<div class="Titulo">
		<img src="Gif-Titulo.gif" alt="GIF animado">
	</div>
</header>
<body>
	<h1>🤖Chatbot Interativo</h1>
	<p>Um chatbot interativo construído com Python, utilizando tecnologias como LangChain, LangGraph e a API da Groq. Este projeto permite ao chatbot aprender com as interações dos usuários e armazenar informações de forma eficiente em um banco de dados vetorial. 🚀</p>
	<div class="chatbot">
		<img src="GIF-chatbot.gif" alt="GIF animado">
	</div>
	<h2>💬Funcionalidades</h2>
	<p>O chatbot oferece:</p>
	<ul>
		<li>Respostas precisas e adaptáveis às perguntas do usuário.</li>
		<li>Aprendizado contínuo com base nas interações.</li>
		<li>Interface intuitiva construída com Streamlit.</li>
		<li>Armazenamento de informações relevantes em um banco de dados vetorial.</li>
	</ul>
	<h2>🛠️Tecnologias Utilizadas</h2>
	<p>O projeto utiliza:</p>
	<ul>
		<li>Linguagem: Python 🐍</li>
		<li>Frameworks: Streamlit, LangChain e LangGraph</li>
		<li>Banco de Dados: SQLite (local) e base vetorial em contêiner Docker</li>
		<li>Modelo de Linguagem: API da Groq</li>
	</ul>
	<h2>📄Instruções de Instalação</h2>
	<ol>
		<li>Clone este repositório com o comando:
			<pre>
				<code>git clone https://github.com/usuario/chatbot_project.git</code>
			</pre>
		</li>
		<li>Entre na pasta do projeto:
			<pre>
				<code>cd chatbot_project</code>
			</pre>
		</li>
		<li>Instale as dependências necessárias:
			<pre>
				<code>pip install -r requirements.txt</code>
			</pre>
		</li>
		<li>Certifique-se de que o Docker está instalado e rodando. Em seguida, execute:
			<pre>
				<code>docker run -d -p 8501:8501 --name chatbot_container chatbot_project</code>
			</pre>
		</li>
		<li>Acesse o chatbot no navegador em:
			<a href="http://localhost:8501" target="_blank">http://localhost:8501</a>
		</li>
	</ol>
	<h2>🎞Créditos</h2>
	<ul>
		<li>Desenvolvedor: [Seu Nome]</li>
		<li>🎶Recursos de áudio: [Inserir se aplicável]</li>
		<li>🎨Recursos gráficos: [Inserir se aplicável]</li>
	</ul>
	<h2>📜Licença</h2>
	<p>Este projeto está sob a licença <a href="https://opensource.org/licenses/MIT">MIT</a>.</p>
</body>
</html>
