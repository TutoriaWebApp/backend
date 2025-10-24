-- -- ---------------------- -- ---------------------- --
-- --             SCRIPT DE EXCLUSÃO (DDL)             --
-- -- Data de criacao...: 30/09/2025                   --
-- -- Autores...........: Lucas Spinosa dos Santos     --
-- --                     Rodrigo Carvalho dos Santos  --
-- --                                                  --
-- -- Banco de Dados....: MySQL                        --
-- -- Base de Dados.....: tutoriadb;                   --
-- --                                                  --
-- -- PROJETO => 01 Base de Dados                      --
-- --            11 ENTIDADES                          --
-- --            02 relacionamentos                    --
-- --                                                  --
-- -- ---------------------- -- ---------------------- --
USE tutoriadb;

-- Tabelas geradas pela ORM do Django

DROP TABLE IF EXISTS USUARIO_groups;
DROP TABLE IF EXISTS USUARIO_user_permissions;
DROP TABLE IF EXISTS auth_group_permissions;
DROP TABLE IF EXISTS auth_permission;
DROP TABLE IF EXISTS auth_group;
DROP TABLE IF EXISTS django_admin_log;
DROP TABLE IF EXISTS django_content_type;
DROP TABLE IF EXISTS django_migrations;
DROP TABLE IF EXISTS django_session;

DROP TABLE IF EXISTS contem;
DROP TABLE IF EXISTS consegue;

DROP TABLE IF EXISTS MENSAGEM;
DROP TABLE IF EXISTS CHAT;
DROP TABLE IF EXISTS SOLICITACAO;
DROP TABLE IF EXISTS SESSAO;
DROP TABLE IF EXISTS ESPECIALIDADE;
DROP TABLE IF EXISTS AREA;
DROP TABLE IF EXISTS AVALIACAO_TUTOR;
DROP TABLE IF EXISTS TUTOR;
DROP TABLE IF EXISTS AVALIACAO_APRENDIZ;
DROP TABLE IF EXISTS CONQUISTA;
DROP TABLE IF EXISTS USUARIO;
