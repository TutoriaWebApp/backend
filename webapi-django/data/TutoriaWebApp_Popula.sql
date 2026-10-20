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

-- CONQUISTAS (Total: 31)
INSERT INTO CONQUISTA (tier, pontos, titulo, descricao, urlImagem) VALUES
('B', 50, 'Olá Mundo!', 'Se cadastrou na plataforma.', 'OlaMundo.png'),
('B', 50, 'Primeiro Contato', 'Mandou sua primeira mensagem.', 'contato.png'),
('B', 100, 'Primeiro Passo', 'Realizou a primeira tutoria com sucesso.', 'passo.png'),
('B', 150, 'Networking Inicial', 'Iniciou uma conversa com 5 usuários diferentes.', 'networking.png'),
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
('O', 1200, 'Veterano', 'Forneceu 50 tutorias em uma única área.', 'veterano.png'),
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
('O', 850, 'Estrela Ascendente', 'Recebeu 20 avaliações 5 estrelas.', 'estrela.png', true, 'Um céu bonito é cheio de estrelas...'),
('O', 1000, 'Mestre Bem-Avaliado', 'Manteve uma média maior ou igual a 4.7 como tutor após 20 avaliações.', 'bemAvaliado.png', true, 'A excelência é reconhecida pelos seus aprendizes...'),
('O', 800, 'O Nascimento do Conhecimento', 'Participou de uma tutoria no seu aniversário.', 'nascimento.png', true, 'Nesse dia tão especial, seu presente é o conhecimento!'),
('D', 1600, 'Mestre das Estrelas', 'Recebeu 50 avaliações 5 estrelas.', 'mestreEstrelas.png', true, 'Seu comprometimento tem uma constelação própria!'),

('D', 2000, 'Deixando uma Marca', 'Manteve uma média maior ou igual a 4.7 como tutor ou aprendiz após 80 avaliações.', 'marca.png', true, 'Um legado gravado na história da plataforma...');

-- AREAS
INSERT INTO AREA (nomeArea) VALUES
('Matemática'),
('Programação'),
('Design Gráfico'),
('Idiomas'),
('História'),
('Geografia'),
('Biologia'),
('Química'),
('Física'),
('Filosofia'),
('Sociologia'),
('Artes'),
('Música'),
('Educação Física'),
('Economia'),
('Direito'),
('Medicina'),
('Psicologia'),
('Arquitetura'),
('Marketing'),
('Gastronomia'),
('Moda'),
('Fotografia'),
('Cinema'),
('Inteligência Artificial'),
('Segurança da Informação'),
('Redes de Computadores'),
('Banco de Dados'),
('Pedagogia'),
('Nutrição'),
('Enfermagem'),
('Odontologia'),
('Fisioterapia'),
('Farmácia'),
('Estatística'),
('Dança'),
('Teatro'),
('Desenho'),
('Pintura'),
('Artesanato'),
('Marcenaria'),
('Redação'),
('Literatura'),
('Oratória'),
('Finanças Pessoais'),
('Investimentos'),
('Yoga'),
('Meditação'),
('Jardinagem'),
('Xadrez'),
('Jogos de Tabuleiro'),
('Edição de Vídeo'),
('Modelagem 3D'),
('Animação'),
('Eletrônica'),
('Robótica'),
('Gastronomia');

-- ESPECIALIDADES 

-- Especialidades de Matemática
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(1, 1, 'Aritmética e Matemática Básica');
(2, 1, 'Álgebra e Equações'),
(3, 1, 'Geometria Plana e Espacial'),
(4, 1, 'Trigonometria'),
(5, 1, 'Matemática Financeira'),
(6, 1, 'Raciocínio Lógico'),
(7, 1, 'Matemática para ENEM e Vestibulares'),
--Ensino Superior e Graduação
(5, 1, 'Cálculo 1'),
(6, 1, 'Cálculo 2'),
(7, 1, 'Cálculo 3'),
(8, 1, 'Geometria Analítica'),
(9, 1, 'Álgebra Linear'),
(10, 1, 'Cálculo Numérico');
(11, 1, 'Equações Diferenciais Ordinárias (EDO)'),
(12, 1, 'Cálculo Numérico'),
(13, 1, 'Matemática Discreta'),
(14, 1, 'Probabilidade e Estatística'),
(15, 1, 'Análise Real'),
(16, 1, 'Variáveis Complexas');

