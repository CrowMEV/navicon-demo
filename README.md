# Navicon demo

## Настройка проекта

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -r requirements.txt
```

## Запуск тестов

```bash
pytest
```

с отчётом о покрытие

```bash
pytest --cov=app
```

полезные флаги для запуска pytest

```
--tb=[auto/long/short/line/native/no]: Управляет стилем трассировки.
-v / --verbose: Отображает все имена тестов, пройденных или не пройденных.
-l / --showlocals: Отображает локальные переменные рядом с трассировкой стека.
-lf / --last-failed: Запускает только тесты, которые завершились неудачей.
-x / --exitfirst: Останавливает тестовую сессию при первом сбое.
--pdb: Запускает интерактивный сеанс отладки в точке сбоя.
```