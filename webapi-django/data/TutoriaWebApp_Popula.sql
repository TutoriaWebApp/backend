-- -- ---------------------- -- ---------------------- --
-- --             SCRIPT DE POPULAÇÃO (DML)            --
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

-- USUARIOS (Total: 30)
INSERT INTO USUARIO (email, senha, nomePerfil, cidade, estado, aniversario, is_active, is_staff, is_superuser) VALUES
('admin@tutoria.com', 'pbkdf2_sha256$1000000$zZBLgMtlMlfKvomGWZKEKt$ifR7/CLjG7xZUl6+iFjJ0W3mXON2p3smJGnn2XuBUSY=', 'Admin', 'Não Aplicado', 'NA', '1971-03-15', 1, 1, 1);

INSERT INTO USUARIO (email, senha, nomePerfil, cidade, estado, aniversario) VALUES
('ana.lima@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Ana Lima', 'Curitiba', 'PR', '1985-03-05'),
('joao.silva@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'João Silva', 'São Paulo', 'SP', '1990-01-03'),
('maria.oliveira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Maria Oliveira', 'Rio de Janeiro', 'RJ', '1979-03-05'),
('carlos.souza@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Carlos Souza', 'Belo Horizonte', 'MG', '1988-02-18'),
('paula.mendes@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Paula Mendes', 'Salvador', 'BA', '1988-01-05'),
('fernanda.rocha@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Fernanda Rocha', 'Porto Alegre', 'RS', '1992-07-12'),
('ricardo.alves@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Ricardo Alves', 'Fortaleza', 'CE', '1983-11-25'),
('gabriela.costa@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Gabriela Costa', 'Brasília', 'DF', '1995-05-30'),
('bruno.ferreira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Bruno Ferreira', 'Manaus', 'AM', '1987-09-14'),
('juliana.pereira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Juliana Pereira', 'Recife', 'PE', '1991-12-08'),
('lucas.martins@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Lucas Martins', 'Florianópolis', 'SC', '1989-04-22'),
('amanda.santos@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Amanda Santos', 'Vitória', 'ES', '1994-10-05'),
('tiago.gomes@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Tiago Gomes', 'Goiânia', 'GO', '1986-01-19'),
('patricia.lima@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Patricia Lima', 'Belém', 'PA', '1984-06-27'),
('rafael.silva@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Rafael Silva', 'São Luís', 'MA', '1993-08-03'),
('larissa.souza@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Larissa Souza', 'Natal', 'RN', '1996-02-15'),
('andre.oliveira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Andre Oliveira', 'Teresina', 'PI', '1982-12-20'),
('camila.mendes@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Camila Mendes', 'João Pessoa', 'PB', '1990-05-10'),
('felipe.alves@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Felipe Alves', 'Maceió', 'AL', '1985-09-02'),
('beatriz.costa@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Beatriz Costa', 'Aracaju', 'SE', '1994-03-25'),
('rodrigo.ferreira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Rodrigo Ferreira', 'Campo Grande', 'MS', '1988-07-08'),
('vanessa.pereira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Vanessa Pereira', 'Cuiabá', 'MT', '1991-11-14'),
('marcelo.martins@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Marcelo Martins', 'Porto Velho', 'RO', '1987-04-30'),
('elaine.santos@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Elaine Santos', 'Rio Branco', 'AC', '1984-10-18'),
('igor.gomes@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Igor Gomes', 'Boa Vista', 'RR', '1993-01-22'),
('leticia.lima@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Leticia Lima', 'São Paulo', 'SP', '1995-06-05'),
('danilo.silva@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Danilo Silva', 'Rio de Janeiro', 'RJ', '1989-08-28'),
('monica.souza@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Monica Souza', 'Belo Horizonte', 'MG', '1992-02-14'),
('eduardo.oliveira@gmail.com', 'pbkdf2_sha256$1000000$l8XBm8Z49Qkms3QVmkQYP1$2wYS/+kyD9G259Si3zvA/T8JzdevHAWZG9pD/sMjkpc=', 'Eduardo Oliveira', 'Salvador', 'BA', '1986-11-09');

-- CONQUISTAS (Total: 25)
INSERT INTO CONQUISTA (pontos, titulo, descricao, urlImagem) VALUES
(100, 'A primeira de muitas!', 'Realize sua primeira sessão de tutoria!', 'https://picsum.photos/100?6'),
(250, 'Aprendiz', 'Completou 5 aulas', 'https://picsum.photos/100?7'),
(500, 'Tutor Experiente', 'Completou 20 aulas', 'https://picsum.photos/100?8'),
(1000, 'Mestre', 'Conquistou 1000 pontos', 'https://picsum.photos/100?9'),
(1500, 'Lenda', 'Conquistou mais de 1500 pontos', 'https://picsum.photos/100?10'),
(200, 'Explorador', 'Visitou 5 áreas diferentes', 'https://picsum.photos/100?11'),
(300, 'Pontual', 'Chegou no horário em 10 sessões', 'https://picsum.photos/100?12'),
(400, 'Comunicador', 'Enviou 100 mensagens no chat', 'https://picsum.photos/100?13'),
(600, 'Ajudante', 'Avaliou 10 tutores', 'https://picsum.photos/100?14'),
(800, 'Dedicado', 'Estudou por 50 horas no total', 'https://picsum.photos/100?15'),
(50, 'Bem-vindo', 'Completou o perfil', 'https://picsum.photos/100?16'),
(150, 'Curioso', 'Fez 3 perguntas em uma sessão', 'https://picsum.photos/100?17'),
(350, 'Notívago', 'Teve uma sessão após as 20h', 'https://picsum.photos/100?18'),
(450, 'Madrugador', 'Teve uma sessão antes das 9h', 'https://picsum.photos/100?19'),
(700, 'Especialista', 'Dominou uma especialidade', 'https://picsum.photos/100?20'),
(900, 'Multitarefa', 'Inscrito em 3 áreas ao mesmo tempo', 'https://picsum.photos/100?21'),
(1100, 'Mentor', 'Ajudou 5 novos alunos', 'https://picsum.photos/100?22'),
(1200, 'Sábio', 'Acumulou 100 avaliações 5 estrelas', 'https://picsum.photos/100?23'),
(1300, 'Veterano', 'Membro há mais de um ano', 'https://picsum.photos/100?24'),
(1400, 'Influenciador', 'Indicou 3 amigos', 'https://picsum.photos/100?25'),
(100, 'Social', 'Participou de um chat em grupo', 'https://picsum.photos/100?26'),
(200, 'Crítico', 'Escreveu um comentário detalhado', 'https://picsum.photos/100?27'),
(300, 'Fiel', 'Teve 5 sessões com o mesmo tutor', 'https://picsum.photos/100?28'),
(400, 'Viajante', 'Teve sessões com tutores de 3 estados', 'https://picsum.photos/100?29'),
(500, 'Gênio', 'Resolveu um problema complexo', 'https://picsum.photos/100?30');

-- AREAS (Total: 25)
INSERT INTO AREA (nomeArea) VALUES
('Matemática'), ('Programação'), ('Design Gráfico'), ('Idiomas'), ('Ciências Exatas'),
('História'), ('Geografia'), ('Biologia'), ('Química'), ('Física'),
('Filosofia'), ('Sociologia'), ('Artes'), ('Música'), ('Educação Física'),
('Economia'), ('Direito'), ('Medicina'), ('Psicologia'), ('Arquitetura'),
('Marketing'), ('Gastronomia'), ('Moda'), ('Fotografia'), ('Cinema');

-- ESPECIALIDADES (Total: 25)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(1, 1, 'Cálculo Diferencial'), (2, 2, 'Desenvolvimento Web'), (3, 3, 'Photoshop Avançado'),
(4, 4, 'Inglês Intermediário'), (5, 5, 'Física Quântica'), (6, 6, 'Brasil Colônia'),
(7, 7, 'Geopolítica Moderna'), (8, 8, 'Genética Molecular'), (9, 9, 'Termodinâmica Química'),
(10, 10, 'Mecânica Clássica'), (11, 11, 'Existencialismo'), (12, 12, 'Teoria Crítica'),
(13, 13, 'Pintura a Óleo'), (14, 14, 'Teoria Musical'), (15, 15, 'Fisiologia do Exercício'),
(16, 16, 'Microeconomia'), (17, 17, 'Direito Civil'), (18, 18, 'Anatomia Humana'),
(19, 19, 'Psicologia Cognitiva'), (20, 20, 'Urbanismo Sustentável'), (21, 21, 'Marketing Digital'),
(22, 22, 'Culinária Italiana'), (23, 23, 'Corte e Costura'), (24, 24, 'Iluminação de Estúdio'),
(25, 25, 'Roteiro Cinematográfico');

-- TUTORES (Total: 25)
INSERT INTO TUTOR (usuarioId) VALUES
(1), (2), (3), (4), (5), (6), (7), (8), (9), (10),
(11), (12), (13), (14), (15), (16), (17), (18), (19), (20),
(21), (22), (23), (24), (25);

-- CONTEM (Relacionamento Tutor-Especialidade, Total: 25)
INSERT INTO contem (tutorId, especialidadeId) VALUES
(1, 1), (1, 2), (2, 2),
(3, 3), (3, 2),
(4, 4), (4, 2),
(5, 5), (5, 2),
(6, 6), (6, 2),
(7, 7), (7, 2),
(8, 8), (8, 2),
(9, 9), (9, 2),
(10, 10), (10, 2),
(11, 11), (11, 2),
(12, 12), (12, 2),
(13, 13), (13, 2),
(14, 14), (14, 2),
(15, 15), (15, 2),
(16, 16), (16, 2),
(17, 17), (17, 2),
(18, 18), (18, 2),
(19, 19), (19, 2),
(20, 20), (20, 2),
(21, 21), (21, 2),
(22, 22), (22, 2),
(23, 23), (23, 2),
(24, 24), (24, 2),
(25, 25), (25, 2);

-- AGENDAS (Total: 25)
INSERT INTO AGENDA (tutorId, horarioInicio, horarioFim, dia) VALUES
(1, '08:00:00', '10:00:00', 'SEG'), (1, '14:00:00', '16:00:00', 'QUA'),
(2, '10:00:00', '12:00:00', 'TER'), (3, '09:00:00', '11:00:00', 'QUI'),
(4, '15:00:00', '17:00:00', 'SEX'), (5, '08:00:00', '10:00:00', 'SAB'),
(6, '13:00:00', '15:00:00', 'SEG'), (7, '16:00:00', '18:00:00', 'TER'),
(8, '09:00:00', '11:00:00', 'QUA'), (9, '14:00:00', '16:00:00', 'QUI'),
(10, '10:00:00', '12:00:00', 'SEX'), (11, '08:00:00', '10:00:00', 'DOM'),
(12, '14:00:00', '16:00:00', 'SEG'), (13, '10:00:00', '12:00:00', 'TER'),
(14, '09:00:00', '11:00:00', 'QUA'), (15, '15:00:00', '17:00:00', 'QUI'),
(16, '16:00:00', '18:00:00', 'SEX'), (17, '08:00:00', '10:00:00', 'SAB'),
(18, '13:00:00', '15:00:00', 'SEG'), (19, '10:00:00', '12:00:00', 'TER'),
(20, '14:00:00', '16:00:00', 'QUA'), (21, '09:00:00', '11:00:00', 'QUI'),
(22, '15:00:00', '17:00:00', 'SEX'), (23, '10:00:00', '12:00:00', 'SAB'),
(24, '08:00:00', '10:00:00', 'DOM'), (25, '14:00:00', '16:00:00', 'SEG');

-- SOLICITACOES (Total: 25)
INSERT INTO SOLICITACAO (usuarioId, agendaId, areaId, especialidadeId, dataPretendida, validade, recorrente, estado) VALUES
(26, 1, 1, 1, '2026-06-01', '23:59:59', FALSE, 'ACEITO'),
(27, 2, 1, 1, '2026-06-03', '23:59:59', FALSE, 'PENDENTE'),
(28, 3, 2, 2, '2026-06-02', '23:59:59', TRUE, 'RECORRENTE'),
(29, 4, 3, 3, '2026-06-04', '23:59:59', FALSE, 'ACEITO'),
(30, 5, 4, 4, '2026-06-05', '23:59:59', FALSE, 'RECUSADO'),
(26, 6, 5, 5, '2026-06-06', '23:59:59', FALSE, 'PENDENTE'),
(27, 7, 6, 6, '2026-06-08', '23:59:59', FALSE, 'ACEITO'),
(28, 8, 7, 7, '2026-06-09', '23:59:59', FALSE, 'PENDENTE'),
(29, 9, 8, 8, '2026-06-10', '23:59:59', FALSE, 'ACEITO'),
(30, 10, 9, 9, '2026-06-11', '23:59:59', FALSE, 'PENDENTE'),
(26, 11, 10, 10, '2026-06-14', '23:59:59', FALSE, 'ACEITO'),
(27, 12, 11, 11, '2026-06-15', '23:59:59', FALSE, 'PENDENTE'),
(28, 13, 12, 12, '2026-06-16', '23:59:59', FALSE, 'ACEITO'),
(29, 14, 13, 13, '2026-06-17', '23:59:59', FALSE, 'PENDENTE'),
(30, 15, 14, 14, '2026-06-18', '23:59:59', FALSE, 'ACEITO'),
(26, 16, 15, 15, '2026-06-19', '23:59:59', FALSE, 'PENDENTE'),
(27, 17, 16, 16, '2026-06-20', '23:59:59', FALSE, 'ACEITO'),
(28, 18, 17, 17, '2026-06-22', '23:59:59', FALSE, 'PENDENTE'),
(29, 19, 18, 18, '2026-06-23', '23:59:59', FALSE, 'ACEITO'),
(30, 20, 19, 19, '2026-06-24', '23:59:59', FALSE, 'PENDENTE'),
(26, 21, 20, 20, '2026-06-25', '23:59:59', FALSE, 'ACEITO'),
(27, 22, 21, 21, '2026-06-26', '23:59:59', FALSE, 'PENDENTE'),
(28, 23, 22, 22, '2026-06-27', '23:59:59', FALSE, 'ACEITO'),
(29, 24, 23, 23, '2026-06-28', '23:59:59', FALSE, 'PENDENTE'),
(30, 25, 24, 24, '2026-06-29', '23:59:59', FALSE, 'ACEITO');

-- SESSOES (Total: 25)
INSERT INTO SESSAO (usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(26,  1, 1, 1, '2026-05-19', '08:00:00', '10:00:00'),
(27,  2, 2, 2, '2026-05-20', '10:00:00', '12:00:00'),
(28,  3, 3, 3, '2026-05-21', '09:00:00', '11:00:00'),
(29,  4, 4, 4, '2026-05-22', '15:00:00', '17:00:00'),
(30,  5, 5, 5, '2026-05-23', '08:00:00', '10:00:00'),
(26,  6, 6, 6, '2026-05-25', '13:00:00', '15:00:00'),
(27,  7, 7, 7, '2026-05-26', '16:00:00', '18:00:00'),
(28,  8, 8, 8, '2026-05-27', '09:00:00', '11:00:00'),
(29,  9, 9, 9, '2026-05-28', '14:00:00', '16:00:00'),
(30, 10, 10, 10, '2026-05-29', '10:00:00', '12:00:00'),
(26, 11, 11, 11, '2026-05-31', '08:00:00', '10:00:00'),
(27, 12, 12, 12, '2026-06-01', '14:00:00', '16:00:00'),
(28, 13, 13, 13, '2026-06-02', '10:00:00', '12:00:00'),
(29, 14, 14, 14, '2026-06-03', '09:00:00', '11:00:00'),
(30, 15, 15, 15, '2026-06-04', '15:00:00', '17:00:00'),
(26, 16, 16, 16, '2026-06-05', '16:00:00', '18:00:00'),
(27, 17, 17, 17, '2026-06-06', '08:00:00', '10:00:00'),
(28, 18, 18, 18, '2026-06-08', '13:00:00', '15:00:00'),
(29, 19, 19, 19, '2026-06-09', '10:00:00', '12:00:00'),
(30, 20, 20, 20, '2026-06-10', '14:00:00', '16:00:00'),
(26, 21, 21, 21, '2026-06-11', '09:00:00', '11:00:00'),
(27, 22, 22, 22, '2026-06-12', '15:00:00', '17:00:00'),
(28, 23, 23, 23, '2026-06-13', '10:00:00', '12:00:00'),
(29, 24, 24, 24, '2026-06-14', '08:00:00', '10:00:00'),
(30, 25, 25, 25, '2026-06-15', '14:00:00', '16:00:00');

-- AVALIACOES_APRENDIZ (Total: 25)
INSERT INTO AVALIACAO_APRENDIZ (usuarioId, sessaoId, nota, comentario) VALUES
(26,  1, 5, 'Aluno muito dedicado e interessado.'),
(27,  2, 4, 'Demonstrou facilidade com programação.'),
(28,  3, 2, 'Boa criatividade, precisa focar em detalhes.'),
(29,  4, 4, 'Pronúncia excelente.'),
(30,  5, 3, 'Dedicado, mas precisa revisar conceitos básicos.'),
(26,  6, 4, 'Interessado em detalhes históricos.'),
(27,  7, 3, 'Boa compreensão geopolítica.'),
(28,  8, 3, 'Interessado, mas faltou base em biologia.'),
(29,  9, 4, 'Ótima evolução na química.'),
(30, 10, 3, 'Física dominada com sucesso.'),
(26, 11, 3, 'Reflexivo e participativo.'),
(27, 12, 3, 'Boa análise social.'),
(28, 13, 3, 'Habilidade artística notável.'),
(29, 14, 3, 'Ritmo bom, precisa praticar mais.'),
(30, 15, 5, 'Atleta dedicado aos estudos.'),
(26, 16, 5, 'Visão econômica apurada.'),
(27, 17, 5, 'Raciocínio jurídico rápido.'),
(28, 18, 4, 'Esforçado na memorização de termos.'),
(29, 19, 5, 'Interesse genuíno em comportamento.'),
(30, 20, 5, 'Projetos inovadores.'),
(26, 21, 5, 'Visão de mercado excelente.'),
(27, 22, 5, 'Mão cheia na cozinha.'),
(28, 23, 4, 'Bom acabamento nas peças.'),
(29, 24, 5, 'Olhar fotográfico apurado.'),
(30, 25, 5, 'Roteiros com bom ritmo.');

-- AVALIACOES_TUTOR (Total: 25)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(1,   1, 5, 'Excelente tutor, explicou tudo perfeitamente.'),
(2,   2, 4, 'Muito bom, mas o horário foi um pouco apertado.'),
(3,   3, 5, 'Aula incrível, aprendi muito sobre design.'),
(4,   4, 5, 'O melhor tutor de idiomas que já tive.'),
(5,   5, 4, 'Boa didática, recomendo.'),
(6,   6, 5, 'Aula de história muito envolvente.'),
(7,   7, 3, 'Poderia ser mais paciente com as dúvidas.'),
(8,   8, 5, 'Genética explicada de forma simples.'),
(9,   9, 4, 'Bom conhecimento técnico.'),
(10, 10, 5, 'Mecânica clássica nunca foi tão fácil.'),
(11, 11, 4, 'Gostei muito da abordagem filosófica.'),
(12, 12, 5, 'Excelente visão sociológica.'),
(13, 13, 5, 'Pintura a óleo técnica muito boa.'),
(14, 14, 4, 'Teoria musical bem explicada.'),
(15, 15, 5, 'Fisiologia aplicada de forma prática.'),
(16, 16, 3, 'Achei a aula um pouco cansativa.'),
(17, 17, 5, 'Direito civil de forma clara.'),
(18, 18, 5, 'Anatomia humana fascinante.'),
(19, 19, 4, 'Psicologia cognitiva bem estruturada.'),
(20, 20, 5, 'Urbanismo sustentável muito atual.'),
(21, 21, 5, 'Marketing digital na prática.'),
(22, 22, 5, 'Culinária italiana deliciosa.'),
(23, 23, 4, 'Corte e costura técnica precisa.'),
(24, 24, 5, 'Iluminação de estúdio profissional.'),
(25, 25, 5, 'Roteiro cinematográfico criativo.');

-- CHATS (Total: 25)
INSERT INTO CHAT (tutorId, usuarioId) VALUES
(1, 26), (2, 27), (3, 28), (4, 29), (5, 30),
(6, 26), (7, 27), (8, 28), (9, 29), (10, 30),
(11, 26), (12, 27), (13, 28), (14, 29), (15, 30),
(16, 26), (17, 27), (18, 28), (19, 29), (20, 30),
(21, 26), (22, 27), (23, 28), (24, 29), (25, 30);

-- MENSAGENS (Total: 25)
INSERT INTO MENSAGEM (chatId, conteudo) VALUES
(1, 'Olá, gostaria de tirar dúvidas sobre Cálculo.'),
(2, 'Poderia revisar o conteúdo de HTML?'),
(3, 'Como ajustar camadas no Photoshop?'),
(4, 'Pode corrigir meu texto em inglês?'),
(5, 'Fiquei com dúvidas na aula de Física.'),
(6, 'Pode me enviar o material de história?'),
(7, 'Qual o tema da próxima aula de geografia?'),
(8, 'Tenho dúvidas sobre DNA.'),
(9, 'Pode explicar a tabela periódica de novo?'),
(10, 'O que cai na prova de física?'),
(11, 'Qual filósofo vamos estudar hoje?'),
(12, 'Pode me ajudar com o ensaio de sociologia?'),
(13, 'Quais tintas devo comprar?'),
(14, 'Como ler partituras mais rápido?'),
(15, 'Qual o melhor exercício para costas?'),
(16, 'O que é oferta e demanda?'),
(17, 'Como funciona o processo civil?'),
(18, 'Onde fica o fêmur?'),
(19, 'O que é memória de curto prazo?'),
(20, 'Como planejar uma praça?'),
(21, 'Como subir anúncios no Facebook?'),
(22, 'Qual o ponto do risoto?'),
(23, 'Como fazer a barra invisível?'),
(24, 'Qual ISO usar de dia?'),
(25, 'Como criar um plot twist?');

-- CONSEGUE (Relacionamento Usuario-Conquista, Total: 25)
INSERT INTO consegue (usuarioId, conquistaId) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
(21, 21), (22, 22), (23, 23), (24, 24), (25, 25);
