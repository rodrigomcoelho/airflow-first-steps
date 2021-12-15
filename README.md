# Primeiros passos com Apache Airflow
Esse diretório contém passos básicos para subir uma versão básica do airflow.

Criar o Ambiente Virtual
```zsh
make create-env
```

Configurar o Airflow com Docker
```zsh
make airflow-init
```

Iniciar o Airflow:
```zsh
make airflow-start
```

Instalar libs do Airflow no ambiente virtual
```zsh
install-airflow-lib
```

Limpar tudo
```zsh
clean-up
```
