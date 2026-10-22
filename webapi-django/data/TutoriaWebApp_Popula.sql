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
INSERT INTO CONQUISTA (tier, pontos, titulo, descricao, urlImagem, secreta, pista) VALUES
('B', 50, 'Olá Mundo!', 'Se cadastrou na plataforma.', 'OlaMundo.png', false, null),
('B', 50, 'Primeiro Contato', 'Mandou sua primeira mensagem.', 'contato.png', false, null),
('B', 100, 'Primeiro Passo', 'Realizou a primeira tutoria com sucesso.', 'passo.png', false, null),
('B', 150, 'Networking Inicial', 'Iniciou uma conversa com 5 usuários diferentes.', 'networking.png', false, null),
('B', 150, 'Primeira Impressão', 'Recebeu sua primeira avaliação como tutor ou aprendiz.', 'impressao.png', false, null),
('B', 100, 'Caminho das Pedras I', 'Participou de 5 sessões de tutoria.', 'caminho1.png', false, null),
('B', 150, 'O que?! Quer uma medalha?', 'Conseguiu alcançar o nível 5.', 'querUmaMedalha.png', false, null),
('P', 300, 'Volte Sempre', 'Recebeu sua primeira avaliação 5 estrelas como tutor.', 'volteSempre.png', false, null),
('P', 300, 'O prazer foi meu', 'Recebeu sua primeira avaliação 5 estrelas como aprendiz.', 'prazer.png', false, null),
('P', 350, 'Fidelidade', 'Realizou 5 ou mais tutorias com o mesmo tutor.', 'fidelidade.png', false, null),

('P', 500, 'Pau pra Toda Obra', 'Forneceu tutoria em 3 áreas de conhecimento diferentes.', 'todaObra.png', false, null),
('P', 350, 'Caminho das Pedras II', 'Participou de 15 sessões de tutoria.', 'caminho2.png', false, null),
('P', 600, 'Caminho das Pedras III', 'Participou de 30 sessões de tutoria.', 'caminho3.png', false, null),
('P', 500, 'Interessante...', 'Conseguiu alcançar o nível 10.', 'interessante.png', false, null),
('O', 800, 'Feedback de Peso', 'Recebeu 3 avaliações com comentário maior que 100 caracteres.', 'feedback.png', false, null),
('O', 900, 'Incansável', 'Participou de tutorias por 5 dias seguidos.', 'incansavel.png', false, null),
('O', 1200, 'Veterano', 'Forneceu 50 tutorias em uma única área.', 'veterano.png', false, null),
('O', 1100, 'Caminho das Pedras IV', 'Participou de 60 sessões de tutoria.', 'caminho4.png', false, null),
('O', 1400, 'Caminho das Pedras V', 'Participou de 100 sessões de tutoria.', 'caminho5.png', false, null),
('O', 1200, 'O que você quer provar?', 'Conseguiu alcançar o nível 25.', 'oQueVoceQuerProvar.png', false, null),

('D', 2500, 'Caminho das Pedras VI', 'Participou de 300 sessões de tutoria.', 'caminho6.png', false, null),
('D', 3000, 'Lenda', 'Conseguiu alcançar o nível 50.', 'Lenda.png', false, null),
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
('Áudio Visual'),
('Sociologia'),
('Música'),
('Educação Física'),
('Direito'),
('Medicina'),
('Psicologia'),
('Arquitetura'),
('Marketing'),
('Gastronomia'),
('Pedagogia'),
('Nutrição'),
('Enfermagem'),
('Odontologia'),
('Fisioterapia'),
('Farmácia'),
('Estatística'),
('Teatro'),
('Desenho'),
('Pintura'),
('Artesanato'),
('Marcenaria'),
('Redação'),
('Literatura'),
('Oratória'),
('Economia'),
('Xadrez'),
('Modelagem 3D'),
('Animação'),
('Eletrônica'),
('Robótica');

-- ESPECIALIDADES

-- Especialidades de Matemática
INSERT INTO ESPECIALIDADE (areaId, nomeEspecialidade) VALUES
(1, 'Aritmética e Matemática Básica'),
(1, 'Álgebra e Equações'),
(1, 'Geometria Plana e Espacial'),
(1, 'Trigonometria'),
(1, 'Matemática Financeira'),
(1, 'Raciocínio Lógico'),
(1, 'Matemática para ENEM e Vestibulares'),
(1, 'Cálculo 1'),
(1, 'Cálculo 2'),
(1, 'Cálculo 3'),
(1, 'Geometria Analítica'),
(1, 'Álgebra Linear'),
(1, 'Cálculo Numérico'),
(1, 'Equações Diferenciais Ordinárias (EDO)'),
(1, 'Matemática Discreta'),
(1, 'Probabilidade e Estatística'),
(1, 'Análise Real'),
(1, 'Variáveis Complexas'),