-- Especialidades de Programação
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
-- Fundamentos e Conceitos
(17, 2, 'Lógica de Programação'),
(18, 2, 'Algoritmos e Estruturas de Dados'),
(19, 2, 'Programação Orientada a Objetos (POO)'),
(20, 2, 'Programação Funcional'),

-- Linguagens de Programação
(21, 2, 'Python'),
(22, 2, 'JavaScript e TypeScript'),
(23, 2, 'Java'),
(24, 2, 'C'),
(25, 2, 'C++'),
(26, 2, 'C#'),
(27, 2, '.NET'),
(28, 2, 'PHP'),
(29, 2, 'Go (Golang)'),
(30, 2, 'Rust'),
(31, 2, 'Kotlin'),
(32, 2, 'Swift'),
(33, 2, 'Ruby'),

-- Desenvolvimento de Aplicações
(34, 2, 'React'),
(35, 2, 'Vue'),
(36, 2, 'Angular'),
(37, 2, 'Node.js'),
(38, 2, 'Django'),
(39, 2, 'Spring'),
(40, 2, 'Flutter'),
(41, 2, 'React Native'),

-- Engenharia de Software, Arquitetura e Boas Práticas
(42, 2, 'Padrões de Projeto (Design Patterns)'),
(43, 2, 'Arquiteturas de Software e Microsserviços'),
(44, 2, 'Clean Code e Refatoração'),
(45, 2, 'Testes de Software'),
(46, 2, 'Git e Controle de Versão'),
(47, 2, 'DevOps'),
(48, 2, 'Sistemas Distribuídos');
(49, 2, 'CSS');
(50, 2, 'HTML');

-- Especialidades para Design Gráfico (areaId = 3)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
-- Softwares e Ferramentas
(51, 3, 'Adobe Photoshop'),
(52, 3, 'Adobe Illustrator'),
(53, 3, 'Adobe InDesign'),
(54, 3, 'Figma'),
(55, 3, 'Canva'),
(56, 3, 'CorelDRAW'),
(57, 3, 'Affinity Designer'),

-- Fundamentos e Conceitos
(58, 3, 'Tipografia'),
(59, 3, 'Teoria das Cores'),
(60, 3, 'Composição e Grid'),

-- Áreas de Atuação e Especialidades
(61, 3, 'Design de Logotipos'),
(62, 3, 'Identidade Visual'),
(63, 3, 'Branding'),
(64, 3, 'UI Design'),
(65, 3, 'UX Design'),
(66, 3, 'Motion Design'),
(67, 3, 'Design Editorial'),
(68, 3, 'Diagramação'),
(69, 3, 'Design para Redes Sociais'),
(70, 3, 'Design de Embalagens'),
(71, 3, 'Vetorização'),
(72, 3, 'Tratamento de Imagem');

-- Especialidades para Idiomas (areaId = 4)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
-- Inglês
(73, 4, 'Inglês Básico'),
(74, 4, 'Inglês Intermediário'),
(75, 4, 'Inglês Avançado'),
(76, 4, 'Conversação em Inglês'),
(77, 4, 'Inglês para Negócios'),
(78, 4, 'Preparatório TOEFL e IELTS'),

-- Espanhol
(79, 4, 'Espanhol Básico'),
(80, 4, 'Espanhol Intermediário'),
(81, 4, 'Espanhol Avançado'),
(82, 4, 'Conversação em Espanhol'),

-- Outros Idiomas
(83, 4, 'Francês'),
(84, 4, 'Alemão'),
(85, 4, 'Italiano'),
(86, 4, 'Japonês'),
(87, 4, 'Mandarim'),
(88, 4, 'Coreano'),
(89, 4, 'Russo'),
(90, 4, 'LIBRAS (Língua Brasileira de Sinais)'),
(91, 4, 'Português para Estrangeiros');

-- Especialidades para História (areaId = 5)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
-- História do Brasil
(92, 5, 'História do Brasil Colônia'),
(93, 5, 'História do Brasil Império'),
(94, 5, 'História do Brasil República'),
(95, 5, 'Período Militar no Brasil'),

-- História Geral
(96, 5, 'Pré-História'),
(97, 5, 'História Antiga'),
(98, 5, 'História Medieval'),
(99, 5, 'História Moderna'),
(100, 5, 'História Contemporânea'),

