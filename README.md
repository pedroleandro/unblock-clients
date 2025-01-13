# Unblock Clients Project

<p align="justify">
Esse é um projeto que executa um script em python para desbloquear clientes inadimplentes do Sistema TOTVS WinThor
</p>

## Instalação

### 1. Clone o repositório

Primeiro, clone o repositório para o seu computador:

```bash
git clone https://github.com/pedroleandro/unblock-clients.git
cd unblock-clients
```

### 2. Crie um arquivo .env

Copie e cole o arquivo .env-example e renomei para .env
```bash
cp .env-example .env
```
Adicione as credenciais do banco de dados no arquivo .env

```bash
# Configuração do Banco de Dados
DB_USER=your_user
DB_PASSWORD=yout_pass
DB_HOST=your_host
DB_PORT=port
DB_SERVICE_NAME=_service_name
```
### 3. Construa a imagem Docker

```bash
docker-compose build
```

### 4. Execute o container

```bash
docker-compose up
```

O script será executado automaticamente, registrando logs no arquivo app.log.

Esse `README.md` combina todas as etapas necessárias, desde a instalação até a execução do projeto, em um único arquivo. Ele fornece informações claras sobre como configurar e rodar o projeto, incluindo a solução de problemas e o uso de dependências.

<hr style="border: 3px solid gray; border-radius: 10px;">

## <div style="text-align: center;">Desenvolvido por</div>

<div style="display: flex; align-items: center; justify-content: space-around;">
  <div style="text-align: center;">
    <img src="https://github.com/pedroleandro.png" width="150" height="150" style="border-radius: 50%;"/>
    <p><strong>Pedro Leandro Gomes da Silva</strong></p>
    <a href="https://github.com/pedroleandro" target="_blank">GitHub</a>
  </div>
</div>







