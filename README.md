
# 🚗 Oficina Manager Pro

![Dashboard](assets/images/dashboard.png)

> Um sistema desktop completo para gerenciamento de oficinas mecânicas, focado em organização, controle de estoque e ordens de serviço.

## 📋 Sobre o Projeto

O **Oficina Manager Pro** é uma aplicação desktop desenvolvida para auxiliar proprietários de oficinas mecânicas no controle diário de suas operações. Com uma interface moderna e escura (Dark Mode), o sistema facilita o gerenciamento de clientes, veículos, agendamentos e fluxo de caixa.

O objetivo é substituir planilhas complexas ou anotações em papel por um software intuitivo que centraliza todas as informações do negócio.

## ✨ Funcionalidades

O sistema é dividido em módulos integrados acessíveis através do Dashboard principal:

* **📊 Dashboard Interativo:** Visão geral rápida com total de clientes, veículos, agendamentos do dia e receita mensal.
* **👥 Gestão de Clientes:** Cadastro, listagem e busca rápida de clientes (Nome, Telefone, Email).
* **🚘 Gestão de Veículos:** Cadastro de carros vinculados aos clientes, incluindo placa, marca, modelo e ano.
* **📅 Agendamentos:** Controle de agenda com visualização de status (Agendado, Em andamento) e filtro por datas.
* **🔧 Catálogo de Serviços:** Lista de preços padronizada para serviços (Troca de óleo, Alinhamento, Freios, etc.).
* **📦 Controle de Estoque:** Monitoramento de peças, quantidades, valores e alertas visuais de estoque baixo.
* **📝 Ordem de Serviço (OS):** Criação de OS completa, selecionando veículo, adicionando múltiplos serviços e peças, com cálculo automático do valor total.

## 📷 Screenshots

### Dashboard e Visão Geral
[Dashboard](assets/images/dashboard.png)

### Agendamentos
Visualize os compromissos do dia e futuros, com status de execução.
![Agendamentos](assets/images/agendamentos.png)

### Controle de Estoque
Gerencie peças, veja valores unitários e monitore quantidades mínimas.
![Estoque](assets/images/estoque.png)

### Gestão de Veículos e Clientes
Mantenha o banco de dados da oficina organizado.
![Veículos](assets/images/veiculos.png)
![Clientes](assets/images/clientes.png)

### Serviços
Tabela de preços e serviços cadastrados.
![Serviços](assets/images/servicos.png)

### Criação de Ordem de Serviço
Interface unificada para lançar serviços e peças em um atendimento.
![Nova OS](assets/images/nova_os.png)

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica (GUI):** CustomTkinter (Baseado nas imagens)
* **Banco de Dados:** SQLite (Provável, para armazenamento local)
* **Manipulação de Imagens:** Pillow (PIL)

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.

### Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/RegisnaldoJunior/oficina_aap.git](https://github.com/RegisnaldoJunior/oficina_aap.git)
Entre na pasta do projeto:

Bash

cd oficina_aap
Instale as dependências (recomenda-se usar um ambiente virtual):

Bash

pip install -r requirements.txt
(Caso não tenha o arquivo requirements.txt, instale as bibliotecas principais manualmente, ex: pip install customtkinter pillow)

Execute a aplicação:

Bash

python main.py
(Substitua main.py pelo nome do seu arquivo principal, caso seja diferente)


📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Regisnaldo Junior


Com certeza\! Com base nas imagens da interface (que sugerem fortemente o uso de Python com uma biblioteca de interface gráfica moderna, provavelmente **CustomTkinter**, devido ao visual "dark mode" e botões arredondados) e nas funcionalidades apresentadas, elaborei um `README.md` completo e profissional.

Você pode copiar o código abaixo e criar o arquivo no seu repositório.

-----

