# 🛠️ Guia de Manutenção: GAB-Bot

Este documento contém as informações técnicas para você gerenciar o bot.

## 🏠 Hospedagem
O bot está hospedado **localmente** na sua máquina no diretório:
`~/.ssh/gab_bot/`

## 🏗️ Explicação da Infraestrutura
- **Hospedagem Local:** O bot roda como um processo de segundo plano no seu Linux. Enquanto o script estiver ativo, o bot está online.
- **Banco de Dados (SQLite):** Utilizamos o SQLite para persistência. Diferente de bancos complexos, ele salva tudo em um único arquivo (`rpg_bot.db`), facilitando backups e portabilidade.
- **Segurança (.env):** O Token do Discord é mantido fora do código principal, isolado no arquivo `.env`, seguindo padrões de segurança de desenvolvimento.

## 🧠 Arquitetura da Aplicação
A aplicação foi construída de forma modular em Python:
1. **`bot.py` (O Coração):** Gerencia a conexão com o Discord, interpreta comandos e organiza as respostas.
2. **`dice_logic.py` (O Motor):** Processa as rolagens. Ele usa Regex (Expressões Regulares) para identificar dados (ex: `1d20`) e substitui atributos (ex: `for`) pelos modificadores calculados.
3. **`db_manager.py` (O Gerente):** Cuida exclusivamente da leitura e escrita no banco de dados, além de calcular os modificadores de D&D 5e: `(valor - 10) // 2`.

## ⚙️ Estrutura de Arquivos
- `bot.py`: Código principal (Comandos do Discord).
- `db_manager.py`: Gerenciamento do banco de dados SQLite.
- `dice_logic.py`: Lógica de processamento de dados e modificadores.
- `.env`: Contém o seu **TOKEN** (chave secreta). **Nunca compartilhe este arquivo!**
- `rpg_bot.db`: Arquivo que armazena as fichas de todos os jogadores.

## 🚀 Como Ligar o Bot
Sempre que quiser usar o bot, abra o terminal e rode:
```bash
cd ~/.ssh/
python3 gab_bot/bot.py
```

## 🛠️ Manutenção Local
1. **Mudar Prefixo:** Edite a linha `command_prefix='-gab-'` no arquivo `bot.py`.
2. **Atualizar Dependências:** Caso mude de computador, rode `pip install -r requirements.txt`.
3. **Backup de Dados:** Para salvar as fichas dos jogadores, basta fazer uma cópia do arquivo `rpg_bot.db`.

## 🆘 Troubleshooting (Problemas Comuns)
- **Bot não responde:** Verifique se o comando `python3` ainda está rodando no terminal.
- **Erro de Privileged Intents:** Certifique-se que o "Message Content Intent" está ligado no Discord Developer Portal.
- **Erro de Módulo não encontrado:** Rode `pip install discord.py python-dotenv`.

---
*Documentação gerada automaticamente pelo Gemini CLI.*
