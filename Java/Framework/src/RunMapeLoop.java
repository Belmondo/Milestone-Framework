import models.NFRDefinition;

import java.util.ArrayList;
import java.util.List;

public class RunMapeLoop {


    List<NFRDefinition> NFRImplemented = new ArrayList<>();

    public void addNFR(NFRDefinition nfr){
        NFRImplemented.add(nfr);
    }

    public void runMapeLoop(){
        
    }

    private void prepareMapeLoop(){}


}


/*
 * 
 * 
 * 
 * SQuaRE (Software product Quality Requirements and Evaluation), define um modelo de qualidade de software 
 * que inclui vários requisitos não-funcionais.

Usabilidade: se refere à facilidade de uso do software pelo usuário final. 
Inclui características como facilidade de aprendizado, eficiência de uso, 
facilidade de memorização, prevenção de erros e satisfação do usuário.

Confiabilidade: se refere à capacidade do software de desempenhar suas funções 
corretamente em diferentes condições de uso e manter o desempenho esperado ao longo do tempo. 
Inclui características como tolerância a falhas, capacidade de recuperação, manutenibilidade e 
confiabilidade de desempenho.

Desempenho: se refere à capacidade do software de responder de forma rápida e eficiente às solicitações 
do usuário, mesmo sob carga máxima de trabalho. Inclui características como tempo de resposta, velocidade 
de processamento, escalabilidade e capacidade de gerenciamento de recursos.

Segurança: se refere à capacidade do software de proteger informações e dados sensíveis 
contra acesso não autorizado, perda ou roubo. Inclui características como autenticação, 
autorização, criptografia, integridade de dados e conformidade com normas e regulamentações de segurança.

Portabilidade: se refere à capacidade do software de ser executado em diferentes plataformas e 
ambientes sem a necessidade de modificação significativa. Inclui características como compatibilidade 
com sistemas operacionais, suporte a diferentes linguagens de programação e bibliotecas, e facilidade 
de instalação e configuração.

Manutenibilidade: se refere à facilidade com que o software pode ser modificado, adaptado ou 
corrigido após o lançamento. Inclui características como modularidade, facilidade de compreensão
 do código-fonte, facilidade de teste e documentação adequada.

Eficiência: se refere à capacidade do software de utilizar efetivamente os recursos disponíveis, 
como processador, memória e espaço em disco. Inclui características como uso eficiente de memória, 
tempo de inicialização e uso de recursos de rede.
 */

 /* 

 Principais métricas 


Usabilidade:
1. Taxa de erros: mede a frequência de erros cometidos pelo usuário durante o uso do software.
2. Tempo de aprendizado: mede o tempo necessário para o usuário aprender a usar o software.
3. Satisfação do usuário: mede a satisfação do usuário com o software por meio de pesquisas de satisfação.

Confiabilidade:
1. Tempo médio entre falhas (MTBF): mede o tempo médio entre falhas do software.
2. Taxa de falhas: mede a frequência de falhas do software em um determinado período de tempo.
3. Tempo médio de recuperação (MTTR): mede o tempo médio necessário para o software se recuperar após uma falha.

Desempenho:
1. Tempo de resposta: mede o tempo necessário para o software responder às solicitações do usuário.
2. Taxa de transferência: mede a quantidade de dados que podem ser transferidos por unidade de tempo.
3. Utilização de recursos: mede a quantidade de recursos do sistema (como CPU e memória) utilizados pelo software.

Segurança:
1. Taxa de sucesso de autenticação: mede a frequência de sucesso na autenticação do usuário.
2. Taxa de sucesso de autorização: mede a frequência de sucesso na autorização do usuário.
3. Tempo médio para identificação e resposta a incidentes de segurança: mede o tempo médio necessário para identificar e responder a incidentes de segurança.

Portabilidade:
1. Grau de compatibilidade: mede o grau de compatibilidade do software com diferentes plataformas e sistemas operacionais.
2. Esforço de adaptação: mede o esforço necessário para adaptar o software a diferentes plataformas e sistemas operacionais.
3. Grau de conformidade: mede o grau de conformidade do software com as normas e padrões de portabilidade.

Manutenibilidade:
1. Taxa de defeitos encontrados: mede a frequência de defeitos encontrados durante a manutenção do software.
2. Tempo de correção de defeitos: mede o tempo médio necessário para corrigir defeitos encontrados.
3. Grau de modularidade: mede o grau de modularidade do software, ou seja, a facilidade de modificar partes específicas do software sem afetar outras partes.

Eficiência:
1. Tempo de resposta: mede o tempo necessário para o software responder às solicitações do usuário.
2. Utilização de recursos: mede a quantidade de recursos do sistema (como CPU e memória) utilizados pelo software.
3. Taxa de transferência: mede a quantidade de dados que podem ser transferidos por unidade de tempo.
  * 

  */