-- Especialidades de Programação
(2, 'Lógica de Programação'),
(2, 'Algoritmos e Estruturas de Dados'),
(2, 'Programação Orientada a Objetos (POO)'),
(2, 'Programação Funcional'),
(2, 'Python'),
(2, 'JavaScript e TypeScript'),
(2, 'Java'),
(2, 'C'),
(2, 'C++'),
(2, 'C#'),
(2, '.NET'),
(2, 'PHP'),
(2, 'Go (Golang)'),
(2, 'Rust'),
(2, 'Kotlin'),
(2, 'Swift'),
(2, 'Ruby'),
(2, 'React'),
(2, 'Vue'),
(2, 'Angular'),
(2, 'Node.js'),
(2, 'Django'),
(2, 'Spring'),
(2, 'Flutter'),
(2, 'React Native'),
(2, 'Padrões de Projeto (Design Patterns)'),
(2, 'Arquiteturas de Software e Microsserviços'),
(2, 'Clean Code e Refatoração'),
(2, 'Testes de Software'),
(2, 'Git e Controle de Versão'),
(2, 'DevOps'),
(2, 'Sistemas Distribuídos'),
(2, 'CSS'),
(2, 'HTML'),
(2, 'Inteligência Artificial'),
(2, 'Segurança da Informação'),
(2, 'Redes de Computadores'),
(2, 'Banco de Dados'),

-- Especialidades para Design Gráfico (areaId = 3)
(3, 'Adobe Photoshop'),
(3, 'Adobe Illustrator'),
(3, 'Adobe InDesign'),
(3, 'Figma'),
(3, 'Canva'),
(3, 'CorelDRAW'),
(3, 'Affinity Designer'),
(3, 'Tipografia'),
(3, 'Teoria das Cores'),
(3, 'Composição e Grid'),
(3, 'Design de Logotipos'),
(3, 'Identidade Visual'),
(3, 'Branding'),
(3, 'UI Design'),
(3, 'UX Design'),
(3, 'Motion Design'),
(3, 'Design Editorial'),
(3, 'Diagramação'),
(3, 'Design para Redes Sociais'),
(3, 'Design de Embalagens'),
(3, 'Vetorização'),
(3, 'Tratamento de Imagem'),

-- Especialidades para Idiomas (areaId = 4)
(4, 'Inglês Básico'),
(4, 'Inglês Intermediário'),
(4, 'Inglês Avançado'),
(4, 'Conversação em Inglês'),
(4, 'Inglês para Negócios'),
(4, 'Preparatório TOEFL e IELTS'),
(4, 'Espanhol Básico'),
(4, 'Espanhol Intermediário'),
(4, 'Espanhol Avançado'),
(4, 'Conversação em Espanhol'),
(4, 'Francês'),
(4, 'Alemão'),
(4, 'Italiano'),
(4, 'Japonês'),
(4, 'Mandarim'),
(4, 'Coreano'),
(4, 'Russo'),
(4, 'LIBRAS (Língua Brasileira de Sinais)'),
(4, 'Português para Estrangeiros'),

-- Especialidades para História (areaId = 5)
(5, 'História do Brasil Colônia'),
(5, 'História do Brasil Império'),
(5, 'História do Brasil República'),
(5, 'Período Militar no Brasil'),
(5, 'Pré-História'),
(5, 'História Antiga'),
(5, 'História Medieval'),
(5, 'História Moderna'),
(5, 'História Contemporânea'),
(5, 'História da América'),
(5, 'História da África'),
(5, 'História da Europa'),
(5, 'História da Ásia'),
(5, 'História das Guerras Mundiais'),
(5, 'Guerra Fria'),
(5, 'Historiografia'),
(5, 'Teoria da História'),
(5, 'Patrimônio e Memória'),

-- Especialidades para Geografia (areaId = 6)
(6, 'Geografia Física'),
(6, 'Geografia Humana'),
(6, 'Climatologia'),
(6, 'Geomorfologia'),
(6, 'Hidrografia'),
(6, 'Biogeografia'),
(6, 'Geopolítica'),
(6, 'Geografia Urbana'),
(6, 'Geografia Agrária'),
(6, 'Geografia Econômica'),
(6, 'Demografia e População'),
(6, 'Geografia Ambiental'),
(6, 'Geografia do Brasil'),
(6, 'Geografia Mundial'),
(6, 'Cartografia'),
(6, 'Sistemas de Informação Geográfica (SIG)'),
(6, 'Sensoriamento Remoto'),

-- Especialidades para Biologia (areaId = 7)
(7, 'Citologia'),
(7, 'Histologia'),
(7, 'Genética'),
(7, 'Evolução'),
(7, 'Ecologia'),
(7, 'Botânica'),
(7, 'Zoologia'),
(7, 'Microbiologia'),
(7, 'Parasitologia'),
(7, 'Embriologia'),
(7, 'Anatomia Humana'),
(7, 'Fisiologia Humana'),
(7, 'Biologia Molecular'),
(7, 'Biotecnologia'),
(7, 'Bioquímica'),
(7, 'Imunologia'),
(7, 'Biologia Marinha'),

