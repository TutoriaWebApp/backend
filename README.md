# Backend do TutoriaWebApp

Este repositório tem como objetivo apresentar o backend do Trabalho de Conclusão de Curso dos alunos Lucas Spinosa e Rodrigo Santos.

## Pré requisitos
- Docker
- Docker Compose
- python3 com pip

## Como executar

### Rodando em contêiner Docker
Crie o seu arquivo `.env` de configuração de ambiente, como o exemplo `env/.env.example`:
Você pode configurar seus token para BREVO SMTP

```sh
cp env/.env.example env/.env
```

Para executar o programa inicie o docker

```
docker-compose --env-file ./env/.env up --build -d
```

## Endpoints
Ao executar este software, os endpoints poderão ser acessados pela documentação exposta em [localhost:8000/v1/docs](http://localhost:8000/v1/docs)
<!-- - [](http://localhost:8000/v1/) -->
