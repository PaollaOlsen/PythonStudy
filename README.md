# PythonStudy

Repositório criado para os estudos de python

## Como instalar o virtualenv

Para instalar o virtualenv, execute o seguinte comando:

```bash
sudo apt install virtualenv
```

## Criando o ambiente

Para criar um ambiente específico para sua aplicação utilizando o virtualenv, execute o seguinte comando: 

```bash
virtualenv -p python3.8 env
```

## Como ativar o virtualenv

Dentro do repositório, execute o seguinte comando:

```bash
source env/bin/activate
```

Para sair do virtualenv atual, utilize o seguinte comando:

```bash
deactivate
```

## Como executar o programa em Python

Para executar o programa em Python, execute o seguinte comando:

```bash
python caminhodoarquivo.py
```



**Comando úteis:**
`which python3.8`: retorna o local onde o python está instalado
`python --version`: retorna a versão do python 
`python`: executa o python permitindo que se possa testar pequenos códigos direto no terminal, para sair digite `exit()`
