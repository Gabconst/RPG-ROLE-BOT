# 🎲 GAB-Bot: Guia do Jogador (D&D 5e)

Este bot foi criado para facilitar suas rolagens e o controle da sua ficha durante nossas sessões de RPG. O prefixo para todos os comandos é `-gab-`.

---

## ⚔️ Comandos de Rolagem

Você pode rolar dados de duas formas:

1. **Atalho Direto:** Basta digitar o prefixo e os dados.
   - Exemplo: `-gab- d20+for`
   - Exemplo: `-gab- 2d10+5`

2. **Comando Explícito:**
   - Exemplo: `-gab-roll 1d20+des`

*O bot entende bônus de atributos automaticamente se você configurou sua ficha (use `for`, `des`, `con`, `int`, `sab`, `car`).*

---

## 📝 Gerenciamento de Ficha

Antes do combate, configure seus atributos básicos (valores de 1 a 20):

- **Definir Atributo:** `-gab-set [atributo] [valor]`
  - Atributos aceitos: `for`, `des`, `con`, `int`, `sab`, `car`.
  - Exemplo: `-gab-set for 16` (O bot calculará o bônus de +3 automaticamente).

- **Ver sua Ficha:** `-gab-sheet`
  - Mostra todos os seus bônus atuais e sua vida.

---

## ❤️ Controle de Vida (HP)

- **Definir Vida Máxima:** `-gab-set hp [valor]`
  - Exemplo: `-gab-set hp 40`
- **Receber Dano:** `-gab-hp -[valor]`
  - Exemplo: `-gab-hp -10` (Tira 10 de vida).
- **Receber Cura:** `-gab-hp [valor]`
  - Exemplo: `-gab-hp 5` (Cura 5 de vida).

---

*Bom jogo e que os deuses dos dados estejam a seu favor!*