-- Especialidades para Química (areaId = 8)
(8, 'Química Geral'),
(8, 'Química Inorgânica'),
(8, 'Química Orgânica'),
(8, 'Físico-Química'),
(8, 'Química Analítica'),
(8, 'Estequiometria'),
(8, 'Termoquímica'),
(8, 'Eletroquímica'),
(8, 'Cinética Química'),
(8, 'Equilíbrio Químico'),
(8, 'Química Ambiental'),
(8, 'Química Quântica'),
(8, 'Espectroscopia'),
(8, 'Química Industrial'),

-- Especialidades para Física (areaId = 9)
(9, 'Cinemática'),
(9, 'Dinâmica e Leis de Newton'),
(9, 'Estática e Hidrostática'),
(9, 'Termodinâmica e Calorimetria'),
(9, 'Óptica Geométrica'),
(9, 'Ondulatória'),
(9, 'Eletrostática'),
(9, 'Eletrodinâmica'),
(9, 'Eletromagnetismo'),
(9, 'Física Moderna'),
(9, 'Relatividade Restrita'),
(9, 'Física Quântica'),
(9, 'Astrofísica'),
(9, 'Física Nuclear'),
(9, 'Mecânica Estatística'),

-- Especialidades para Filosofia (areaId = 10)
(10, 'Ética'),
(10, 'Estética'),
(10, 'Lógica'),
(10, 'Epistemologia'),
(10, 'Metafísica'),
(10, 'Filosofia Política'),
(10, 'Filosofia Antiga'),
(10, 'Filosofia Medieval'),
(10, 'Filosofia Moderna'),
(10, 'Filosofia Contemporânea'),
(10, 'Filosofia da Mente'),
(10, 'Filosofia da Linguagem'),
(10, 'Filosofia da Ciência'),
(10, 'Existencialismo'),
(10, 'Fenomenologia'),

-- Especialidades para Áudio Visual (areaId = 11)
(11, 'Produção Audiovisual'),
(11, 'Direção de Cinema e TV'),
(11, 'Roteiro e Narrativa'),
(11, 'Direção de Fotografia'),
(11, 'Operação de Câmera'),
(11, 'Iluminação para Vídeo'),
(11, 'Captação de Áudio Direto'),
(11, 'Edição de Vídeo'),
(11, 'Color Grading (Correção de Cor)'),
(11, 'Edição e Mixagem de Áudio'),
(11, 'Sound Design (Design de Som)'),
(11, 'Efeitos Visuais (VFX)'),
(11, 'Motion Graphics'),
(11, 'Produção de Documentários'),
(11, 'Transmissão ao Vivo e Streaming'),

-- Especialidades para Sociologia (areaId = 12)
(12, 'Sociologia Geral'),
(12, 'Teoria Sociológica Clássica'),
(12, 'Teoria Sociológica Contemporânea'),
(12, 'Sociologia do Trabalho'),
(12, 'Sociologia da Educação'),
(12, 'Sociologia Política'),
(12, 'Sociologia da Cultura'),
(12, 'Sociologia Urbana'),
(12, 'Sociologia Rural'),
(12, 'Sociologia da Religião'),
(12, 'Sociologia Brasileira'),
(12, 'Movimentos Sociais'),
(12, 'Desigualdade Social e Estratificação'),
(12, 'Relações Étnico-Raciais'),
(12, 'Estudos de Gênero e Sexualidade'),
(12, 'Metodologia de Pesquisa nas Ciências Sociais'),
(12, 'Antropologia Cultural'),
(12, 'Ciência Política'),

-- Especialidades para Música (areaId = 13)
-- Teoria e Fundamentos
(13, 'Teoria Musical'),
(13, 'Harmonia e Arranjo'),
(13, 'Solfejo e Percepção Musical'),
(13, 'Leitura de Partitura'),
(13, 'Composição Musical'),
(13, 'História da Música'),

-- Canto e Voz
(13, 'Canto Popular'),
(13, 'Canto Lírico'),
(13, 'Técnica Vocal'),
(13, 'Canto Coral'),

-- Instrumentos de Cordas (Dedilhadas e Friccionadas)
(13, 'Violão Clássico'),
(13, 'Violão Popular'),
(13, 'Guitarra Elétrica'),
(13, 'Contrabaixo Elétrico'),
(13, 'Ukulele'),
(13, 'Cavaquinho'),
(13, 'Viola Caipira'),
(13, 'Violino'),
(13, 'Violoncelo'),

-- Instrumentos de Teclas
(13, 'Piano Erudito'),
(13, 'Piano Popular'),
(13, 'Teclado e Sintetizador'),
(13, 'Acordeon'),

-- Instrumentos de Sopro
(13, 'Flauta Doce'),
(13, 'Flauta Transversal'),
(13, 'Saxofone'),
(13, 'Trompete'),
(13, 'Clarinete'),
(13, 'Trombone'),

-- Instrumentos de Percussão
(13, 'Bateria'),
(13, 'Percussão Popular Brasileira'),
(13, 'Cajón'),
(13, 'Percussão Sinfônica'),

-- Tecnologia e Produção
(13, 'Produção Musical'),
(13, 'Home Studio e Gravação'),

