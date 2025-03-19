# Python Algo Trading

## Visão Geral
Este repositório contém um conjunto de scripts Python para trading algorítmico usando a API MetaTrader 5. O projeto oferece diversas funcionalidades, desde a conexão com a plataforma MetaTrader 5 até a implementação de estratégias de trading automatizadas, backtesting e uso de modelos de aprendizado de máquina para previsão de mercado.

## Estrutura do Projeto
O projeto está organizado em diversos arquivos que representam diferentes funcionalidades:

### Configuração e Conexão
- `00-initialize_mt5.py` - Inicialização básica da conexão com o MetaTrader 5
- `01-informacoes_conta_mt5.py` - Obtém informações da conta do usuário

### Coleta de Dados
- `02-ativos_mt5.py` a `08-dados_investpy.py` - Scripts para coleta de dados de ativos, informações de mercado, preços OHLC e dados em tempo real

### Backtesting e Estratégias
- `09-backtest_cruzamento_media_mt5.py` - Backtest da estratégia de cruzamento de médias
- `10-rebaixamento_estrategia_cruzamento_media_mt5.py` - Análise de rebaixamento para estratégia de cruzamento
- `11-estrategia_compra_queda_yfinance.py` - Estratégia de compra na queda com dados do Yahoo Finance

### Execução de Ordens
- `12-envio_ordem_mt5.py` - Script para envio de ordens de compra e venda
- `13-ordem_fechamento_mt5.py` - Script para fechamento de ordens

### Análise Preditiva
- `14-previ_prophet.py` - Previsão usando Facebook Prophet
- `15-regressao_linear.py` - Implementação de modelos de regressão linear
- `16-rede_neural.py` - Implementação de redes neurais para previsão

### Notebooks
- `notebook-01.ipynb` a `notebook-04.ipynb` - Jupyter notebooks com análises e exemplos práticos

## Requisitos
- Python 3.7+
- MetaTrader 5 instalado e configurado
- Conta em uma corretora compatível com MetaTrader 5
- Bibliotecas Python listadas em requirements.txt

## Instalação

### Usando pip
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-algo-trading.git
cd python-algo-trading

# Instale as dependências
pip install -r requirements.txt
```

### Usando Docker
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-algo-trading.git
cd python-algo-trading

# Construa a imagem Docker
docker build -t python-algo-trading .

# Execute o container
docker run -it python-algo-trading
```

## Configuração

1. Instale o MetaTrader 5 em seu computador
2. Configure sua conta em uma corretora compatível
3. Faça login na plataforma MetaTrader 5
4. Execute os scripts conforme sua necessidade

## Uso

### Exemplos Básicos

1. Inicializar conexão com MetaTrader 5:
```bash
python 00-initialize_mt5.py
```

2. Verificar informações da conta:
```bash
python 01-informacoes_conta_mt5.py
```

3. Executar uma estratégia de trading:
```bash
python 12-envio_ordem_mt5.py
```

### Executando Backtests

```bash
python 09-backtest_cruzamento_media_mt5.py
```

### Usando Modelos Preditivos

```bash
python 15-regressao_linear.py
```

## Notas Importantes

- Certifique-se de que o MetaTrader 5 esteja em execução antes de rodar os scripts
- Entenda completamente as estratégias antes de executá-las com dinheiro real
- Comece com pequenas quantidades para testar o funcionamento do sistema
- Sempre monitore a execução dos scripts de trading automatizado

## Aviso de Risco

O trading algorítmico envolve riscos significativos. Este código é fornecido apenas para fins educacionais e de pesquisa. Não recomendamos o uso destes scripts para trading real sem uma compreensão completa do mercado e dos riscos envolvidos. O autor não se responsabiliza por quaisquer perdas financeiras decorrentes do uso deste software.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
