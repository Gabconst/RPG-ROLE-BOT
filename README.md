# 🎲 RPG-Role-Bot (GAB-Bot)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

O **RPG-Role-Bot** (também conhecido como **GAB-Bot**) é um assistente completo para jogadores de D&D 5e no Discord. Ele automatiza rolagens de dados, gerencia fichas de personagens e controla pontos de vida (HP) de forma simples e intuitiva.

## 🚀 Objetivo
O projeto nasceu da necessidade de simplificar as sessões de RPG, permitindo que os jogadores foquem na história enquanto o bot cuida da matemática dos atributos e das rolagens complexas.

## ✨ Funcionalidades

- **🎲 Rolagens Inteligentes:** Suporte para dados (ex: `1d20+5`) e integração automática com atributos da ficha (ex: `d20+for`).
- **📝 Ficha de Personagem:** Armazenamento persistente de atributos (FOR, DES, CON, INT, SAB, CAR).
- **❤️ Gestão de HP:** Controle dinâmico de vida máxima, dano e cura.
- **📦 Banco de Dados:** Utiliza SQLite para garantir que os dados dos jogadores não sejam perdidos após reinicializações.
- **🛡️ Segurança:** Configuração via variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Discord.py:** Biblioteca principal para integração com a API do Discord.
- **SQLite:** Banco de dados leve e eficiente para persistência.
- **Python-dotenv:** Gerenciamento de segredos e tokens.

## 📂 Estrutura do Projeto

- `bot.py`: O coração do bot, gerenciando comandos e eventos do Discord.
- `db_manager.py`: Módulo responsável por toda a comunicação com o banco de dados e cálculos de modificadores.
- `dice_logic.py`: Motor de processamento de expressões de dados e Regex.
- `documentacao/`: Guias detalhados para jogadores e administradores.
- `requirements.txt`: Lista de dependências do projeto.

## 🔧 Instalação e Execução

### Pré-requisitos
- Python 3.10 ou superior.
- Um Token de Bot do Discord (obtido no [Discord Developer Portal](https://discord.com/developers/applications)).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Gabconst/RPG-ROLE-BOT.git
   cd RPG-ROLE-BOT
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   DISCORD_TOKEN=seu_token_aqui
   ```

4. **Inicie o bot:**
   ```bash
   python3 bot.py
   ```

## 🎮 Comandos Principais

O prefixo padrão é `-gab-`.

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| `roll` | Rola dados (suporta atributos) | `-gab-roll d20+for` |
| `set` | Define valor de um atributo | `-gab-set for 16` |
| `hp` | Ajusta vida (cura ou dano) | `-gab-hp -10` |
| `sheet` | Mostra a ficha completa | `-gab-sheet` |

*Para mais detalhes, consulte o [Guia do Jogador](documentacao/Guia_do_Jogador.md).*

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---
Desenvolvido com ❤️ por [Gabconst](https://github.com/Gabconst)
