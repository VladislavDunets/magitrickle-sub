<div align="center">

# 🚀 MagiTrickle Subscriptions

### Автоматически обновляемые подписки для MagiTrickle

![GitHub last commit](https://img.shields.io/github/last-commit/VladislavDunets/magitrickle-sub)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/VladislavDunets/magitrickle-sub/update-subscriptions.yml)
![License](https://img.shields.io/github/license/VladislavDunets/magitrickle-sub)

Подборка готовых подписок для **MagiTrickle** с ежедневическим автоматическим обновлением из **v2fly/domain-list-community**.

</div>

---

# 📌 Возможности

- 🔄 Автоматическое обновление каждый день
- 🤖 Отдельная подписка для AI-сервисов
- 💬 Telegram и Discord
- 📷 Meta (Facebook, Instagram, Messenger, Threads, WhatsApp)
- 📺 Twitch
- ⚡ Готовые ссылки для подключения в MagiTrickle
- 🛠 Полностью открытый исходный код

---

# 📦 Доступные подписки

| Подписка | Что входит |
|----------|------------|
| 🤖 AI | ChatGPT, Claude, Gemini, DeepSeek, Grok, Perplexity, Mistral, Cohere, Hugging Face и другие |
| 💬 Discord | Домены Discord |
| ✈ Telegram | Домены Telegram |
| 📷 Meta | Facebook, Instagram, Messenger, Threads, WhatsApp, Oculus |
| 📺 Twitch | Twitch и связанные CDN |

---

# 🚀 Подключение

В MagiTrickle откройте раздел **Подписки**, нажмите **Добавить** и вставьте одну из ссылок ниже.

## 🤖 AI

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/ai.txt
```

---

## 💬 Discord

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/discord.txt
```

---

## ✈ Telegram (домены)

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/telegram.txt
```

---

## 🌐 Telegram IPList

Официальные IPv4/IPv6 диапазоны Telegram.

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/telegram-ip.txt
```

> **Рекомендуется использовать вместе с `telegram.txt`.**
> Домены обеспечивают корректную маршрутизацию DNS-запросов, а IPList позволяет маршрутизировать MTProto-трафик, который Telegram часто отправляет напрямую по IP-адресам.

---

## 📷 Meta

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/meta-instagram.txt
```

---

## 📺 Twitch

```text
https://raw.githubusercontent.com/VladislavDunets/magitrickle-sub/main/subscriptions/twitch.txt
```

---

# 🔄 Как происходит обновление

Каждый день GitHub Actions автоматически:

1. Скачивает актуальные правила из **v2fly/domain-list-community**
2. Генерирует подписки для MagiTrickle
3. Если обнаружены изменения — публикует новую версию файлов

Схема работы:

```text
v2fly/domain-list-community
            │
            ▼
     GitHub Actions
            │
            ▼
 Генерация подписок
            │
            ▼
      GitHub Raw
            │
            ▼
      MagiTrickle
```

После этого MagiTrickle автоматически скачивает обновлённую подписку по указанному URL.

---

# 📁 Структура проекта

```text
.
├── subscriptions/
│   ├── ai.txt
│   ├── discord.txt
│   ├── meta-instagram.txt
│   ├── telegram.txt
│   └── twitch.txt
│
├── scripts/
│   └── build.py
│
├── sources/
│   └── config.json
│
└── .github/
    └── workflows/
```

---

# ❤️ Источники

Проект использует данные:

- https://github.com/v2fly/domain-list-community

---

# 🤝 Как помочь проекту

Если вы нашли отсутствующий сервис или ошибку в правилах:

- создайте **Issue**;
- либо отправьте **Pull Request**.

Любые предложения по новым подпискам приветствуются.

---

# 📄 Лицензия

MIT