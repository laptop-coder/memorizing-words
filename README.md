# Запоминание слов

## Деплой на Linux-сервер

### Зависимости

- `curl`
- `docker`
- `vi`

### Команды

```
mkdir ./memorizing-words
cd ./memorizing-words
curl https://raw.githubusercontent.com/laptop-coder/memorizing-words/refs/heads/main/.env.example > ./.env
vi ./.env
docker run -d --env-file=./.env --restart=always laptopcoder/memorizing-words:latest
```

## Источник

Слова взяты из толкового словаря живого великорусского языка В. И. Даля