-- História Regional e Temática
(101, 5, 'História da América'),
(102, 5, 'História da África'),
(103, 5, 'História da Europa'),
(104, 5, 'História da Ásia'),
(105, 5, 'História das Guerras Mundiais'),
(106, 5, 'Guerra Fria'),

-- Ensino Superior e Teoria
(107, 5, 'Historiografia'),
(108, 5, 'Teoria da História'),
(109, 5, 'Patrimônio e Memória');

-- Especialidades para Geografia (areaId = 6)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
-- Geografia Geral e Física
(110, 6, 'Geografia Física'),
(111, 6, 'Geografia Humana'),
(112, 6, 'Climatologia'),
(113, 6, 'Geomorfologia'),
(114, 6, 'Hidrografia'),
(115, 6, 'Biogeografia'),

-- Geografia Humana e Econômica
(116, 6, 'Geopolítica'),
(117, 6, 'Geografia Urbana'),
(118, 6, 'Geografia Agrária'),
(119, 6, 'Geografia Econômica'),
(120, 6, 'Demografia e População'),
(121, 6, 'Geografia Ambiental'),

-- Regional
(122, 6, 'Geografia do Brasil'),
(123, 6, 'Geografia Mundial'),

-- Geotecnologias
(124, 6, 'Cartografia'),
(125, 6, 'Sistemas de Informação Geográfica (SIG)'),
(126, 6, 'Sensoriamento Remoto');

-- Especialidades para Biologia (areaId = 7)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(127, 7, 'Citologia'),
(128, 7, 'Histologia'),
(129, 7, 'Genética'),
(130, 7, 'Evolução'),
(131, 7, 'Ecologia'),
(132, 7, 'Botânica'),
(133, 7, 'Zoologia'),
(134, 7, 'Microbiologia'),
(135, 7, 'Parasitologia'),
(136, 7, 'Embriologia'),
(137, 7, 'Anatomia Humana'),
(138, 7, 'Fisiologia Humana'),
(139, 7, 'Biologia Molecular'),
(140, 7, 'Biotecnologia'),
(141, 7, 'Bioquímica'),
(142, 7, 'Imunologia'),
(143, 7, 'Biologia Marinha');

-- Especialidades para Química (areaId = 8)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(144, 8, 'Química Geral'),
(145, 8, 'Química Inorgânica'),
(146, 8, 'Química Orgânica'),
(147, 8, 'Físico-Química'),
(148, 8, 'Química Analítica'),
(149, 8, 'Estequiometria'),
(150, 8, 'Termoquímica'),
(151, 8, 'Eletroquímica'),
(152, 8, 'Cinética Química'),
(153, 8, 'Equilíbrio Químico'),
(154, 8, 'Química Ambiental'),
(155, 8, 'Química Quântica'),
(156, 8, 'Espectroscopia'),
(157, 8, 'Química Industrial');

-- Especialidades para Física (areaId = 9)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(158, 9, 'Cinemática'),
(159, 9, 'Dinâmica e Leis de Newton'),
(160, 9, 'Estática e Hidrostática'),
(161, 9, 'Termodinâmica e Calorimetria'),
(162, 9, 'Óptica Geométrica'),
(163, 9, 'Ondulatória'),
(164, 9, 'Eletrostática'),
(165, 9, 'Eletrodinâmica'),
(166, 9, 'Eletromagnetismo'),
(167, 9, 'Física Moderna'),
(168, 9, 'Relatividade Restrita'),
(169, 9, 'Física Quântica'),
(170, 9, 'Astrofísica'),
(171, 9, 'Física Nuclear'),
(172, 9, 'Mecânica Estatística');

-- Especialidades para Filosofia (areaId = 10)
INSERT INTO ESPECIALIDADE (especialidadeId, areaId, nomeEspecialidade) VALUES
(173, 10, 'Ética'),
(174, 10, 'Estética'),
(175, 10, 'Lógica'),
(176, 10, 'Epistemologia'),
(177, 10, 'Metafísica'),
(178, 10, 'Filosofia Política'),
(179, 10, 'Filosofia Antiga'),
(180, 10, 'Filosofia Medieval'),
(181, 10, 'Filosofia Moderna'),
(182, 10, 'Filosofia Contemporânea'),
(183, 10, 'Filosofia da Mente'),
(184, 10, 'Filosofia da Linguagem'),
(185, 10, 'Filosofia da Ciência'),
(186, 10, 'Existencialismo'),
(187, 10, 'Fenomenologia');
