# 🎨 Creative Design Skill

Architecture diagrams, ASCII video, infographics, manim, p5js, popular web designs

**Repository by:** [Alpesh Makwana](https://github.com/makwanaalpesh811-a11y)

---

## 📦 What's Inside

10 Hermes Agent skills for creative design skill:

- `architecture-diagram` — "Dark-themed SVG architecture/cloud/infra diagrams as HTML."
- `ascii-video` — "ASCII video: convert video/audio to colored ASCII MP4/GIF."
- `baoyu-infographic` — "Infographics: 21 layouts x 21 styles (信息图, 可视化)."
- `claude-design` — Design one-off HTML artifacts (landing, deck, prototype).
- `design-md` — Author/validate/export Google's DESIGN.md token spec files.
- `humanizer` — "Humanize text: strip AI-isms and add real voice."
- `manim-video` — "Manim CE animations: 3Blue1Brown math/algo videos."
- `p5js` — "p5.js sketches: gen art, shaders, interactive, 3D."
- `popular-web-designs` — 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- `songwriting-and-ai-music` — "Songwriting craft and Suno AI music prompts."

---


## 🔐 SECURITY NOTICE

**This repo is safe to use publicly.** It contains only skill definitions (SKILL.md) and documentation - no live credentials.

### What NOT to commit:
- API keys (GitHub, YouTube, Gemini, OpenAI, etc.)
- AWS credentials (`~/.aws/credentials`)
- Telegram bot tokens
- Exchange API keys (Delta, Hyperliquid, etc.)
- Private keys or certificates

### Where to store secrets (on your machine):
```
~/.aws/credentials          # AWS
~/.youtube_token.json       # YouTube OAuth
~/.ig_env                   # Instagram/Gemini
~/.signal_bot_env           # Trading bot
~/.gh_token                 # GitHub token
```

All skills are designed to read secrets from your filesystem, not embed them.


## 🚀 Installation

### Option 1: Clone to Hermes skills directory
```bash
git clone https://github.com/makwanaalpesh811-a11y/creative-design-skill.git ~/.hermes/skills/creative-design-skill
```

### Option 2: Install individual skills
```bash
# Create skills dir if not exists
mkdir -p ~/.hermes/skills

# Clone only what you need
git clone --depth 1 --filter=blob:none https://github.com/makwanaalpesh811-a11y/creative-design-skill.git /tmp/creative-design-skill
cp -r /tmp/creative-design-skill/skills/* ~/.hermes/skills/
```

---

## ⚙️ Prerequisites

Check each skill's `SKILL.md` for specific dependencies. Common ones:
- **Termux** (Android terminal) or Linux/macOS
- **Python 3.11+**
- **Node.js + npm** (for CLI-based skills)
- **API keys** stored in `~/.<name>_env` or `~/.<name>_token.json` files

---

## 🔧 Setup Guide

1. **Install Hermes Agent:** `pip install hermes-agent` or see [Hermes docs](https://hermes-agent.nousresearch.com/docs)
2. **Clone this repo** into `~/.hermes/skills/`
3. **Configure credentials** in your environment (see each skill's SKILL.md)
4. **Use in chat:** Ask Hermes to use any skill by name

---

## 📚 Skill Documentation

Each skill lives in `skills/<skill-name>/SKILL.md` with:
- **YAML frontmatter:** name, description
- **Commands:** CLI/API references
- **Examples:** Ready-to-use snippets
- **Gotchas:** Real-world pitfalls

---

## 🛡️ Security

## 🔐 SECURITY NOTICE

**This repo is safe to use publicly.** It contains only skill definitions (SKILL.md) and documentation - no live credentials.

### What NOT to commit:
- API keys (GitHub, YouTube, Gemini, OpenAI, etc.)
- AWS credentials (`~/.aws/credentials`)
- Telegram bot tokens
- Exchange API keys (Delta, Hyperliquid, etc.)
- Private keys or certificates

### Where to store secrets (on your machine):
```
~/.aws/credentials          # AWS
~/.youtube_token.json       # YouTube OAuth
~/.ig_env                   # Instagram/Gemini
~/.signal_bot_env           # Trading bot
~/.gh_token                 # GitHub token
```

All skills are designed to read secrets from your filesystem, not embed them.

---

## 📜 License

MIT License - see [LICENSE](./LICENSE)

---

## 👨‍💻 Author

**Alpesh Makwana** — Trading, content, and Hermes Agent enthusiast.

- **GitHub:** [makwanaalpesh811-a11y](https://github.com/makwanaalpesh811-a11y)
- **Telegram:** @alpeshalgobot

---

## 🤝 Contributing

Issues and PRs welcome. Follow the SKILL.md format conventions.

## 🏷️ Topics
`creative` `design` `diagram` `infographic` `manim` 