-- Especialidades para Educação Física (areaId = 14)
-- Fundamentos e Ciências do Movimento
(14, 'Anatomia e Cinesiologia'),
(14, 'Fisiologia do Exercício'),
(14, 'Biomecânica do Movimento'),
(14, 'Desenvolvimento e Aprendizagem Motora'),

-- Metodologias de Treino e Saúde
(14, 'Treino de Força e Musculação'),
(14, 'Treino Funcional'),
(14, 'Condicionamento Físico'),
(14, 'Atividade Física para Grupos Especiais'),
(14, 'Ergonomia e Ginástica Laboral'),
(14, 'Avaliação Física e Antropométrica'),
(14, 'Educação Física Escolar'),
(14, 'Recreação e Lazer'),

-- Desportos Coletivos e Individuais
(14, 'Futebol'),
(14, 'Futsal'),
(14, 'Basquetebol'),
(14, 'Voleibol'),
(14, 'Andebol'),
(14, 'Natação'),
(14, 'Atletismo'),
(14, 'Ginástica Artística'),
(14, 'Ginástica Rítmica'),

-- Lutas e Artes Marciais
(14, 'Judô'),
(14, 'Karaté'),
(14, 'Jiu-Jitsu'),
(14, 'Boxe'),
(14, 'Capoeira'),

-- Especialidades para Direito (areaId = 15)
-- Direito Público
(15, 'Direito Constitucional'),
(15, 'Direito Administrativo'),
(15, 'Direito Penal'),
(15, 'Direito Processual Penal'),
(15, 'Direito Tributário'),
(15, 'Direito Internacional Público'),
(15, 'Direito Eleitoral'),
(15, 'Direito Ambiental'),

-- Direito Privado
(15, 'Direito Civil'),
(15, 'Direito Processual Civil'),
(15, 'Direito Empresarial e Comercial'),
(15, 'Direito do Trabalho'),
(15, 'Direito Processual do Trabalho'),
(15, 'Direito do Consumidor'),
(15, 'Direito de Família e Sucessões'),
(15, 'Direito Imobiliário'),
(15, 'Direito Internacional Privado'),

-- Direitos Sociais e Novas Áreas
(15, 'Direito Previdenciário'),
(15, 'Direito Digital e Cibernético'),
(15, 'Direito Desportivo'),
(15, 'Direito Médico e da Saúde'),

-- Fundamentos
(15, 'Teoria Geral do Direito'),
(15, 'Filosofia do Direito'),
(15, 'História do Direito'),

-- Especialidades para Medicina (areaId = 16)
-- Ciclo Básico e Fundamentos
(16, 'Anatomia Humana'),
(16, 'Fisiologia Médica'),
(16, 'Patologia Geral'),
(16, 'Farmacologia Médica'),

-- Grandes Áreas
(16, 'Clínica Médica (Medicina Interna)'),
(16, 'Cirurgia Geral'),
(16, 'Pediatria'),
(16, 'Ginecologia e Obstetrícia'),
(16, 'Medicina Geral e Familiar'),

-- Especialidades Clínicas
(16, 'Cardiologia'),
(16, 'Neurologia'),
(16, 'Psiquiatria'),
(16, 'Endocrinologia'),
(16, 'Gastroenterologia'),
(16, 'Pneumologia'),
(16, 'Nefrologia'),
(16, 'Infecciologia'),
(16, 'Reumatologia'),
(16, 'Dermatologia'),

-- Especialidades Cirúrgicas e Específicas
(16, 'Ortopedia e Traumatologia'),
(16, 'Oftalmologia'),
(16, 'Otorrinolaringologia'),
(16, 'Urologia'),
(16, 'Cirurgia Plástica'),
(16, 'Anestesiologia'),

-- Outras Especialidades e Diagnóstico
(16, 'Oncologia Médica'),
(16, 'Medicina Intensiva'),
(16, 'Medicina de Urgência'),
(16, 'Radiologia e Diagnóstico por Imagem'),
(16, 'Medicina Legal e Forense'),

-- Especialidades para Psicologia (areaId = 17)
-- Abordagens Clínicas e Teóricas
(17, 'Psicanálise'),
(17, 'Terapia Cognitivo-Comportamental (TCC)'),
(17, 'Psicologia Comportamental (Behaviorismo)'),
(17, 'Psicologia Humanista e Fenomenológica'),
(17, 'Psicologia Analítica (Junguiana)'),
(17, 'Gestalt-terapia'),

-- Áreas de Atuação e Especializações
(17, 'Psicologia Clínica'),
(17, 'Psicologia Organizacional e do Trabalho'),
(17, 'Psicologia Escolar e Educacional'),
(17, 'Psicologia Social'),
(17, 'Psicologia Hospitalar e da Saúde'),
(17, 'Psicologia Jurídica e Forense'),
(17, 'Psicologia do Esporte'),

-- Fundamentos e Avaliação
(17, 'Psicologia do Desenvolvimento'),
(17, 'Neuropsicologia'),
(17, 'Psicopatologia'),
(17, 'Avaliação Psicológica e Psicometria'),
(17, 'Orientação Vocacional e de Carreira'),

