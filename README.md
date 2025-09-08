Monitoramento Automatizado de Preços - Estante Virtual
<br>

Este projeto é uma solução de automação de ponta a ponta para rastrear e registrar preços de livros no site Estante Virtual. Ele transforma um processo manual e tedioso em um fluxo de trabalho autônomo, confiável e escalável, demonstrando a aplicação prática de web scraping e infraestrutura em nuvem.

O Problema Proposto
O monitoramento manual de preços em e-commerces como o Estante Virtual é ineficiente e propenso a falhas, tornando-o inviável para análises de longo prazo. A necessidade era de uma ferramenta que pudesse coletar dados de preços de forma consistente, sem intervenção humana, e armazená-los em um local centralizado para futuras consultas e análises.

Solução Implementada
O projeto foi construído sobre uma arquitetura de três camadas que garante a coleta, persistência e automação contínua dos dados.

1. Coleta de Dados (Python e Web Scraping)
O coração da solução é um script em Python que utiliza as bibliotecas requests e BeautifulSoup para navegar até as páginas de produtos da Estante Virtual e extrair informações críticas, como o título do livro e o preço. A lógica foi desenvolvida para ser robusta, lidando com a estrutura de dados do site de forma eficiente e confiável.

2. Persistência de Dados (Firebase Firestore)
Os dados coletados são imediatamente enviados para um banco de dados NoSQL, o Firebase Firestore. Essa escolha permitiu armazenar os preços junto com um timestamp de forma simples e flexível, sem a necessidade de um esquema rígido. O Firebase serve como a fonte de verdade centralizada, tornando os dados acessíveis para monitoramento e análise.

3. Infraestrutura e Automação (Google Cloud)
Para garantir que o processo seja totalmente autônomo, o script foi implantado em uma máquina virtual (VM) na Google Cloud Platform (GCP). A execução é agendada em horários pré-determinados utilizando um cron job. Esta abordagem assegura que a automação opere 24/7 de forma confiável, sem depender de uma máquina local, demonstrando meu conhecimento em infraestrutura e serviços de nuvem.

Habilidades Demonstradas
Linguagens de Script: Proficiência em Python para automação de tarefas.

Web Scraping: Habilidade em coletar dados de websites de forma programática.

Integração de APIs: Experiência em conectar e gerenciar serviços de terceiros (Firebase) via APIs.

Banco de Dados: Conhecimento de bancos de dados NoSQL e sua aplicação prática para dados não estruturados.

DevOps e Infraestrutura em Nuvem: Noções de implantação e agendamento de tarefas em ambientes de produção com Google Cloud e Shell Scripting (cron).

Resolução de Problemas: Adaptação do projeto para uma nova fonte de dados após o bloqueio inicial.

Como Executar
Clone este repositório.

Instale as dependências com pip install -r requirements.txt.

Configure as credenciais do Firebase.

Execute o script Python.
