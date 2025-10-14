-- ---------------------- -- ---------------------- --
--             SCRIPT DE POPULAÇÃO (DML)            --
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

USE tutoriadb;

INSERT INTO USUARIO (email, senha, nomePerfil, cidade, estado, urlFoto) VALUES
('joao.silva@gmail.com', 'senha123', 'João Silva', 'São Paulo', 'SP', 'https://picsum.photos/100?1'),
('maria.oliveira@gmail.com', 'senha456', 'Maria Oliveira', 'Rio de Janeiro', 'RJ', 'https://picsum.photos/100?2'),
('carlos.souza@gmail.com', 'senha789', 'Carlos Souza', 'Belo Horizonte', 'MG', 'https://picsum.photos/100?3'),
('ana.lima@gmail.com', 'senhaabc', 'Ana Lima', 'Curitiba', 'PR', 'https://picsum.photos/100?4'),
('paula.mendes@gmail.com', 'senha321', 'Paula Mendes', 'Salvador', 'BA', 'https://picsum.photos/100?5');

INSERT INTO CONQUISTA (pontos, titulo, descricao, urlImagem) VALUES
(100, 'Iniciante', 'Primeira conquista alcançada', 'https://picsum.photos/100?6'),
(250, 'Aprendiz', 'Completou 5 aulas', 'https://picsum.photos/100?7'),
(500, 'Tutor Experiente', 'Completou 20 aulas', 'https://picsum.photos/100?8'),
(1000, 'Mestre', 'Conquistou 1000 pontos', 'https://picsum.photos/100?9'),
(1500, 'Lenda', 'Conquistou mais de 1500 pontos', 'https://picsum.photos/100?10');

INSERT INTO AREA (nomeArea) VALUES
('Matemática'),
('Programação'),
('Design Gráfico'),
('Idiomas'),
('Ciências Exatas');

INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(1, 1, 'Cálculo Diferencial'),
(2, 2, 'Desenvolvimento Web'),
(3, 3, 'Photoshop Avançado'),
(4, 4, 'Inglês Intermediário'),
(5, 5, 'Física Quântica');

INSERT INTO TUTOR (usuarioId) VALUES (1), (2), (3), (4), (5);

INSERT INTO AVALIACAO_APRENDIZ (usuarioId, nota, comentario) VALUES
(1, 5, 'Excelente aluno!'),
(2, 4, 'Bom desempenho.'),
(3, 3, 'Precisa de mais dedicação.'),
(4, 5, 'Muito participativo!'),
(5, 4, 'Aprende rápido.');

INSERT INTO AVALIACAO_TUTOR (tutorId, nota, comentario) VALUES
(1, 5, 'Ótimo tutor, explica muito bem.'),
(2, 4, 'Didática boa e paciente.'),
(3, 3, 'Pode melhorar a explicação.'),
(4, 5, 'Excelente metodologia.'),
(5, 4, 'Muito atencioso.');

INSERT INTO SESSAO (tutorId, horarioInicio, horarioFim, dia) VALUES
(1, '08:00:00', '10:00:00', 'SEG'),
(1, '14:00:00', '16:00:00', 'QUA'),
(2, '10:00:00', '12:00:00', 'TER'),
(3, '09:00:00', '11:00:00', 'QUI'),
(4, '15:00:00', '17:00:00', 'SEX');

INSERT INTO SOLICITACAO (usuarioId, sessaoId, dataCriacao, validade, estado) VALUES
(2, 1, '08:30:00', '10:00:00', 'ACEITO'),
(3, 2, '13:00:00', '15:00:00', 'PENDENTE'),
(4, 3, '09:00:00', '12:00:00', 'ACEITO'),
(5, 4, '08:45:00', '11:00:00', 'RECUSADO'),
(1, 5, '15:30:00', '17:00:00', 'RECORRENTE');

INSERT INTO CHAT (tutorId, usuarioId) VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 1);

INSERT INTO MENSAGEM (chatId, conteudo) VALUES
(1, 'Olá, gostaria de tirar dúvidas sobre Cálculo.'),
(2, 'Poderia revisar o conteúdo de HTML?'),
(3, 'Como ajustar camadas no Photoshop?'),
(4, 'Pode corrigir meu texto em inglês?'),
(5, 'Fiquei com dúvidas na aula de Física.');

INSERT INTO consegue (usuarioId, conquistaId) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO contem (especialidadeId, tutorId) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
