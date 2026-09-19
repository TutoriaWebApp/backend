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
INSERT INTO USUARIO (email, senha, nomePerfil, cidade, estado, aniversario, localizacao, is_active, is_staff, is_superuser) VALUES
('admin@tutoria.com', 'pbkdf2_sha256$1000000$zZBLgMtlMlfKvomGWZKEKt$ifR7/CLjG7xZUl6+iFjJ0W3mXON2p3smJGnn2XuBUSY=', 'Admin', 'Não Aplicado', 'NA', '1971-03-15', ST_GeomFromText('POINT(0 0)', 4326), 1, 1, 1);

-- Para fins de testes a senha destes usuários será Senha@123456
INSERT INTO USUARIO (email, senha, nomePerfil, cidade, estado, aniversario, localizacao) VALUES
('webapp.tutoria+teste01@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Ana Lima', 'Curitiba', 'PR', '1985-03-05', ST_GeomFromText('POINT(-49.2733 -25.4284)', 4326)),
('webapp.tutoria+teste02@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'João Silva', 'São Paulo', 'SP', '1990-01-03', ST_GeomFromText('POINT(-46.6333 -23.5505)', 4326)),
('webapp.tutoria+teste03@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Maria Oliveira', 'Rio de Janeiro', 'RJ', '1979-03-05', ST_GeomFromText('POINT(-43.1729 -22.9068)', 4326)),
('webapp.tutoria+teste04@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Carlos Souza', 'Belo Horizonte', 'MG', '1988-02-18', ST_GeomFromText('POINT(-43.9345 -19.9167)', 4326)),
('webapp.tutoria+teste05@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Paula Mendes', 'Salvador', 'BA', '1988-01-05', ST_GeomFromText('POINT(-38.5016 -12.9777)', 4326)),
('webapp.tutoria+teste06@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Fernanda Rocha', 'Porto Alegre', 'RS', '1992-07-12', ST_GeomFromText('POINT(-51.2177 -30.0346)', 4326)),
('webapp.tutoria+teste07@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Ricardo Alves', 'Fortaleza', 'CE', '1983-11-25', ST_GeomFromText('POINT(-38.5267 -3.7319)', 4326)),
('webapp.tutoria+teste08@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Gabriela Costa', 'Brasília', 'DF', '1995-05-30', ST_GeomFromText('POINT(-47.8919 -15.7975)', 4326)),
('webapp.tutoria+teste09@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Bruno Ferreira', 'Manaus', 'AM', '1987-09-14', ST_GeomFromText('POINT(-60.0217 -3.1190)', 4326)),
('webapp.tutoria+teste10@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Juliana Pereira', 'Recife', 'PE', '1991-12-08', ST_GeomFromText('POINT(-34.8770 -8.0476)', 4326)),
('webapp.tutoria+teste11@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Lucas Martins', 'Florianópolis', 'SC', '1989-04-22', ST_GeomFromText('POINT(-48.5480 -27.5954)', 4326)),
('webapp.tutoria+teste12@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Amanda Santos', 'Vitória', 'ES', '1994-10-05', ST_GeomFromText('POINT(-40.3128 -20.3155)', 4326)),
('webapp.tutoria+teste13@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Tiago Gomes', 'Goiânia', 'GO', '1986-01-19', ST_GeomFromText('POINT(-49.2648 -16.6869)', 4326)),
('webapp.tutoria+teste14@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Patricia Lima', 'Belém', 'PA', '1984-06-27', ST_GeomFromText('POINT(-48.4902 -1.4558)', 4326)),
('webapp.tutoria+teste15@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Rafael Silva', 'São Luís', 'MA', '1993-08-03', ST_GeomFromText('POINT(-44.3068 -2.5307)', 4326)),
('webapp.tutoria+teste16@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Larissa Souza', 'Natal', 'RN', '1996-02-15', ST_GeomFromText('POINT(-35.2110 -5.7945)', 4326)),
('webapp.tutoria+teste17@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Andre Oliveira', 'Teresina', 'PI', '1982-12-20', ST_GeomFromText('POINT(-42.8038 -5.0920)', 4326)),
('webapp.tutoria+teste18@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Camila Mendes', 'João Pessoa', 'PB', '1990-05-10', ST_GeomFromText('POINT(-34.8450 -7.1195)', 4326)),
('webapp.tutoria+teste19@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Felipe Alves', 'Maceió', 'AL', '1985-09-02', ST_GeomFromText('POINT(-35.7353 -9.6658)', 4326)),
('webapp.tutoria+teste20@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Beatriz Costa', 'Aracaju', 'SE', '1994-03-25', ST_GeomFromText('POINT(-37.0731 -10.9472)', 4326)),
('webapp.tutoria+teste21@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Rodrigo Ferreira', 'Campo Grande', 'MS', '1988-07-08', ST_GeomFromText('POINT(-54.6201 -20.4697)', 4326)),
('webapp.tutoria+teste22@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Vanessa Pereira', 'Cuiabá', 'MT', '1991-11-14', ST_GeomFromText('POINT(-56.0974 -15.6010)', 4326)),
('webapp.tutoria+teste23@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Marcelo Martins', 'Porto Velho', 'RO', '1987-04-30', ST_GeomFromText('POINT(-63.9039 -8.7619)', 4326)),
('webapp.tutoria+teste24@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Elaine Santos', 'Rio Branco', 'AC', '1984-10-18', ST_GeomFromText('POINT(-67.8249 -9.9754)', 4326)),
('webapp.tutoria+teste25@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Igor Gomes', 'Boa Vista', 'RR', '1993-01-22', ST_GeomFromText('POINT(-60.6758 2.8235)', 4326)),
('webapp.tutoria+teste26@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Leticia Lima', 'São Paulo', 'SP', '1995-06-05', ST_GeomFromText('POINT(-46.6333 -23.5505)', 4326)),
('webapp.tutoria+teste27@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Danilo Silva', 'Rio de Janeiro', 'RJ', '1989-08-28', ST_GeomFromText('POINT(-43.1729 -22.9068)', 4326)),
('webapp.tutoria+teste28@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Monica Souza', 'Belo Horizonte', 'MG', '1992-02-14', ST_GeomFromText('POINT(-43.9345 -19.9167)', 4326)),
('webapp.tutoria+teste29@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Eduardo Oliveira', 'Salvador', 'BA', '1986-11-09', ST_GeomFromText('POINT(-38.5016 -12.9777)', 4326)),
('webapp.tutoria+teste30@gmail.com', 'pbkdf2_sha256$1000000$Puno9AlBwFpMzEwmivywLO$MVEGoa7Tl6ss3/SXicru2pzqOI3LV1jne/qcs3XNkGI=', 'Vanderson Silva', 'Recife', 'PE', '2002-08-10', ST_GeomFromText('POINT(-34.8770 -8.0476)', 4326));

-- CONQUISTAS (Total: 31)
INSERT INTO CONQUISTA (tier, pontos, titulo, descricao, urlImagem) VALUES
('B', 50, 'Olá Mundo!', 'Se cadastrou na plataforma.', 'OlaMundo.png'),
('B', 50, 'Primeiro Contato', 'Mandou sua primeira mensagem.', 'contato.png'),
('B', 100, 'Primeiro Passo', 'Realizou a primeira tutoria com sucesso.', 'passo.png'),
('B', 150, 'Networking Inicial', 'Mandou mensagem para 5 tutores diferentes.', 'networking.png'),
('B', 150, 'Primeira Impressão', 'Recebeu sua primeira avaliação como tutor ou aprendiz.', 'impressao.png'),
('B', 100, 'Caminho das Pedras I', 'Participou de 5 sessões de tutoria.', 'caminho1.png'),
('B', 150, 'O que?! Quer uma medalha?', 'Conseguiu alcançar o nível 5.', 'querUmaMedalha.png'),
('P', 300, 'Volte Sempre', 'Recebeu sua primeira avaliação 5 estrelas como tutor.', 'volteSempre.png'),
('P', 300, 'O prazer foi meu', 'Recebeu sua primeira avaliação 5 estrelas como aprendiz.', 'prazer.png'),
('P', 350, 'Fidelidade', 'Realizou 5 ou mais tutorias com o mesmo tutor.', 'fidelidade.png'),
('P', 500, 'Pau pra Toda Obra', 'Forneceu tutoria em 3 áreas de conhecimento diferentes.', 'todaObra.png'),
('P', 350, 'Caminho das Pedras II', 'Participou de 15 sessões de tutoria.', 'caminho2.png'),
('P', 600, 'Caminho das Pedras III', 'Participou de 30 sessões de tutoria.', 'caminho3.png'),
('P', 500, 'Interessante...', 'Conseguiu alcançar o nível 10.', 'interessante.png'),
('O', 800, 'Feedback de Peso', 'Recebeu 3 avaliações com comentário maior que 100 caracteres.', 'feedback.png'),
('O', 900, 'Incansável', 'Participou de tutorias por 5 dias seguidos.', 'incansavel.png'),
('O', 1200, 'Veterano', 'Forneceu 50 tutorias em uma única especialidade.', 'veterano.png'),
('O', 1100, 'Caminho das Pedras IV', 'Participou de 60 sessões de tutoria.', 'caminho4.png'),
('O', 1400, 'Caminho das Pedras V', 'Participou de 100 sessões de tutoria.', 'caminho5.png'),
('O', 1200, 'O que você quer provar?', 'Conseguiu alcançar o nível 25.', 'oQueVoceQuerProvar.png'),
('D', 2500, 'Caminho das Pedras VI', 'Participou de 300 sessões de tutoria.', 'caminho6.png'),
('D', 3000, 'Lenda', 'Conseguiu alcançar o nível 50.', 'Lenda.png');

INSERT INTO CONQUISTA (tier, pontos, titulo, descricao, urlImagem, secreta, pista) VALUES
('B', 150, 'Agora é minha vez!', 'Se tornou um tutor.', 'minhavez.png', true, 'Quem aprende também pode ensinar...'),
('B', 200, 'Fim de Semana Ativo', 'Realizou uma tutoria em final de semana.', 'fimdesemana.png', true, 'O conhecimento não tira folga no sábado ou domingo...'),
('P', 400, 'Coruja', 'Realizou uma tutoria na madrugada (22h às 05h).', 'coruja.png', true, 'Para aqueles cujas mentes brilham sob o luar...'),
('P', 450, 'Guerreiro do Feriado', 'Realizou uma tutoria em um feriado nacional.', 'guerreiro.png', true, 'Enquanto todos festeja e comemoram, você evolui...'),
('O', 850, 'Estrela Ascendente', 'Recebeu 5 avaliações 5 estrelas.', 'estrela.png', true, 'Um céu bonito é cheio de estrelas...'),
('O', 1000, 'Mestre Bem-Avaliado', 'Manteve uma média maior ou igual a 4.7 como tutor após 20 avaliações.', 'bemAvaliado.png', true, 'A excelência é reconhecida pelos seus aprendizes...'),
('O', 800, 'O Nascimento do Conhecimento', 'Participou de uma tutoria no seu aniversário.', 'nascimento.png', true, 'Nesse dia tão especial, seu presente é o conhecimento!'),
('D', 1600, 'Mestre das Estrelas', 'Recebeu 15 avaliações 5 estrelas.', 'mestreEstrelas.png', true, 'Seu comprometimento tem uma constelação própria!'),
('D', 2000, 'Deixando uma Marca', 'Manteve uma média maior ou igual a 4.7 como tutor ou aprendiz após 80 avaliações.', 'marca.png', true, 'Um legado gravado na história da plataforma...');

-- AREAS (Total: 25
INSERT INTO AREA (nomeArea) VALUES
('Matemática'), ('Programação'), ('Design Gráfico'), ('Idiomas'), ('Ciências Exatas'),
('História'), ('Geografia'), ('Biologia'), ('Química'), ('Física'),
('Filosofia'), ('Sociologia'), ('Artes'), ('Música'), ('Educação Física'),
('Economia'), ('Direito'), ('Medicina'), ('Psicologia'), ('Arquitetura'),
('Marketing'), ('Gastronomia'), ('Moda'), ('Fotografia'), ('Cinema');

-- ESPECIALIDADES (Total: 25)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(1, 1, 'Cálculo Diferencial'),
(2, 2, 'Desenvolvimento Web'),
(3, 3, 'Photoshop Avançado'),
(4, 4, 'Inglês Intermediário'),
(5, 5, 'Física Quântica'),
(6, 6, 'Brasil Colônia'),
(7, 7, 'Geopolítica Moderna'),
(8, 8, 'Genética Molecular'),
(9, 9, 'Termodinâmica Química'),
(10, 10, 'Mecânica Clássica'),
(11, 11, 'Existencialismo'),
(12, 12, 'Teoria Crítica'),
(13, 13, 'Pintura a Óleo'),
(14, 14, 'Teoria Musical'),
(15, 15, 'Fisiologia do Exercício'),
(16, 16, 'Microeconomia'),
(17, 17, 'Direito Civil'),
(18, 18, 'Anatomia Humana'),
(19, 19, 'Psicologia Cognitiva'),
(20, 20, 'Urbanismo Sustentável'),
(21, 21, 'Marketing Digital'),
(22, 22, 'Culinária Italiana'),
(23, 23, 'Corte e Costura'),
(24, 24, 'Iluminação de Estúdio'),
(25, 25, 'Roteiro Cinematográfico'),
(26, 2, 'Sistemas Embarcados');

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
(1, 1), (1, 2),
(2, 2),
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

INSERT INTO SESSAO (
    dataSessao,
    horarioInicio,
    horarioFim,
    usuarioId,
    tutorId,
    areaId,
    especialidadeId
) VALUES (
    '2026-07-25',      -- Data passada
    '14:00:00',
    '15:00:00',
    1,                 -- Admin (Aprendiz)
    2,                 -- Tutor 2 (Quem o Admin precisa avaliar)
    1,
    1
);

-------------------------------------------------------------------------
-- 2. Sessão onde o Admin participou como TUTOR (ficou pendente de avaliar o Aprendiz)
-- *Nota: Requer que o Admin possua um registro na tabela TUTOR (ex: tutorId = 1)
-------------------------------------------------------------------------
INSERT INTO SESSAO (
    dataSessao,
    horarioInicio,
    horarioFim,
    usuarioId,
    tutorId,
    areaId,
    especialidadeId
) VALUES (
    '2026-07-26',      -- Data passada
    '10:00:00',
    '11:00:00',
    2,                 -- Aprendiz 2 (Quem o Admin precisa avaliar)
    1,                 -- Admin (Tutor)
    1,                 -- areaId
    1                  -- especialidadeId
);                     -- Parêntese e ponto e vírgula fechados corretamente!

-- =========================================================================
-- AVALIACOES_APRENDIZ (Total: 41 - Mapeamento 1:1 exato com as sessões)
-- =========================================================================
INSERT INTO AVALIACAO_APRENDIZ (usuarioId, sessaoId, nota, comentario, dataCriacao) VALUES
(26, 1, 5, 'Excelente', '2026-05-19 10:05:00'), (27, 2, 5, 'Ótimo', '2026-05-20 12:05:00'), (28, 3, 4, 'Bom', '2026-05-21 11:05:00'), (29, 4, 5, 'Muito bom', '2026-05-22 17:05:00'),
(26, 5, 4, 'Ok', '2026-05-20 12:05:00'), (27, 6, 4, 'Ok', '2026-05-21 12:05:00'), (28, 7, 4, 'Ok', '2026-05-22 12:05:00'), (29, 8, 4, 'Ok', '2026-05-23 12:05:00'), (30, 9, 4, 'Ok', '2026-05-24 12:05:00'), (26, 10, 4, 'Ok', '2026-05-25 12:05:00'),
(26, 11, 5, '', '2026-05-19 11:05:00'), (27, 12, 5, '', '2026-05-20 11:05:00'), (28, 13, 5, '', '2026-05-21 11:05:00'), (29, 14, 4, '', '2026-05-22 11:05:00'), (30, 15, 5, '', '2026-05-23 11:05:00'),
(26, 16, 3, '', '2026-05-19 17:05:00'), (27, 17, 3, '', '2026-05-20 17:05:00'), (28, 18, 4, '', '2026-05-21 17:05:00'),
(26, 19, 4, '', '2026-05-19 10:05:00'), (27, 20, 4, '', '2026-05-20 10:05:00'),
(26, 21, 5, '', '2026-05-19 11:05:00'), (27, 22, 5, '', '2026-05-20 11:05:00'),
(26, 23, 5, '', '2026-05-19 16:05:00'),
(26, 24, 3, '', '2026-05-19 15:05:00'), (26, 25, 4, '', '2026-05-19 18:05:00'), (26, 26, 4, '', '2026-05-19 16:05:00'), (26, 27, 5, '', '2026-05-19 12:05:00'), (26, 28, 4, '', '2026-05-19 10:05:00'),
(26, 29, 2, '', '2026-05-19 16:05:00'), (26, 30, 3, '', '2026-05-19 12:05:00'), (26, 31, 4, '', '2026-05-19 11:05:00'), (26, 32, 4, '', '2026-05-19 17:05:00'), (26, 33, 3, '', '2026-05-19 18:05:00'),
(26, 34, 5, '', '2026-05-19 10:05:00'), (26, 35, 4, '', '2026-05-19 15:05:00'), (26, 36, 4, '', '2026-05-19 12:05:00'), (26, 37, 3, '', '2026-05-19 11:05:00'), (26, 38, 4, '', '2026-05-19 17:05:00'),
(26, 39, 3, '', '2026-05-19 12:05:00'), (26, 40, 5, '', '2026-05-19 10:05:00'), (26, 41, 3, '', '2026-05-19 16:05:00');


-- =========================================================================
-- AVALIACOES_TUTOR (Total: 41 - Uma avaliação real casando com cada Sessão)
-- =========================================================================

INSERT INTO AVALIACAO_TUTOR (tutorId, sessaoId, nota, comentario, dataCriacao) VALUES
(1, 1, 5, 'Excelente didática.', '2026-05-19 10:05:00'), (1, 2, 5, 'Ótimo.', '2026-05-20 12:05:00'), (1, 3, 5, 'Muito prestativo.', '2026-05-21 11:05:00'), (1, 4, 5, 'Perfeito.', '2026-05-22 17:05:00'),
(2, 5, 4, '', '2026-05-20 12:05:00'), (2, 6, 4, '', '2026-05-21 12:05:00'), (2, 7, 5, '', '2026-05-22 12:05:00'), (2, 8, 4, '', '2026-05-23 12:05:00'), (2, 9, 4, '', '2026-05-24 12:05:00'), (2, 10, 5, '', '2026-05-25 12:05:00'),
(3, 11, 5, '', '2026-05-19 11:05:00'), (3, 12, 5, '', '2026-05-20 11:05:00'), (3, 13, 4, '', '2026-05-21 11:05:00'), (3, 14, 5, '', '2026-05-22 11:05:00'), (3, 15, 5, '', '2026-05-23 11:05:00'),
(4, 16, 3, '', '2026-05-19 17:05:00'), (4, 17, 4, '', '2026-05-20 17:05:00'), (4, 18, 3, '', '2026-05-21 17:05:00'),
(5, 19, 4, '', '2026-05-19 10:05:00'), (5, 20, 4, '', '2026-05-20 10:05:00'),
(8, 21, 5, '', '2026-05-19 11:05:00'), (8, 22, 5, '', '2026-05-20 11:05:00'),
(20, 23, 5, '', '2026-05-19 16:05:00'),
(6, 24, 3, '', '2026-05-19 15:05:00'), (7, 25, 4, '', '2026-05-19 18:05:00'), (9, 26, 4, '', '2026-05-19 16:05:00'), (10, 27, 5, '', '2026-05-19 12:05:00'), (11, 28, 4, '', '2026-05-19 10:05:00'),
(12, 29, 2, '', '2026-05-19 16:05:00'), (13, 30, 3, '', '2026-05-19 12:05:00'), (14, 31, 4, '', '2026-05-19 11:05:00'), (15, 32, 4, '', '2026-05-19 17:05:00'), (16, 33, 3, '', '2026-05-19 18:05:00'),
(17, 34, 5, '', '2026-05-19 10:05:00'), (18, 35, 4, '', '2026-05-19 15:05:00'), (19, 36, 4, '', '2026-05-19 12:05:00'), (21, 37, 3, '', '2026-05-19 11:05:00'), (22, 38, 4, '', '2026-05-19 17:05:00'),
(23, 39, 3, '', '2026-05-19 12:05:00'), (24, 40, 5, '', '2026-05-19 10:05:00'), (25, 41, 3, '', '2026-05-19 16:05:00');

-- CHATS (Total: 25)
INSERT INTO CHAT (tutorId, usuarioId) VALUES
(1, 26), (2, 27), (3, 28), (4, 29), (5, 30),
(6, 26), (7, 27), (8, 28), (9, 29), (10, 30),
(11, 26), (12, 27), (13, 28), (14, 29), (15, 30),
(16, 26), (17, 27), (18, 28), (19, 29), (20, 30),
(21, 26), (22, 27), (23, 28), (24, 29), (25, 30);

-- MENSAGENS (Total: 25)
INSERT INTO MENSAGEM (chatId, usuarioId, conteudo) VALUES
(1, 26, 'Olá, gostaria de tirar dúvidas sobre Cálculo.'),
(2, 27, 'Poderia revisar o conteúdo de HTML?'),
(3, 28, 'Como ajustar camadas no Photoshop?'),
(4, 29, 'Pode corrigir meu texto em inglês?'),
(5, 30, 'Fiquei com dúvidas na aula de Física.'),
(6, 26, 'Pode me enviar o material de história?'),
(7, 27, 'Qual o tema da próxima aula de geografia?'),
(8, 28, 'Tenho dúvidas sobre DNA.'),
(9, 29, 'Pode explicar a tabela periódica de novo?'),
(10, 30, 'O que cai na prova de física?'),
(11, 26, 'Qual filósofo vamos estudar hoje?'),
(12, 27, 'Pode me ajudar com o ensaio de sociologia?'),
(13, 28, 'Quais tintas devo comprar?'),
(14, 29, 'Como ler partituras mais rápido?'),
(15, 30, 'Qual o melhor exercício para costas?'),
(16, 26, 'O que é oferta e demanda?'),
(17, 27, 'Como funciona o processo civil?'),
(18, 28, 'Onde fica o fêmur?'),
(19, 29, 'O que é memória de curto prazo?'),
(20, 30, 'Como planejar uma praça?'),
(21, 26, 'Como subir anúncios no Facebook?'),
(22, 27, 'Qual o ponto do risoto?'),
(23, 28, 'Como fazer a barra invisível?'),
(24, 29, 'Qual ISO usar de dia?'),
(25, 30, 'Como criar um plot twist?');

-- CONSEGUE (Relacionamento Usuario-Conquista, Total: 25)
INSERT INTO consegue (usuarioId, conquistaId) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20),
(1, 21),
(1, 22),
(1, 23),
(1, 24),
(1, 25);