-- Especialidades para Arquitetura (areaId = 18)
-- Fundamentos e Teoria
(18, 'Projeto Arquitetônico'),
(18, 'História da Arquitetura e Urbanismo'),
(18, 'Conforto Ambiental'),
(18, 'Desenho Arquitetônico'),
(18, 'Sistemas Estruturais'),
(18, 'Materiais e Técnicas Construtivas'),

-- Áreas de Atuação
(18, 'Arquitetura de Interiores'),
(18, 'Paisagismo'),
(18, 'Urbanismo e Planejamento Urbano'),
(18, 'Restauro e Conservação de Patrimônio Histórico'),
(18, 'Gestão e Acompanhamento de Obras'),

-- Softwares e Tecnologias
(18, 'AutoCAD'),
(18, 'Revit'),
(18, 'SketchUp'),
(18, 'Archicad'),
(18, 'V-Ray'),
(18, 'Lumion'),
(18, 'Corona Renderer'),

-- Especialidades para Marketing (areaId = 19)
-- Fundamentos e Estratégia
(19, 'Marketing Estratégico'),
(19, 'Pesquisa de Mercado'),
(19, 'Branding e Posicionamento'),
(19, 'Marketing de Produto'),
(19, 'Marketing de Relacionamento (CRM)'),
(19, 'Endomarketing'),
(19, 'Trade Marketing'),

-- Marketing Digital e Performance
(19, 'Marketing Digital'),
(19, 'Inbound Marketing'),
(19, 'Marketing de Conteúdo'),
(19, 'SEO (Search Engine Optimization)'),
(19, 'Tráfego Pago'),
(19, 'Google Ads'),
(19, 'Meta Ads'),
(19, 'Gestão de Redes Sociais (Social Media)'),
(19, 'E-mail Marketing'),
(19, 'Copywriting'),
(19, 'Growth Hacking'),
(19, 'Web Analytics'),

-- Especialidades para Gastronomia (areaId = 20)
-- Fundamentos e Técnicas
(20, 'Técnicas Básicas de Cozinha'),
(20, 'Higiene e Segurança Alimentar'),
(20, 'Cortes e Preparo de Ingredientes'),
(20, 'Empratamento e Apresentação'),

-- Especialidades Culinárias
(20, 'Panificação'),
(20, 'Pastelaria e Confeitaria'),
(20, 'Chocolataria'),
(20, 'Cozinha Fria (Garde Manger)'),
(20, 'Açougue e Preparo de Carnes'),

-- Cozinhas do Mundo
(20, 'Gastronomia Brasileira'),
(20, 'Gastronomia Francesa'),
(20, 'Gastronomia Italiana'),
(20, 'Gastronomia Asiática'),
(20, 'Gastronomia Mediterrânica'),

-- Bebidas e Harmonização
(20, 'Enologia e Harmonização de Vinhos'),
(20, 'Mixologia e Cocktails'),
(20, 'Barismo e Cafés Especiais'),

-- Dietas e Tendências
(20, 'Cozinha Vegetariana e Vegana'),
(20, 'Cozinha Inclusiva (Sem Glúten e Sem Lactose)'),

-- Gestão
(20, 'Gestão de Restauração e Bares'),
(20, 'Fichas Técnicas e Precificação'),

-- Especialidades para Pedagogia (areaId = 21)
-- Áreas de Atuação e Níveis de Ensino
(21, 'Educação Infantil'),
(21, 'Anos Iniciais do Ensino Fundamental'),
(21, 'Educação de Jovens e Adultos (EJA)'),
(21, 'Educação Especial e Inclusiva'),

-- Fundamentos e Metodologias
(21, 'Didática Geral'),
(21, 'Alfabetização e Letramento'),
(21, 'Metodologias Ativas de Aprendizagem'),
(21, 'Avaliação da Aprendizagem'),
(21, 'Tecnologias Educacionais'),

-- Gestão e Apoio
(21, 'Gestão Escolar e Educacional'),
(21, 'Coordenação Pedagógica'),
(21, 'Psicopedagogia'),
(21, 'Orientação Educacional'),

-- Teoria e Fundamentos
(21, 'História da Educação'),
(21, 'Filosofia da Educação'),
(21, 'Sociologia da Educação'),

-- Especialidades para Nutrição (areaId = 22)
-- Áreas Clínicas e Ciclos de Vida
(22, 'Nutrição Clínica'),
(22, 'Nutrição Materno-Infantil'),
(22, 'Nutrição Pediátrica'),
(22, 'Nutrição Geriátrica'),
(22, 'Nutrição Hospitalar'),

-- Desporto e Estética
(22, 'Nutrição Desportiva'),
(22, 'Nutrição e Estética'),

-- Comportamento e Dietas Específicas
(22, 'Comportamento Alimentar'),
(22, 'Transtornos Alimentares'),
(22, 'Nutrição Vegetariana e Vegana'),

-- Fundamentos e Gestão
(22, 'Dietética e Planeamento Alimentar'),
(22, 'Avaliação Nutricional'),
(22, 'Nutrição em Saúde Pública'),
(22, 'Fitoterapia Aplicada à Nutrição'),
(22, 'Tecnologia dos Alimentos'),
(22, 'Gestão de Unidades de Alimentação e Nutrição (UAN)'),

