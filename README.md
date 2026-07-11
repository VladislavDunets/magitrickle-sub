<div align="center">

# 🚀 MagiTrickle Subscriptions

### Автоматически обновляемые подписки для MagiTrickle

![GitHub last commit](https://img.shields.io/github/last-commit/VladislavDunets/magitrickle-sub)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/VladislavDunets/magitrickle-sub/update-subscriptions.yml)
![License](https://img.shields.io/github/license/VladislavDunets/magitrickle-sub)

Готовые списки доменов и IP-сетей для маршрутизации сервисов через **MagiTrickle**.

Подписки автоматически обновляются из открытых и официальных источников с помощью GitHub Actions.

</div>

---

## 📌 Возможности

- 🔄 Ежедневическое автоматическое обновление
- 🌐 Доменные списки из `v2fly/domain-list-community`
- 📡 Официальные IPv4/IPv6-сети Telegram
- 🤖 Отдельная подписка для AI-сервисов
- 💬 Telegram и Discord
- 📷 Meta, Instagram и связанные сервисы
- 📺 Twitch
- ⚡ Готовые Raw-ссылки для MagiTrickle
- 🛠 Открытый генератор подписок

---

## 📦 Доступные подписки

| Подписка | Тип правил | Что входит |
|---|---|---|
| 🤖 AI | Домены | ChatGPT, Claude, Gemini, DeepSeek, Grok, Perplexity, Mistral, Cohere, Hugging Face и другие |
| 💬 Discord | Домены | Discord и связанные домены |
| ✈ Telegram | Домены | Telegram, `t.me`, Telegraph, Fragment, TON и связанные сервисы |
| 🌐 Telegram IPList | IPv4 и IPv6 CIDR | Официальные IP-сети Telegram |
| 📷 Meta + Instagram | Домены | Facebook, Instagram, Messenger, Threads, WhatsApp, Oculus |
| 📺 Twitch | Домены | Twitch и связанные CDN |

---

## 🚀 Подключение

Откройте в MagiTrickle раздел **Подписки**, создайте новую подписку и вставьте нужную Raw-ссылку.

Назначьте подписку группе, которая маршрутизируется через VPN или другой нужный интерфейс.

### 🤖 AI

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/ai.txt
```

### 💬 Discord

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/discord.txt
```

### ✈ Telegram — домены

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/telegram.txt
```

### 🌐 Telegram IPList

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/telegram-ip.txt
```

> Для корректной работы Telegram рекомендуется подключить **обе подписки**:
>
> - `telegram.txt` — домены;
> - `telegram-ip.txt` — официальные IPv4/IPv6-сети.
>
> Telegram-клиенты могут подключаться к дата-центрам напрямую по IP, поэтому одной доменной подписки иногда недостаточно.

### 📷 Meta + Instagram

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/meta-instagram.txt
```

### 📺 Twitch

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/twitch.txt
```

---

## 🔄 Как происходит обновление

GitHub Actions запускает генератор:

- ежедневно по расписанию;
- вручную через вкладку **Actions**;
- при изменении генератора, конфигурации или workflow.

Во время запуска генератор:

1. Загружает актуальные доменные категории из `v2fly/domain-list-community`.
2. Рекурсивно раскрывает директивы `include:`.
3. Обрабатывает правила `domain:`, `full:`, `regexp:` и `keyword:`.
4. Исключает правила с атрибутом `@ads`.
5. Загружает официальный список IPv4/IPv6-сетей Telegram.
6. Проверяет корректность CIDR.
7. Формирует готовые текстовые подписки для MagiTrickle.
8. Создаёт новый commit только в том случае, если списки действительно изменились.

---

## 🗂 Источники данных

### Доменные правила

Для доменных подписок используется:

```text
https://github.com/v2fly/domain-list-community
```

Из него формируются списки:

- AI;
- Discord;
- Telegram Domains;
- Meta + Instagram;
- Twitch.

### IP-сети Telegram

Для `telegram-ip.txt` используется официальный источник Telegram:

```text
https://core.telegram.org/resources/cidr.txt
```

Этот файл содержит актуальные IPv4- и IPv6-диапазоны дата-центров Telegram.

---

## 🔁 Схема работы

```text
v2fly/domain-list-community
       │
       │ доменные правила
       ▼
┌─────────────────────┐
│                     │
│    GitHub Actions   │
│      + build.py     │
│                     │
└─────────────────────┘
       ▲
       │ IPv4/IPv6 CIDR
       │
core.telegram.org/resources/cidr.txt
       │
       ▼
subscriptions/*.txt
       │
       ▼
GitHub Raw
       │
       ▼
MagiTrickle
```

---

## 📁 Структура проекта

```text
.
├── .github/
│   └── workflows/
│       └── update-subscriptions.yml
│
├── scripts/
│   └── build.py
│
├── sources/
│   └── config.json
│
├── subscriptions/
│   ├── ai.txt
│   ├── discord.txt
│   ├── meta-instagram.txt
│   ├── telegram.txt
│   ├── telegram-ip.txt
│   └── twitch.txt
│
├── LICENSE
└── README.md
```

---

## ⚠️ Важные замечания

Доменные подписки могут содержать домены CDN и общей инфраструктуры сервисов. Перед использованием рекомендуется просмотреть содержимое конкретного списка.

Подписка `telegram-ip.txt` предназначена для маршрутизации всей сетевой инфраструктуры Telegram и может включать IPv4- и IPv6-диапазоны всех его дата-центров.

IP-сети для Discord, Twitch, Meta и AI-сервисов намеренно не добавляются: многие из этих сервисов используют общие сети Cloudflare, Fastly, Akamai и других CDN. Маршрутизация таких CIDR может затронуть посторонние сайты.

---

## 🛠 Настройка состава подписок

Состав доменных подписок задаётся в файле:

```text
sources/config.json
```

После его изменения GitHub Actions автоматически перегенерирует списки.

Файлы в каталоге `subscriptions` редактировать вручную не рекомендуется — при следующем запуске генератора изменения будут перезаписаны.

---

## 🤝 Участие в проекте

Если вы нашли отсутствующий домен, ошибочное правило или хотите предложить новую подписку:

- создайте **Issue**;
- либо отправьте **Pull Request**.

Предложения и исправления приветствуются.

---

## ❤️ Благодарности

Проект использует данные и инструменты следующих проектов:

- [MagiTrickle](https://github.com/MagiTrickle/MagiTrickle)
- [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community)
- [Telegram CIDR](https://core.telegram.org/resources/cidr.txt)

---

## 📄 Лицензия

Проект распространяется по лицензии MIT.