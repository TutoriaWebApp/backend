# Backend do TutoriaWebApp

Este repositório tem como objetivo apresentar o backend do Trabalho de Conclusão de Curso dos alunos Lucas e Rodrigo.

## Pré requisitos
- Docker
- Docker Compose

## Como executar

Crie o seu arquivo `.env` de configuração de ambiente, como o exemplo `env/.env.example`:

```sh
cp env/.env.example env/.env
```

Para executar o programa inicie o docker

```
docker-compose --env-file ./env/.env up --build -d
```

## Endpoints de [localhost:8000/v1](http://localhost:8000/v1)

- [/](http://localhost:8000/v1/): É possível verificar os links disponíveis para a API
- [/usuarios/novo](http://localhost:8000/v1/usuarios/novo) Cria novo Usuário (POST)<br>
	```js
	// Exemplo em javascript
	const formData = new FormData();
	formData.append('email', 'teste@email.com');
	formData.append('nomePerfil', 'Meu Nome');
	formData.append('estado', 'DF');
	formData.append('cidade', 'Brasília');
	formData.append('aniversário', '2026-12-31');
	if (fotoFile) {
		formData.append('foto', fotoFile);
	}

	const response = await fetch(`http://localhost:8000/v1/usuarios/${idUsuario}`, {
		method: 'PUT',
		body: formData,
	});
	```
- [/usuarios](http://localhost:8000/v1/usuarios) Lista usuários (GET), retorna no padrão JSON.<br>
	```json
	[
		{
			"email": "",
			"password": "",
			"nomePerfil": "",
			"cidade": "",
			"estado": ""
		},
	]
	```
- [/usuarios/:id](http://localhost:8000/v1/usuarios/:id)
	- Dados de um usuário (GET) retorna no padrão JSON.<br>
		```json
		{
			"email": "",
			"nomePerfil": "",
			"estado": "",
			"cidade": "",
			"aniversario": "",
			"pontuacao": "",
			"fotoURL": "",
			"foto"
		}
		```
	- Alterar dados de um usuário (PUT), o formato deve ser FormData, para enviar os dados do usuário:
		```js
		// Exemplo em javascript
		const formData = new FormData();
		formData.append('email', 'teste@email.com');
		formData.append('nomePerfil', 'Meu Nome');
		formData.append('estado', 'DF');
		formData.append('cidade', 'Brasília');
		formData.append('aniversário', '2026-12-31');
		if (fotoFile) {
			formData.append('foto', fotoFile);
		}

		const response = await fetch(`http://localhost:8000/v1/usuarios/${idUsuario}`, {
			method: 'PUT',
			body: formData,
		});
		```
- [/conquistas](http://localhost:8000/v1/conquistas) Lista as conquistas (Só é possível criar novas na dashboard de admin)
- [/conquistas/usuario/:usuarioId](http://localhost:8000/v1/conquistas/usuario/1) Lista as conquistas do usuario
- [consegue](http://localhost:8000/v1/consegue) Lista conquistas dos usuarios (GET) ou cria novo relacionamento de usuário com a conquista (POST)
	```json
	{
		"usuarioId": "",
		"conquistaId": ""
	}
	```
- [/tutor](http://localhost:8000/v1/tutor) Lista os tutores (GET), ou cria Tutor (POST)
	```json
	{
		"usuarioId": ""
	}
	```
- [/sessoes](http://localhost:8000/v1/sessoes) Lista as sessoes dos tutores (GET), ou cria Sessão para o tutor
	```json
	{
		"horaInicio": "HH:mm",
		"horaFim": "HH:mm",
		"dia": "SEG",
		"tutorId": ""
	}
	```
- [/solicitacao](http://localhost:8000/v1/solicitacao) Lista solicitacoes dos usuarios (GET), ou cria uma nova solicitação para a Sessão (POST)
	```json
	{
		"sessaoId": ""
	}
	```
<!-- - [](http://localhost:8000/v1/) -->
