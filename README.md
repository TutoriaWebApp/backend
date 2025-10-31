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
docker-compose --env-file /env/.env up --build -d
```

## Endpoints de [localhost:8080/v1](http://localhost:8080/v1)

- [/](http://localhost:8080/v1/): É possível verificar os links disponíveis para a API
- [/usuarios](http://localhost:8080/v1/usuarios) Lista usuários (GET), ou cria usuário (POST)<br>
	```json
	{
		"email": "",
		"password": "",
		"nomePerfil": "",
		"cidade": "",
		"estado": "",
		"urlFoto": ""
	}
	```
- [/conquistas](http://localhost:8080/v1/conquistas) Lista as conquistas (Só é possível criar novas na dashboard de admin)
- [/conquistas/usuario/:usuarioId](http://localhost:8080/v1/conquistas/usuario/1) Lista as conquistas do usuario
- [consegue](http://localhost:8080/v1/consegue) Lista conquistas dos usuarios (GET) ou cria novo relacionamento de usuário com a conquista (POST)
	```json
	{
		"usuarioId": "",
		"conquistaId": ""
	}
	```
- [/tutor](http://localhost:8080/v1/tutor) Lista os tutores (GET), ou cria Tutor (POST)
	```json
	{
		"usuarioId": ""
	}
	```
- [/sessoes](http://localhost:8080/v1/sessoes) Lista as sessoes dos tutores (GET), ou cria Sessão para o tutor
	```json
	{
		"horaInicio": "HH:mm",
		"horaFim": "HH:mm",
		"dia": "SEG",
		"tutorId": ""
	}
	```
- [/solicitacao](http://localhost:8080/v1/solicitacao) Lista solicitacoes dos usuarios (GET), ou cria uma nova solicitação para a Sessão (POST)
	```json
	{
		"sessaoId": ""
	}
	```
<!-- - [](http://localhost:8080/v1/) -->
