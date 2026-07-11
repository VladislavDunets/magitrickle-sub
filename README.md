# MagiTrickle Subscriptions

Готовые подписки для MagiTrickle 0.7.0+.

Каждый файл в каталоге `subscriptions/` — обычный текстовый список:
- один домен, IP или подсеть на строку;
- строки, начинающиеся с `#`, считаются комментариями;
- MagiTrickle автоматически определяет тип правила;
- дубликаты удаляются при генерации.

## Быстрый старт

1. Откройте нужный файл в GitHub.
2. Нажмите **Raw**.
3. Скопируйте адрес.
4. В MagiTrickle откройте раздел подписок.
5. Добавьте URL и выберите нужную группу маршрутизации.

После публикации репозитория URL будет выглядеть так:

```text
https://raw.githubusercontent.com/USERNAME/magitrickle-sub/main/subscriptions/ai/openai.txt
```

Замените `USERNAME` на свой GitHub-логин.

## Готовые наборы

### AI
- `ai/openai.txt`
- `ai/anthropic.txt`
- `ai/google-ai.txt`
- `ai/perplexity.txt`
- `ai/all-ai.txt`

### Разработка
- `dev/github.txt`
- `dev/docker.txt`
- `dev/jetbrains.txt`
- `dev/cursor.txt`
- `dev/all-dev.txt`

### Медиа
- `media/youtube.txt`
- `media/twitch.txt`
- `media/spotify.txt`
- `media/netflix.txt`
- `media/all-media.txt`

### Общение
- `social/discord.txt`
- `social/telegram.txt`
- `social/reddit.txt`
- `social/all-social.txt`

### Игры
- `gaming/steam.txt`
- `gaming/xbox.txt`
- `gaming/playstation.txt`
- `gaming/epic-games.txt`
- `gaming/all-gaming.txt`

### Комплексные наборы
- `bundles/developer.txt`
- `bundles/gamer.txt`
- `bundles/everything.txt`

## Автоматическое обновление

GitHub Action запускает `scripts/build.py` каждый день и обновляет объединённые наборы.

Исходные домены хранятся в `sources/catalog.json`. На первом этапе они поддерживаются вручную, чтобы списки оставались компактными и предсказуемыми. Позже генератор можно расширить импортом из `v2fly/domain-list-community`.

## Важное замечание

Домены сервисов меняются. Перед включением большого набора рекомендуется проверить, не попали ли туда общие CDN-домены, маршрутизация которых через VPN может затронуть посторонние сайты.
