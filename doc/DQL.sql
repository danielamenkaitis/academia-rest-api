SELECT * FROM USUARIO;

SELECT * FROM ALUNO;

SELECT * FROM EXERCICIO;

SELECT 
    a.nomeexercicio
    ,a.instrucao
    ,a.url
    ,a.datacadastro
    ,a.ativo    
    ,a.idusuario
FROM EXERCICIO as a
WHERE ativo= 'S' and a.id = a.id;

SELECT * FROM TREINO;

SELECT 
    a.id
    ,a.treino
    ,a.instrucao
    ,a.datacadastro
    ,a.ativo
    ,a.idusuario
FROM TREINO as a
WHERE ativo= 'S' and a.id = a.id;

SELECT 
    a.id
    ,a.nome
    ,a.email
    ,a.whatsapp
    ,a.observacao
    ,a.datacadastro
    ,a.ativo
    ,a.idusuario
FROM ALUNO as a
where a.id = a.id

SELECT
    a.id
    ,a.nome
    ,b.id as idtreino
    ,b.treino
    ,b.idusuario
    ,a.ativo
FROM ALUNO as a
inner join treino as b on a.id = b.id
where a.ativo = 'S'

SELECT
    a.id
    ,c.nome
    ,b.treino
    ,b.instrucao as grupo_muscular
    ,e.nomeexercicio
    ,e.instrucao
    ,e.url
    ,d.usuario    
FROM treinoAluno as a
inner join treino as b on a.id = b.id
inner join aluno as c on a.id = c.id
inner join usuario as d on a.id = d.id
inner join exercicio as e on a.id = e.id
where a.ativo = 'S'

SELECT * FROM treino

SELECT * FROM treinoExercicio

SELECT * FROM treinoaluno;
SELECT
    b.id
    ,b.nome
    ,c.instrucao as grupomuscular
    ,a.idtreino
    ,c.treino
    ,d.nomeexercicio
    ,d.instrucao
    ,d.url
FROM treinoaluno as a 
INNER JOIN ALUNO as b on a.id = b.id
INNER JOIN treino as c on a.id = c.id
INNER JOIN exercicio as d on a.id = d.id