-- Especialidades para Enfermagem (areaId = 23)
-- Fundamentos e Assistência Básica
(23, 'Fundamentos de Enfermagem'),
(23, 'Sistematização da Assistência de Enfermagem (SAE)'),
(23, 'Farmacologia Aplicada à Enfermagem'),

-- Especialidades Clínicas e Cirúrgicas
(23, 'Enfermagem Médico-Cirúrgica'),
(23, 'Enfermagem em Bloco Operatório e Central de Esterilização'),
(23, 'Enfermagem de Urgência e Emergência'),
(23, 'Enfermagem em Cuidados Intensivos'),
(23, 'Enfermagem Oncológica'),

-- Ciclos de Vida e Saúde Específica
(23, 'Enfermagem Pediátrica e Neonatologia'),
(23, 'Enfermagem Obstétrica e Saúde da Mulher'),
(23, 'Enfermagem Geriátrica e Gerontológica'),
(23, 'Enfermagem em Saúde Mental e Psiquiatria'),

-- Saúde Coletiva e Gestão
(23, 'Enfermagem em Saúde Pública e Comunitária'),
(23, 'Enfermagem do Trabalho'),
(23, 'Auditoria e Gestão em Enfermagem'),

-- Especialidades para Odontologia (areaId = 24)
-- Fundamentos e Diagnóstico
(24, 'Anatomia e Escultura Dental'),
(24, 'Radiologia Odontológica e Imaginologia'),
(24, 'Patologia Oral e Maxilofacial'),
(24, 'Estomatologia'),

-- Especialidades Clínicas e Cirúrgicas
(24, 'Clínica Geral Odontológica'),
(24, 'Dentística e Estética Dental'),
(24, 'Endodontia'),
(24, 'Periodontia'),
(24, 'Ortodontia'),
(24, 'Ortopedia Funcional dos Maxilares'),
(24, 'Cirurgia e Traumatologia Bucomaxilofacial'),
(24, 'Implantodontia'),

-- Prótese e Reabilitação
(24, 'Prótese Dentária'),
(24, 'Disfunção Temporomandibular e Dor Orofacial'),

-- Públicos Específicos e Novas Áreas
(24, 'Odontopediatria'),
(24, 'Odontogeriatria'),
(24, 'Odontologia para Pacientes com Necessidades Especiais'),
(24, 'Odontologia em Saúde Coletiva'),
(24, 'Harmonização Orofacial'),

-- Especialidades para Fisioterapia (areaId = 25)
-- Fundamentos e Recursos Terapêuticos
(25, 'Anatomia e Biomecânica Aplicadas'),
(25, 'Cinesiologia e Cinesioterapia'),
(25, 'Eletrotermofototerapia'),

-- Especialidades Clínicas e de Reabilitação
(25, 'Fisioterapia Traumato-Ortopédica'),
(25, 'Fisioterapia Desportiva'),
(25, 'Fisioterapia Neurofuncional'),
(25, 'Fisioterapia Cardiorrespiratória'),
(25, 'Fisioterapia em Terapia Intensiva (UTI)'),
(25, 'Fisioterapia Pélvica e Uroginecológica'),
(25, 'Fisioterapia Dermatofuncional'),

-- Ciclos de Vida
(25, 'Fisioterapia Pediátrica e Neonatal'),
(25, 'Fisioterapia Geriátrica e Gerontológica'),

-- Terapias Manuais e Práticas Específicas
(25, 'Osteopatia'),
(25, 'Quiropraxia'),
(25, 'Pilates Clínico'),
(25, 'Acupuntura Aplicada à Fisioterapia'),

-- Saúde Coletiva e Preventiva
(25, 'Fisioterapia do Trabalho e Ergonomia'),
(25, 'Fisioterapia Preventiva e Saúde Comunitária'),

-- Especialidades para Farmácia (areaId = 26)
-- Fundamentos e Ciências Farmacêuticas
(26, 'Farmacologia Básica e Clínica'),
(26, 'Farmacognosia e Botânica Aplicada'),
(26, 'Farmacocinética e Farmacodinâmica'),
(26, 'Bioquímica Clínica'),

-- Prática Clínica e Assistencial
(26, 'Farmácia Clínica e Atenção Farmacêutica'),
(26, 'Farmácia Hospitalar'),
(26, 'Farmácia Comunitária'),
(26, 'Farmácia Oncológica'),
(26, 'Toxicologia Clínica'),

-- Manipulação e Indústria
(26, 'Farmácia Magistral (Manipulação)'),
(26, 'Farmácia Industrial'),
(26, 'Farmacotécnica'),
(26, 'Cosmetologia'),
(26, 'Controlo e Garantia de Qualidade'),
(26, 'Desenvolvimento Analítico e Galénico'),

-- Outras Especialidades e Regulamentação
(26, 'Análises Clínicas e Laboratoriais'),
(26, 'Homeopatia'),
(26, 'Radiofarmácia'),
(26, 'Farmácia Estética'),
(26, 'Assuntos Regulamentares e Legislação Farmacêutica'),

