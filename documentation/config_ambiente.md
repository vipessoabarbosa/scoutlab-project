# Manual de Configuração do Ambiente ScoutLab

Este manual fornece um guia passo a passo para configurar o ambiente de desenvolvimento do projeto ScoutLab, um sistema de análise estatística de futebol focado em métricas individuais de jogadores. O guia está organizado em ordem cronológica de execução, garantindo uma configuração adequada do ambiente.

## 1. Pré-requisitos
- Python 3.10.9
- VS Code 1.96.2
- Windows 10

## 2. Estrutura de Diretórios

**Criar Diretório Base**
```bash
cd "E:\Desenvolvimento Profissional\Data Science\Python\Projetos"
mkdir 01_scoutlab-project
cd 01_scoutlab-project
```

**Criar Estrutura Principal**
```bash
mkdir data
mkdir documentation
mkdir notebooks
mkdir scripts
mkdir tests
mkdir config
mkdir logs

mkdir data\raw
mkdir data\processed
mkdir data\raw\fbref
mkdir data\raw\whoscored

mkdir documentation\project
mkdir documentation\technical
mkdir documentation\analysis
```

## 3. Ambiente Virtual e Dependências

**Criar e Ativar Ambiente**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Instalar Bibliotecas**
```bash
pip install soccerdata pandas numpy matplotlib seaborn plotly
pip install black flake8 pylint isort
pip freeze > requirements.txt
```

## 4. Configuração do Git

**Configurar Identidade**
```bash
git init
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

**Criar .gitignore**
```text
# Ambiente virtual
venv/
__pycache__/
*.py[cod]

# VS Code
.vscode/

# Arquivos de ambiente
.env

# Dados e logs
*.csv
*.xlsx
*.sqlite
*.log

# Jupyter
.ipynb_checkpoints
```

## 5. Configuração do VS Code

**1. Instalar Extensões**
- Python (Microsoft)
- Pylance
- Jupyter
- Python Indent
- autoDocstring
- Python Test Explorer
- Git Graph
- GitLens
- Rainbow CSV
- Material Icon Theme

**2. Configurar Workspace**
Criar `.vscode/settings.json`:
```json
{
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100],
    "editor.renderWhitespace": "all",
    "editor.minimap.enabled": true,
    "editor.wordWrap": "on",
    "files.trimTrailingWhitespace": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,

    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": true,

    "jupyter.notebookFileRoot": "${workspaceFolder}",
    "jupyter.askForKernelRestart": false,

    "[python]": {
        "editor.formatOnType": true,
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

## 6. Verificação da Instalação

**Criar test_setup.py**
```python
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import soccerdata

print(f"Python version: {sys.version}")
print(f"Matplotlib version: {plt.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Seaborn version: {sns.__version__}")
print(f"Plotly version: {plotly.__version__}")
print(f"Soccerdata version: {soccerdata.__version__}")
```

## 7. Primeiro Commit

```bash
git add .
git commit -m "Configuração inicial do projeto"
git remote add origin https://github.com/seu-usuario/scoutlab-project.git
git push -u origin main
```