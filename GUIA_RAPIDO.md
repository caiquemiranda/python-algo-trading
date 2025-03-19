# Guia Rápido - Python Algo Trading

Este guia fornece instruções rápidas para começar a utilizar o projeto Python Algo Trading.

## Instalação Rápida

### Opção 1: Instalação Local

1. Certifique-se de ter Python 3.7+ instalado
2. Instale o MetaTrader 5 em seu computador
3. Clone o repositório
4. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Opção 2: Usando Docker

```bash
docker build -t python-algo-trading .
docker run -it -p 8888:8888 python-algo-trading
```

## Primeiros Passos

### 1. Configurar o MetaTrader 5

1. Abra o MetaTrader 5
2. Configure uma conta demo ou real
3. Faça login na plataforma

### 2. Testar a Conexão

Execute o script básico para verificar se a conexão está funcionando:

```bash
python 00-initialize_mt5.py
```

### 3. Verificar Informações da Conta

```bash
python 01-informacoes_conta_mt5.py
```

### 4. Explorar os Dados de Mercado

```bash
python 06-coleta_ativos_olhc_mt5.py
```

## Estratégias Disponíveis

1. **Cruzamento de Médias**
   - Arquivo: `09-backtest_cruzamento_media_mt5.py`
   - Descrição: Estratégia que opera baseada no cruzamento de médias móveis

2. **Compra na Queda**
   - Arquivo: `11-estrategia_compra_queda_yfinance.py`
   - Descrição: Estratégia que busca comprar ativos após quedas significativas

## Execução de Ordens

Para executar ordens automaticamente:

```bash
python 12-envio_ordem_mt5.py
```

Para fechar ordens:

```bash
python 13-ordem_fechamento_mt5.py
```

## Modelos Preditivos

O projeto inclui diversos modelos preditivos:

1. **Prophet**
   - Arquivo: `14-previ_prophet.py`
   - Uso: Previsão de séries temporais

2. **Regressão Linear**
   - Arquivo: `15-regressao_linear.py`
   - Uso: Previsão de preços baseada em regressão linear

3. **Redes Neurais**
   - Arquivo: `16-rede_neural.py`
   - Uso: Previsão avançada de preços usando redes neurais

## Notebooks Jupyter

Para uma experiência interativa, use os notebooks:

```bash
jupyter notebook
```

## Dicas e Boas Práticas

1. **Sempre comece com contas demo** para testar suas estratégias
2. **Monitore constantemente** a execução de scripts automáticos
3. **Verifique os parâmetros** antes de executar estratégias (stop loss, take profit)
4. **Mantenha um diário de trading** para avaliar o desempenho
5. **Faça backtests extensivos** antes de usar dinheiro real

## Próximos Passos

1. Explore os notebooks para entender cada estratégia
2. Faça ajustes nos parâmetros para melhorar o desempenho
3. Combine diferentes estratégias
4. Desenvolva suas próprias estratégias baseadas nos modelos fornecidos

## Recursos Adicionais

- [Documentação do MetaTrader 5 para Python](https://www.mql5.com/en/docs/python_metatrader5)
- [Fórum MQL5](https://www.mql5.com/en/forum)
- [Documentação do pandas](https://pandas.pydata.org/docs/)
- [Documentação do scikit-learn](https://scikit-learn.org/stable/documentation.html) 