(27, 'Estatística Descritiva'),
(27, 'Estatística Inferencial'),
(27, 'Análise de Séries Temporais'),
(27, 'Análise Multivariada'),
(27, 'Bioestatística'),
(27, 'Geoestatística'),
(27, 'Econometria'),
(27, 'Amostragem e Pesquisa de Mercado'),
(27, 'Planejamento de Experimentos'),
(27, 'Modelagem Preditiva'),
(27, 'Estatística Computacional'),
(27, 'Análise de Sobrevivência'),
(27, 'Teoria das Probabilidades'),
(27, 'Estatística Bayesiana'),
(27, 'Estatística Espacial'),

(28, 'Atuação e Interpretação'),
(28, 'Direção Teatral'),
(28, 'Dramaturgia'),
(28, 'Cenografia'),
(28, 'Figurino'),
(28, 'Iluminação Teatral'),
(28, 'Sonoplastia e Trilha Sonora'),
(28, 'Produção Teatral'),
(28, 'Maquiagem Cênica'),
(28, 'Teatro Musical'),
(28, 'Teatro de Bonecos e Formas Animadas'),
(28, 'Teatro de Rua'),
(28, 'Expressão Corporal e Mímica'),
(28, 'Preparação Vocal'),
(28, 'Teatro-Educação'),

(29, 'Desenho Artístico'),
(29, 'Desenho Técnico'),
(29, 'Desenho Arquitetônico'),
(29, 'Desenho de Moda'),
(29, 'Desenho Industrial'),
(29, 'Desenho Digital'),
(29, 'Ilustração Editorial'),
(29, 'Histórias em Quadrinhos e Mangá'),
(29, 'Desenho de Animação'),
(29, 'Caricatura e Cartum'),
(29, 'Desenho Botânico'),
(29, 'Desenho de Observação'),
(29, 'Concept Art e Criação de Personagens'),
(29, 'Desenho Científico'),
(29, 'Retrato e Figura Humana'),

(30, 'Pintura a Óleo'),
(30, 'Pintura Acrílica'),
(30, 'Aquarela'),
(30, 'Pintura Mural e Afresco'),
(30, 'Pintura Digital'),
(30, 'Pintura em Tela'),
(30, 'Têmpera'),
(30, 'Pintura Encaústica'),
(30, 'Pintura de Paisagem'),
(30, 'Retrato em Pintura'),
(30, 'Pintura Abstrata'),
(30, 'Pintura Figurativa'),
(30, 'Pintura Botânica'),
(30, 'Pintura em Aquarela'),
(30, 'Restauração de Pinturas'),

(31, 'Cerâmica e Olaria'),
(31, 'Bordado e Ponto Cruz'),
(31, 'Crochê e Tricô'),
(31, 'Marcenaria e Entalhe em Madeira'),
(31, 'Cestaria e Trançados'),
(31, 'Tecelagem e Tear'),
(31, 'Macramê'),
(31, 'Joalheria Artesanal e Ourivesaria'),
(31, 'Saboaria Artesanal e Cosmética Natural'),
(31, 'Trabalhos em Couro e Selaria'),
(31, 'Patchwork e Costura Criativa'),
(31, 'Encadernação Artesanal'),
(31, 'Velas Artesanais e Aromaterapia'),
(31, 'Arte em Papel e Origami'),
(31, 'Modelagem em Biscuit'),

(32, 'Móveis Planejados e Sob Medida'),
(32, 'Restauração de Móveis Antigos'),
(32, 'Marcenaria Fina'),
(32, 'Entalhe e Escultura em Madeira'),
(32, 'Tornearia em Madeira'),
(32, 'Marchetaria'),
(32, 'Luthieria'),
(32, 'Marcenaria Náutica'),
(32, 'Acabamento, Pátina e Lustração'),
(32, 'Fabricação de Brinquedos de Madeira'),
(32, 'Marcenaria Estrutural e Telhados'),
(32, 'Design e Projetos de Mobiliário'),

(33, 'Redação Publicitária e Copywriting'),
(33, 'Redação Jornalística'),
(33, 'Redação Técnica'),
(33, 'Redação Acadêmica e Científica'),
(33, 'Redação para Web e SEO'),
(33, 'Redação Criativa'),
(33, 'Redação Corporativa e Institucional'),
(33, 'UX Writing'),
(33, 'Ghostwriting'),
(33, 'Storytelling'),
(33, 'Redação para Redes Sociais'),
(33, 'Roteiro e Roteirização'),
(33, 'Revisão e Preparação de Texto'),

(34, 'Poesia'),
(34, 'Romance'),
(34, 'Conto'),
(34, 'Crônica'),
(34, 'Ensaio Literário'),
(34, 'Literatura Infantil e Juvenil'),
(34, 'Literatura Fantástica'),
(34, 'Ficção Científica'),
(34, 'Romance Policial e Suspense'),
(34, 'Biografia e Autobiografia'),
(34, 'Literatura Dramática'),
(34, 'Crítica Literária'),
(34, 'Tradução Literária'),
(34, 'Literatura Clássica'),

