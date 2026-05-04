-- ---------------------- -- ---------------------- --
--              SCRIPT DE CRIAÇÃO (DDL)             --
-- Data de criacao...: 30/09/2025                   --
-- Autores...........: Lucas Spinosa dos Santos     --
--                     Rodrigo Carvalho dos Santos  --
--                                                  --
-- Banco de Dados....: MySQL                        --
-- Base de Dados.....: tutoriadb;                   --
--                                                  --
-- PROJETO => 01 Base de Dados                      --
--            11 ENTIDADES                          --
--            02 relacionamentos                    --
--                                                  --
-- ---------------------- -- ---------------------- --

CREATE DATABASE IF NOT EXISTS tutoriadb;
USE tutoriadb;

-- ENTIDADES

CREATE TABLE IF NOT EXISTS
USUARIO (
    usuarioId   INT          NOT NULL AUTO_INCREMENT,
    pontuacao   INT UNSIGNED NOT NULL DEFAULT 0,
    email       VARCHAR(256) NOT NULL,
    senha       VARCHAR(256) NOT NULL,
    nomePerfil  VARCHAR(100) NOT NULL,
    cidade      VARCHAR(80)  NOT NULL,
    estado      CHAR(2)      NOT NULL,
    nascimento  DATE         NOT NULL,

    -- Campos obrigatórios para o Django
    is_active       TINYINT(1)  DEFAULT 1,
    is_staff        TINYINT(1)  DEFAULT 0,
    is_superuser    TINYINT(1)  DEFAULT 0,
    date_joined     DATETIME    DEFAULT CURRENT_TIMESTAMP,
    last_login      DATETIME,

    CONSTRAINT USUARIO_PK
        PRIMARY KEY (usuarioId),

    CONSTRAINT USUARIO_UK
        UNIQUE KEY (email)
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
CONQUISTA (
    conquistaId INT          NOT NULL AUTO_INCREMENT,
    pontos      INT          NOT NULL,
    titulo      VARCHAR(32)  NOT NULL,
    descricao   VARCHAR(64),
    urlImagem   VARCHAR(256) NOT NULL,

    CONSTRAINT CONQUISTA_PK
        PRIMARY KEY (conquistaId),

    CONSTRAINT CONQUISTA_UK
        UNIQUE KEY (titulo)
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
AVALIACAO_APRENDIZ (
    usuarioId  INT    NOT NULL,
    nota       INT(1) NOT NULL,
    comentario VARCHAR(200),

    CONSTRAINT AVALIACAO_APRENDIZ_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
TUTOR (
    tutorId     INT          NOT NULL AUTO_INCREMENT,
    usuarioId   INT          NOT NULL,

    CONSTRAINT TUTOR_PK
        PRIMARY KEY (tutorId),

    CONSTRAINT TUTOR_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
AVALIACAO_TUTOR (
    tutorId    INT    NOT NULL,
    nota       INT(1) NOT NULL,
    comentario VARCHAR(200),

    CONSTRAINT AVALIACAO_TUTOR_USUARIO_FK
        FOREIGN KEY (tutorId)
        REFERENCES TUTOR (tutorId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
AREA (
    areaId   INT         NOT NULL AUTO_INCREMENT,
    nomeArea VARCHAR(60) NOT NULL,

    CONSTRAINT AREA_PK
        PRIMARY KEY (areaId),

    CONSTRAINT AREA_UK
        UNIQUE KEY (nomeArea)
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
ESPECIALIDADE (
    especialidadeId   INT          NOT NULL AUTO_INCREMENT,
    areaId            INT          NOT NULL,
    nomeEspecialidade VARCHAR(100) NOT NULL,

    CONSTRAINT ESPECIALIDADE_PK
        PRIMARY KEY (especialidadeId),

    CONSTRAINT ESPECIALIDADE_UK
        UNIQUE KEY (areaId, nomeEspecialidade),

    CONSTRAINT ESPECIALIDADE_AREA_FK
        FOREIGN KEY (areaId)
        REFERENCES AREA (areaId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
AGENDA (
    agendaId      INT  NOT NULL AUTO_INCREMENT,
    tutorId       INT  NOT NULL,
    horarioInicio TIME NOT NULL,
    horarioFim    TIME NOT NULL,
    dia           ENUM('SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM')  NOT NULL,

    CONSTRAINT AGENDA_PK
        PRIMARY KEY (agendaId),

    CONSTRAINT AGENDA_TUTOR_FK
        FOREIGN KEY (tutorId)
        REFERENCES TUTOR (tutorId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT AGENDA_UK
        UNIQUE KEY (tutorId, dia, horarioInicio)
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
SOLICITACAO (
    solicitacaoId   INT NOT NULL AUTO_INCREMENT,
    usuarioId       INT NOT NULL,
    agendaId        INT NOT NULL,
    areaId          INT NOT NULL,
    especialidadeId INT,
    dataCriacao     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dataPretendida  DATE NOT NULL,
    validade        TIME NOT NULL,
    recorrente      BOOLEAN NOT NULL,
    estado          ENUM('ACEITO', 'PENDENTE', 'RECUSADO', 'RECORRENTE') NOT NULL DEFAULT 'PENDENTE',

    CONSTRAINT SOLICITACAO_PK
        PRIMARY KEY (solicitacaoId),

    CONSTRAINT SOLICITACAO_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT SOLICITACAO_AGENDA_FK
        FOREIGN KEY (agendaId)
        REFERENCES AGENDA (agendaId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT SOLICITACAO_ESPECIALIDADE_FK
        FOREIGN KEY (especialidadeId)
        REFERENCES ESPECIALIDADE (especialidadeId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
SESSAO (
    sessaoId        INT NOT NULL AUTO_INCREMENT,
    usuarioId       INT NOT NULL,
    tutorId         INT NOT NULL,
    areaId          INT NOT NULL,
    especialidadeId INT,

    dataSessao    DATE NOT NULL,
    horarioInicio TIME NOT NULL,
    horarioFim    TIME NOT NULL,

    CONSTRAINT SESSAO_PK
        PRIMARY KEY (sessaoId),

    CONSTRAINT SESSAO_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT SESSAO_TUTOR_FK
        FOREIGN KEY (tutorId)
        REFERENCES TUTOR (tutorId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT SESSAO_AREA_FK
        FOREIGN KEY (areaId)
        REFERENCES AREA (areaId)
        ON DELETE CASCADE
        ON UPDATE CASCADE

    CONSTRAINT SESSAO_ESPECIALIDADE_FK
        FOREIGN KEY (especialidadeId)
        REFERENCES ESPECIALIDADE (especialidadeId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
CHAT (
    chatId    INT NOT NULL AUTO_INCREMENT,
    tutorId   INT NOT NULL,
    usuarioId INT NOT NULL,

    CONSTRAINT CHAT_PK
        PRIMARY KEY (chatId),

    CONSTRAINT CHAT_UK
        UNIQUE KEY (tutorId, usuarioId),

    CONSTRAINT CHAT_TUTOR_FK
        FOREIGN KEY (tutorId)
        REFERENCES TUTOR (tutorId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT CHAT_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
MENSAGEM (
    mensagemId INT          NOT NULL AUTO_INCREMENT,
    chatId     INT          NOT NULL,
    conteudo   VARCHAR(200) NOT NULL,
    horario    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT MENSAGEM_PK
        PRIMARY KEY (mensagemId),

    CONSTRAINT MENSAGEM
        FOREIGN KEY (chatId)
        REFERENCES CHAT (chatId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

-- Tabela de relacionamentos

CREATE TABLE IF NOT EXISTS
consegue (
    consegueId  INT      NOT NULL AUTO_INCREMENT,
    usuarioId   INT      NOT NULL,
    conquistaId INT      NOT NULL,
    dataObtido  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT consegue_PK
        PRIMARY KEY (consegueId),

    CONSTRAINT consegue_UK
        UNIQUE KEY (usuarioId, conquistaId),

    CONSTRAINT consegue_USUARIO_FK
        FOREIGN KEY (usuarioId)
        REFERENCES USUARIO (usuarioId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT consegue_CONQUISTA_FK
        FOREIGN KEY (conquistaId)
        REFERENCES CONQUISTA (conquistaId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS
contem (
    contemId        INT NOT NULL AUTO_INCREMENT,
    especialidadeId INT NOT NULL,
    tutorId         INT NOT NULL,

    CONSTRAINT contem_PK
        PRIMARY KEY (contemId),

    CONSTRAINT contem_UK
        UNIQUE KEY (especialidadeId, tutorId),

    CONSTRAINT contem_ESPECIALIDADE_FK
        FOREIGN KEY (especialidadeId)
        REFERENCES ESPECIALIDADE (especialidadeId)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT contem_TUTOR_FK
        FOREIGN KEY (tutorId)
        REFERENCES TUTOR (tutorId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB, AUTO_INCREMENT=1;
