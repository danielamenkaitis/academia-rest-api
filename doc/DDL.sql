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
)


