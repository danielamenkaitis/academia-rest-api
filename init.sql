-- Active: 1759877895901@@127.0.0.1@5432@gym
-- Active: 1759877895901@@127.0.0.1@5432@fit
--CREATE DATABASE gym;

CREATE TABLE Treino (
  id serial not null primary key,
  treino varchar (100) not null,
  instrucao varchar (500) not null,
  dataCadastro timestamp default current_timestamp,
  ativo char (1) default 'S',
  idUsuario integer NOT NULL 
);

CREATE table Aluno (
    id serial not null primary key,
    nome varchar (100),
    email varchar (100),
    whatsapp varchar (100),
    observacao varchar (500),
    dataCadastro timestamp default current_timestamp,
    ativo char (1) default 'S',
    idUsuario integer NOT NULL
);

CREATE table exercicio (
    id serial not null primary key,
    nomeExercicio varchar (100),
    instrucao varchar (500),
    url varchar (2048),
    dataCadastro timestamp default current_timestamp,
    ativo char (1) default 'S',
    idUsuario integer NOT NULL
);

CREATE table usuario (
    id serial not null primary key,
    usuario varchar (100),
    senha varchar (50),
    tipo varchar (10),
    dataCadastro timestamp default current_timestamp,
    ativo char (1) default 'S',
    idUsuario integer NOT NULL
);

CREATE table treinoAluno (
    id serial not null primary key,
    idTreino integer NOT NULL, FOREIGN KEY(idTreino) REFERENCES treino(id),
    idAluno integer NOT NULL, FOREIGN KEY(idAluno) REFERENCES aluno(id),
    dataCadastro timestamp default current_timestamp,
    ativo char (1) default 'S',
    idUsuario integer NOT NULL
);

CREATE table treinoExercicio (
    id serial not null primary key,
    idTreino integer NOT NULL, FOREIGN KEY(idTreino) REFERENCES treino(id),
    idExercicio integer NOT NULL, FOREIGN KEY(idexercicio) REFERENCES exercicio(id),
    dataCadastro timestamp default current_timestamp,
    ativo char (1) default 'S',
    idUsuario integer NOT NULL
);

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








