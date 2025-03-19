# Instruções para Uso do Docker

Este documento fornece instruções detalhadas para executar o projeto Python Algo Trading usando Docker.

## Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop) instalado em seu sistema
- Conhecimento básico de comandos Docker
- MetaTrader 5 instalado localmente (para algumas funcionalidades)

## Construindo a Imagem Docker

1. Abra um terminal na pasta raiz do projeto
2. Execute o comando para construir a imagem:

```bash
docker build -t python-algo-trading .
```

Este processo pode levar alguns minutos, pois o Docker irá instalar todas as dependências necessárias.

## Executando o Container

### Modo Jupyter Notebook

Para iniciar o container com o Jupyter Notebook:

```bash
docker run -it -p 8888:8888 -v $(pwd)/data:/app/data python-algo-trading
```

No Windows, use:

```bash
docker run -it -p 8888:8888 -v %cd%/data:/app/data python-algo-trading
```

Este comando:
- Mapeia a porta 8888 do container para a porta 8888 do host
- Cria um volume que conecta a pasta `data` local com a pasta `/app/data` no container
- Inicia o servidor Jupyter Notebook

Após executar este comando, copie o URL com o token gerado e cole-o em seu navegador para acessar o Jupyter Notebook.

### Modo Interativo (Shell)

Para acessar um shell dentro do container:

```bash
docker run -it python-algo-trading /bin/bash
```

Este modo é útil para executar scripts individuais ou para depuração.

## Limitações do Docker

É importante notar que há limitações ao executar o MetaTrader 5 dentro de um container Docker:

1. Autenticação: O MT5 no Docker pode ter dificuldades para autenticar-se com os servidores da corretora.
2. Interface gráfica: O Docker não fornece uma interface gráfica, então o MT5 funcionará principalmente em modo terminal.
3. Dados em tempo real: Algumas funcionalidades de dados em tempo real podem não funcionar como esperado.

## Solução Alternativa

Uma abordagem melhor pode ser:

1. Instalar o MetaTrader 5 localmente no seu sistema
2. Executar os scripts Python no Docker, configurando-os para se conectar ao MT5 instalado localmente
3. Para isso, você precisará garantir que as portas corretas estejam abertas e acessíveis

## Exemplos de Uso

### Executar um script específico:

```bash
docker run -it python-algo-trading python 00-initialize_mt5.py
```

### Executar um notebook específico:

```bash
docker run -it -p 8888:8888 python-algo-trading jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root /app/notebook-01.ipynb
```

## Problemas Comuns

1. **Erro de conexão com o MetaTrader 5**: Verifique se o MT5 está instalado corretamente no container ou considere usar o MT5 local.
2. **Erro de permissões ao salvar arquivos**: Verifique se o volume está montado corretamente e se você tem permissões de escrita.
3. **Container para de responder**: Pode ser necessário aumentar os recursos alocados ao Docker no seu sistema host.

## Limpeza

Para remover containers parados:

```bash
docker container prune
```

Para remover a imagem criada:

```bash
docker image rm python-algo-trading
``` 