# bancodado

#ESCOPO
Qualquer farmácia pode aproveitar dos
benefícios de um banco de dados, desde grandes redes farmacêuticas, até
farmácias de manipulação que atendem em pequena escala, farmácias de
postos públicos de sáude podem usar o mesmo sistema, se não possuir fins
lucrativos, apenas deverá ser alterados a questão de preços nos itens
supracitados que deverá ser removida.

Usando: MySQL, SqlClient, SqlAlchemy, Bycrypt, Uvicorn, FastAPI, Python, gerenciando o banco de dados por phpmyadmin

#PROBLEMA
Uma farmácia deve possuir um controle
preciso do estoque, devido a possuir itens de diversas naturezas e tarjas, ou
dependendo da farmácia, manipular drogas reais previamente autorizadas pela
Anvisa sob prescrição médica e autorização de uso para pacientes de doenças
terminais incuráveis. Controlar os mesmos usando banco de dados eficiente
garante uma segurança na manipulação e distribuição de medicamentação
tarjada.

Obstante ao supracitado, sendo um local onde se comercializa produtos
de outras naturezas (aquém de medicamentos) o mesmo facilita o controle do
estoque e faturamento separamente de cada unidade de uma rede
farmacêutica, podendo ser então reportado com mais facilidade para a matriz,
a qual também pode usar um banco de dados para registrar todas as
operações executadas pelas filiais, caso que atualmente, não há uma
implementação formal devido a custos com banco de dados pagos.

#SOLUÇÃO

Implementar um sistema de banco de dados que
permita ser usado em cada farmácia individualmente para controle de todas as
ações básicas que requerem para o bom funcionamento da loja. O sistema
deve preferencialmente conter:

CRUD de cliente (4 funcionalidades);
CRUD de cliente preferencial (4 funcionalidades);
CRUD de funcionários (4 funcionalidades);
CRUD de fornecedores (4 funcionalidades);
CRUD de produtos não medicamentosos (4 funcionalidades);
CRUD de produtos medicamentosos (4 funcionalidades);
