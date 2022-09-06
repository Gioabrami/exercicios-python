# LISTA EXERCíCIOS COM LISTAS

1.  Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
2.  Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
3.  Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
4.  Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
5.  Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
6.  Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
7.  Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
8.  Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
9.  Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    <p>	&nbsp; &nbsp; &nbsp; &nbsp; "Telefonou para a vítima?"
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; "Esteve no local do crime?"
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; "Mora perto da vítima?"
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; "Devia para a vítima?"
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; "Já trabalhou com a vítima?"
    <p> O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    <p>	Mostre a quantidade de valores que foram lidos;
    <br/> Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    <br/> Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    <br/> Calcule e mostre a soma dos valores;
    <br/> Calcule e mostre a média dos valores;
    <br/> Calcule e mostre a quantidade de valores acima da média calculada;
    <br/> Calcule e mostre a quantidade de valores abaixo de sete;
    <p> Encerre o programa com uma mensagem;
16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    <p> &nbsp; &nbsp; &nbsp; &nbsp; $200 - $299
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $300 - $399
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $400 - $499
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $500 - $599
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $600 - $699
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $700 - $799
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $800 - $899
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $900 - $999
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; $1000 em diante
    <p> Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    <p> &nbsp; &nbsp; &nbsp; &nbsp; Atleta: Rodrigo Curvêllo
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Primeiro Salto: 6.5 m
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Segundo Salto: 6.1 m
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Terceiro Salto: 6.2 m
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Quarto Salto: 5.4 m
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Quinto Salto: 5.3 m

    <p> &nbsp; &nbsp; &nbsp; &nbsp; Resultado final:
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Atleta: Rodrigo Curvêllo
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Média dos saltos: 5.9 m
18. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
    <p> &nbsp; &nbsp; &nbsp; &nbsp; O total de votos computados;
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Os númeos e respectivos votos de todos os jogadores que receberam votos;
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; O percentual de votos de cada um destes jogadores;
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
    <p> Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
    <br/><br/> Enquete: Quem foi o melhor jogador?

    <p> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 9
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 10
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 9
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 10
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 11
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 10
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 50
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Informe um valor entre 1 e 23 ou 0 para sair!
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 9
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 9
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; Número do jogador (0=fim): 0

    <p> Resultado da votação:

    <p> Foram computados 8 votos.

    Jogador | Votos | %
    :---: | :--: | :---:
    9 | 4 | 50,0%
    10 | 3 | 37,5%
    11 | 1 | 12,5%
    
    <p> O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
    <p> "Qual o melhor Sistema Operacional para uso em servidores?"

    <p> As possíveis respostas são:
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 1- Windows Server
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 2- Unix
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 3- Linux
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 4- Netware
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 5- Mac OS
    <br/> &nbsp; &nbsp; &nbsp; &nbsp; 6- Outro
    <p> Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

    Sistema Operacional | Votos | %
    :------------------ | :---: | ---:
    Windows Server | 1500 | 17%
    Unix | 3500 | 40%
    Linux | 3000 | 34%
    Netware | 500 | 5%
    Mac OS | 150 | 2%
    Outro | 150 | 2%
    ----
    Total 8800

    <p> O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
    <br/> Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
    * Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
    * O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
    <br/> Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
    * O salário de cada funcionário, juntamente com o valor do abono;
    * O número total de funcionário processados;
    * O valor total a ser gasto com o pagamento do abono;
    * O número de funcionário que receberá o valor mínimo de 100 reais;
    * O maior valor pago como abono;
    <p> A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
    <br/><br/>
    Projeção de Gastos com Abono
    ============================ 
    <br/> &nbsp; &nbsp; Salário: 1000
    <br/> &nbsp; &nbsp; Salário: 300
    <br/> &nbsp; &nbsp; Salário: 500
    <br/> &nbsp; &nbsp; Salário: 100
    <br/> &nbsp; &nbsp; Salário: 4500
    <br/> &nbsp; &nbsp; Salário: 0
    <p> &nbsp; &nbsp; Salário    - Abono     
    <br/> &nbsp; &nbsp; R$ 1000.00 - R$  200.00
    <br/> &nbsp; &nbsp; R$  300.00 - R$  100.00
    <br/> &nbsp; &nbsp; R$  500.00 - R$  100.00
    <br/> &nbsp; &nbsp; R$  100.00 - R$  100.00
    <br/> &nbsp; &nbsp; R$ 4500.00 - R$  900.00
 
    <p> &nbsp; &nbsp; Foram processados 5 colaboradores
    <br/> &nbsp; &nbsp; Total gasto com abonos: R$ 1400.00
    <br/> &nbsp; &nbsp; Valor mínimo pago a 3 colaboradores
    <br/> &nbsp; &nbsp; Maior valor de abono pago: R$ 900.00
     