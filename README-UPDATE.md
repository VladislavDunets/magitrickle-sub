# Автоматическое обновление из v2fly

Этот комплект заменяет старую статическую генерацию.

## Что создаётся

- `subscriptions/twitch.txt`
- `subscriptions/discord.txt`
- `subscriptions/meta-instagram.txt`
- `subscriptions/telegram.txt`
- `subscriptions/ai.txt`

## Источники

Скрипт ежедневно скачивает исходные категории из:

`v2fly/domain-list-community/data`

Он рекурсивно раскрывает строки `include:`, удаляет комментарии и правила
с атрибутом `@ads`, преобразует `domain:`, `full:`, `regexp:` и `keyword:`
в формат, который понимает MagiTrickle.

Состав подписок задаётся в `sources/config.json`.

## AI

В AI автоматически входят категории:

- OpenAI / ChatGPT / Sora
- Anthropic / Claude
- Google DeepMind / Gemini / AI Studio / NotebookLM
- Perplexity
- xAI / Grok
- DeepSeek

Для сервисов, которых пока нет отдельной категорией в v2fly, добавлены
ручные домены Mistral, Cohere, Character AI и Hugging Face.

## Запуск

GitHub Actions → `Update subscriptions from v2fly` → `Run workflow`.

Затем открой созданные `.txt` и используй их Raw-ссылки в MagiTrickle.
