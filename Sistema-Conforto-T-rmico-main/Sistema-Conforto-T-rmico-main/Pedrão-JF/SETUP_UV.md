# 🔧 Configuração com UV

Se seu Python está gerenciado por `uv`, siga estes passos:

## ✅ Opção 1: Usar UV (Recomendado)

### 1. Instalar dependências
```bash
uv pip install pandas matplotlib scikit-learn pytest
```

### 2. Executar testes
```bash
cd Pedrão-JF
python run_tests.py all
```

## ✅ Opção 2: Criar Virtual Environment

### 1. Criar venv
```bash
uv venv
```

### 2. Ativar venv
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt pytest
```

### 4. Executar testes
```bash
python run_tests.py all
```

## ✅ Opção 3: Permitir Sistema Packages

Se quiser usar o Python global com `pip`:

```bash
pip install --break-system-packages -r requirements.txt pytest
```

Depois execute os testes:
```bash
python run_tests.py all
```

---

**Problema resolvido! Agora você pode rodar os testes.** 🎉