(35, 'Oratória Corporativa e Executiva'),
(35, 'Comunicação Não-Violenta (CNV)'),
(35, 'Técnicas de Apresentação e Pitch'),
(35, 'Retórica e Argumentação'),
(35, 'Oratória Política e Parlamentar'),
(35, 'Media Training e Relações com a Mídia'),
(35, 'Storytelling Aplicado aos Negócios'),
(35, 'Controle da Ansiedade e Fobia Social'),
(35, 'Improvisação e Técnicas de Palco'),
(35, 'Negociação e Persuasión'),
(35, 'Locução e Modulação Vocal'),
(35, 'Moderação de Painéis e Mestres de Cerimônia'),
(35, 'Debates e Diálogo Estruturado'),

(36, 'Macroeconomia'),
(36, 'Microeconomia'),
(36, 'Economia Internacional'),
(36, 'Economia do Setor Público'),
(36, 'Economia Monetária e Bancária'),
(36, 'Economia do Trabalho'),
(36, 'Economia do Desenvolvimento'),
(36, 'Economia Comportamental'),
(36, 'Economia Industrial'),
(36, 'Economia Agrícola e dos Recursos Naturais'),
(36, 'Finanças Corporativas'),
(36, 'Econometria Aplicada'),
(36, 'História Econômica'),
(36, 'Planejamento Estratégico e de Mercado'),

(37, 'Teoria de Aberturas'),
(37, 'Estratégia de Meio-Jogo'),
(37, 'Técnica de Finais'),
(37, 'Cálculo Tático'),
(37, 'Problemas e Composição de Xadrez'),
(37, 'Xadrez Rápido e Blitz'),
(37, 'Xadrez por Correspondência'),
(37, 'Xadrez às Cegas'),
(37, 'Psicologia no Xadrez'),
(37, 'História e Literatura do Xadrez'),
(37, 'Xadrez Educacional e Treinamento'),
(37, 'Softwares e Motores de Xadrez'),
(37, 'Variantes de Xadrez'),
(37, 'Arbitragem e Organização de Torneios'),

(38, 'Modelagem Orgânica'),
(38, 'Modelagem Hard Surface'),
(38, 'Texturização e Shading (Look Development)'),
(38, 'Rigging de Personagens'),
(38, 'Animação 3D'),
(38, 'Renderização e Iluminação (Lighting/Rendering)'),
(38, 'Escultura Digital (Digital Sculpting)'),
(38, 'Modelagem Arquitetônica (Archviz)'),
(38, 'Design de Produtos e CAD'),
(38, 'Modelagem para Impressão 3D'),
(38, 'Game Art e Otimização (Low Poly)'),
(38, 'VFX e Efeitos Visuais'),
(38, 'Motion Graphics 3D'),
(38, 'Pré-visualização (Previs)'),
(38, 'Fotogrametria e Escaneamento 3D'),

(39, 'Animação de Personagens (Character Animation)'),
(39, 'Animação 2D Tradicional'),
(39, 'Animação 2D Digital (Cut-out)'),
(39, 'Motion Graphics'),
(39, 'Rigging 2D e 3D'),
(39, 'Stop Motion e Claymation'),
(39, 'Animação para Jogos (Game Animation)'),
(39, 'Simulação de Efeitos Visuais (VFX e Dinâmicas)'),
(39, 'Animação Arquitetônica e Walkthrough'),
(39, 'Pós-produção e Composição Digital'),
(39, 'Storyboarding e Layout Animático'),
(39, 'Animação Facial e Blendshapes'),
(39, 'Clean-up e Assistência de Animação'),
(39, 'Direção de Animação e Produção'),

(40, 'Eletrônica Analógica'),
(40, 'Eletrônica Digital'),
(40, 'Circuitos Impressos (PCB Design)'),
(40, 'Sistemas Embarcados'),
(40, 'Microcontroladores e IoT'),
(40, 'Manutenção e Reparo de Placas'),
(40, 'Automação Industrial e CLP'),
(40, 'Robótica e Mecatrônica'),
(40, 'Eletrônica de Potência'),
(40, 'Instrumentação Eletrônica'),
(40, 'Telecomunicações e RF'),
(40, 'Audioeletrônica e Amplificadores'),
(40, 'Energia Solar e Fontes Alternativas'),
(40, 'Prototipagem e Impressão de Circuitos'),

(41, 'Robótica Móvel'),
(41, 'Robótica Industrial'),
(41, 'Robótica Humanoide'),
(41, 'Robótica Médica e Cirúrgica'),
(41, 'Visão Computacional para Robôs'),
(41, 'Cinemática e Dinâmica de Robôs'),
(41, 'Sistemas de Controle e Automação'),
(41, 'Inteligência Artificial em Robótica'),
(41, 'Drones e Veículos Aéreos Não Tripulados (VANTs)'),
(41, 'Robótica Submarina e ROVs'),
(41, 'Exoesqueletos e Próteses Robóticas'),
(41, 'Prototipagem e Impressão 3D para Robótica'),
(41, 'Robot Operating System (ROS) e Software'),
(41, 'Sensores e Atuadores');
