******** Campo Minado em Python Versão com Chamadas RPC/RMI ********
** Rubens Aguiar - 1727555 - Sistemas Distribuidos		 ***
** Data: 19/10/2017						 ***
********************************************************************

Para rodar o campo_minado versao RPC/RMI, basta
executar o "campo_minado_servidor_rpyc.py" e em seguida
testar com o "campo_minado_view_rpyc.py". Caso o servidor
e o cliente estejam em micros diferentes, é preciso
adicionar o IP do servidor em ambos os arquivos na
variavel "HOST", no caso do servidor o arquivo "campo_minado_negocio.py"
também precisa estar no mesmo micro do sevidor.

O arquivo "campo_minado_negocio.py" foi reajustado para melhor
atender a forma de execução RPC/RMI, sendo no seu inicio
verificado se está sendo criado um Novo Jogo ou se a linha e coluna
passadas possuem valor "0" indicando carregamento de um jogo
anterior.