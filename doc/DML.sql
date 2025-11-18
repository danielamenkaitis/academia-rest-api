INSERT INTO usuario(usuario, senha,tipo, idusuario)
VALUES
('admin', '1234', 'admin', '1'),
('Francisco_Jr', '1234', 'personal', '2'),
('Daniela_Fernandes', '1234', 'aluno', '3');

INSERT INTO treino (treino, instrucao, idUsuario)
VALUES 
('Treino 1', 'MMII / QUADRICEPS / PANTURRILHAS', '2');

INSERT INTO aluno (nome, email, whatsapp, observacao, idUsuario)
VALUES
('Daniela Fernandes', 'email@email.com', '1199999-9999', 'Restrição médica', '1');

INSERT INTO exercicio (nomeExercicio, instrucao, url, idUsuario)
VALUES
('Leg Press', '3x8 com carga adaptada descanso de 2 minutos em cada série', 'https://www.youtube.com/shorts/OlWE5rOjS5o?feature=share', 1);

INSERT into treinoAluno (idtreino, idaluno, idusuario)
VALUES
('1', '1', '1');

INSERT INTO treinoExercicio (idtreino, idexercicio, idusuario)
VALUES (1, 1, 2);





