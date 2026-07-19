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
INSERT INTO TUTOR (tutorId, usuarioId, notaAvaliacao) VALUES
(1, 1, 5.0), 
(2, 2, 4.5), 
(3, 3, 4.8), 
(4, 4, 3.5), 
(5, 5, 4.0), 
(6, 6, 2.5), 
(7, 7, 4.2), 
(8, 8, 5.0), 
(9, 9, 3.8), 
(10, 10, 4.7),
(11, 11, 4.1), 
(12, 12, 1.5), -- Nota bem baixa para testar o 'asc'
(13, 13, 3.9), 
(14, 14, 4.9), 
(15, 15, 4.3), 
(16, 16, 2.0), 
(17, 17, 4.6), 
(18, 18, 3.7), 
(19, 19, 4.4), 
(20, 20, 5.0),
(21, 21, 3.2), 
(22, 22, 4.0), 
(23, 23, 2.8), 
(24, 24, 4.9), 
(25, 25, 3.0);

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
(26, 1, 1, 1, '2026-06-01', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(27, 2, 1, 1, '2026-06-03', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(28, 3, 2, 2, '2026-06-02', '2026-10-10 23:59:59', TRUE, 'RECORRENTE'),
(29, 4, 3, 3, '2026-06-04', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(30, 5, 4, 4, '2026-06-05', '2026-10-10 23:59:59', FALSE, 'RECUSADO'),
(26, 6, 5, 5, '2026-06-06', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(27, 7, 6, 6, '2026-06-08', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(28, 8, 7, 7, '2026-06-09', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(29, 9, 8, 8, '2026-06-10', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(30, 10, 9, 9, '2026-06-11', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(26, 11, 10, 10, '2026-06-14', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(27, 12, 11, 11, '2026-06-15', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(28, 13, 12, 12, '2026-06-16', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(29, 14, 13, 13, '2026-06-17', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(30, 15, 14, 14, '2026-06-18', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(26, 16, 15, 15, '2026-06-19', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(27, 17, 16, 16, '2026-06-20', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(28, 18, 17, 17, '2026-06-22', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(29, 19, 18, 18, '2026-06-23', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(30, 20, 19, 19, '2026-06-24', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(26, 21, 20, 20, '2026-06-25', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(27, 22, 21, 21, '2026-06-26', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(28, 23, 22, 22, '2026-06-27', '2026-10-10 23:59:59', FALSE, 'ACEITO'),
(29, 24, 23, 23, '2026-06-28', '2026-10-10 23:59:59', FALSE, 'PENDENTE'),
(30, 25, 24, 24, '2026-06-29', '2026-10-10 23:59:59', FALSE, 'ACEITO');

-- =========================================================================
-- SESSOES (IDs sequenciais de 1 a 40)
-- =========================================================================

-- Tutor 1 (Nota 5.0): Fez 4 sessões (IDs: 1, 2, 3, 4)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(1, 26, 1, 1, 1, '2026-05-19', '08:00:00', '10:00:00'),
(2, 27, 1, 1, 1, '2026-05-20', '10:00:00', '12:00:00'),
(3, 28, 1, 1, 1, '2026-05-21', '09:00:00', '11:00:00'),
(4, 29, 1, 1, 1, '2026-05-22', '15:00:00', '17:00:00');

-- Tutor 2 (Nota 4.5): Fez 6 sessões (IDs: 5, 6, 7, 8, 9, 10)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(5,  26, 2, 2, 2, '2026-05-20', '10:00:00', '12:00:00'),
(6,  27, 2, 2, 2, '2026-05-21', '10:00:00', '12:00:00'),
(7,  28, 2, 2, 2, '2026-05-22', '10:00:00', '12:00:00'),
(8,  29, 2, 2, 2, '2026-05-23', '10:00:00', '12:00:00'),
(9,  30, 2, 2, 2, '2026-05-24', '10:00:00', '12:00:00'),
(10, 26, 2, 2, 2, '2026-05-25', '10:00:00', '12:00:00');

-- Tutor 3 (Nota 4.8): Fez 5 sessões (IDs: 11, 12, 13, 14, 15)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(11, 26, 3, 3, 3, '2026-05-19', '09:00:00', '11:00:00'),
(12, 27, 3, 3, 3, '2026-05-20', '09:00:00', '11:00:00'),
(13, 28, 3, 3, 3, '2026-05-21', '09:00:00', '11:00:00'),
(14, 29, 3, 3, 3, '2026-05-22', '09:00:00', '11:00:00'),
(15, 30, 3, 3, 3, '2026-05-23', '09:00:00', '11:00:00');

-- Tutor 4 (Nota 3.5): Fez 3 sessões (IDs: 16, 17, 18)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(16, 26, 4, 4, 4, '2026-05-19', '15:00:00', '17:00:00'),
(17, 27, 4, 4, 4, '2026-05-20', '15:00:00', '17:00:00'),
(18, 28, 4, 4, 4, '2026-05-21', '15:00:00', '17:00:00');

-- Tutor 5 (Nota 4.0): Fez 2 sessões (IDs: 19, 20)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(19, 26, 5, 5, 5, '2026-05-19', '08:00:00', '10:00:00'),
(20, 27, 5, 5, 5, '2026-05-20', '08:00:00', '10:00:00');

-- Tutor 8 (Nota 5.0): Fez 2 sessões (IDs: 21, 22) -> Perfeito para testar desempate com o Tutor 1!
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(21, 26, 8, 8, 8, '2026-05-19', '09:00:00', '11:00:00'),
(22, 27, 8, 8, 8, '2026-05-20', '09:00:00', '11:00:00');

-- Tutor 20 (Nota 5.0): Fez 1 sessão (ID: 23) -> Outro empate de nota máxima!
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(23, 26, 20, 20, 20, '2026-05-19', '14:00:00', '16:00:00');

-- Restante dos tutores (6, 7, 9 ao 19, 21 ao 25): Apenas 1 sessão padrão para não deixar vazio (IDs: 24 a 40)
INSERT INTO SESSAO (sessaoId, usuarioId, tutorId, areaId, especialidadeId, dataSessao, horarioInicio, horarioFim) VALUES
(24, 26, 6, 6, 6, '2026-05-19', '13:00:00', '15:00:00'),
(25, 26, 7, 7, 7, '2026-05-19', '16:00:00', '18:00:00'),
(26, 26, 9, 9, 9, '2026-05-19', '14:00:00', '16:00:00'),
(27, 26, 10, 10, 10, '2026-05-19', '10:00:00', '12:00:00'),
(28, 26, 11, 11, 11, '2026-05-19', '08:00:00', '10:00:00'),
(29, 26, 12, 12, 12, '2026-05-19', '14:00:00', '16:00:00'),
(30, 26, 13, 13, 13, '2026-05-19', '10:00:00', '12:00:00'),
(31, 26, 14, 14, 14, '2026-05-19', '09:00:00', '11:00:00'),
(32, 26, 15, 15, 15, '2026-05-19', '15:00:00', '17:00:00'),
(33, 26, 16, 16, 16, '2026-05-19', '16:00:00', '18:00:00'),
(34, 26, 17, 17, 17, '2026-05-19', '08:00:00', '10:00:00'),
(35, 26, 18, 18, 18, '2026-05-19', '13:00:00', '15:00:00'),
(36, 26, 19, 19, 19, '2026-05-19', '10:00:00', '12:00:00'),
(37, 26, 21, 21, 21, '2026-05-19', '09:00:00', '11:00:00'),
(38, 26, 22, 22, 22, '2026-05-19', '15:00:00', '17:00:00'),
(39, 26, 23, 23, 23, '2026-05-19', '10:00:00', '12:00:00'),
(40, 26, 24, 24, 24, '2026-05-19', '08:00:00', '10:00:00'),
(41, 26, 25, 25, 25, '2026-05-19', '14:00:00', '16:00:00');

-- =========================================================================
-- AVALIACOES_APRENDIZ (Total: 41 - Mapeamento 1:1 exato com as sessões)
-- =========================================================================
INSERT INTO AVALIACAO_APRENDIZ (usuarioId, sessaoId, nota, comentario) VALUES
(26, 1, 5, 'Excelente'), (27, 2, 5, 'Ótimo'), (28, 3, 4, 'Bom'), (29, 4, 5, 'Muito bom'),
(26, 5, 4, 'Ok'), (27, 6, 4, 'Ok'), (28, 7, 4, 'Ok'), (29, 8, 4, 'Ok'), (30, 9, 4, 'Ok'), (26, 10, 4, 'Ok'),
(26, 11, 5, ''), (27, 12, 5, ''), (28, 13, 5, ''), (29, 14, 4, ''), (30, 15, 5, ''),
(26, 16, 3, ''), (27, 17, 3, ''), (28, 18, 4, ''),
(26, 19, 4, ''), (27, 20, 4, ''),
(26, 21, 5, ''), (27, 22, 5, ''),
(26, 23, 5, ''),
(26, 24, 3, ''), (26, 25, 4, ''), (26, 26, 4, ''), (26, 27, 5, ''), (26, 28, 4, ''),
(26, 29, 2, ''), (26, 30, 3, ''), (26, 31, 4, ''), (26, 32, 4, ''), (26, 33, 3, ''),
(26, 34, 5, ''), (26, 35, 4, ''), (26, 36, 4, ''), (26, 37, 3, ''), (26, 38, 4, ''),
(26, 39, 3, ''), (26, 40, 5, ''), (26, 41, 3, '');


-- =========================================================================
-- AVALIACOES_TUTOR (Total: 41 - Uma avaliação real casando com cada Sessão)
-- =========================================================================

-- Avaliações do Tutor 1 (Sessões 1, 2, 3, 4)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(1, 1, 5, 'Excelente didática.'), (1, 2, 5, 'Ótimo.'), (1, 3, 5, 'Muito prestativo.'), (1, 4, 5, 'Perfeito.');

-- Avaliações do Tutor 2 (Sessões 5, 6, 7, 8, 9, 10)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(2, 5, 4, ''), (2, 6, 4, ''), (2, 7, 5, ''), (2, 8, 4, ''), (2, 9, 4, ''), (2, 10, 5, '');

-- Avaliações do Tutor 3 (Sessões 11, 12, 13, 14, 15)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(3, 11, 5, ''), (3, 12, 5, ''), (3, 13, 4, ''), (3, 14, 5, ''), (3, 15, 5, '');

-- Avaliações do Tutor 4 (Sessões 16, 17, 18)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(4, 16, 3, ''), (4, 17, 4, ''), (4, 18, 3, '');

-- Avaliações do Tutor 5 (Sessões 19, 20)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(5, 19, 4, ''), (5, 20, 4, '');

-- Avaliações do Tutor 8 (Sessões 21, 22)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(8, 21, 5, ''), (8, 22, 5, '');

-- Avaliação do Tutor 20 (Sessão 23)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(20, 23, 5, '');

-- Restante dos Tutores (Sessões de 24 a 41)
INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario) VALUES
(6, 24, 3, ''), (7, 25, 4, ''), (9, 26, 4, ''), (10, 27, 5, ''), (11, 28, 4, ''),
(12, 29, 2, ''), (13, 30, 3, ''), (14, 31, 4, ''), (15, 32, 4, ''), (16, 33, 3, ''),
(17, 34, 5, ''), (18, 35, 4, ''), (19, 36, 4, ''), (21, 37, 3, ''), (22, 38, 4, ''),
(23, 39, 3, ''), (24, 40, 5, ''), (25, 41, 3, '');

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
