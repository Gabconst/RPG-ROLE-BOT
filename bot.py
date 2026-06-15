import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import db_manager
import dice_logic

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-gab-', intents=intents)

@bot.event
async def on_ready():
    db_manager.init_db()
    print(f'Bot conectado como {bot.user}')

@bot.command(name='roll')
async def roll(ctx, *, expression: str):
    char = db_manager.get_character(ctx.author.id)
    rolled, total = dice_logic.roll_dice(expression, char)
    
    if rolled:
        await ctx.send(f'🎲 **{ctx.author.display_name}** rolou: `{expression}`\nResultados: `{rolled}`\n**Total: {total}**')
    else:
        await ctx.send(f'❌ Erro na rolagem: {total}')

@bot.command(name='set')
async def set_attr(ctx, attr: str, value: int):
    valid_attrs = {
        'for': 'strength',
        'des': 'dexterity',
        'con': 'constitution',
        'int': 'intelligence',
        'sab': 'wisdom',
        'car': 'charisma',
        'hp': 'hp_max'
    }
    
    attr = attr.lower()
    if attr in valid_attrs:
        db_manager.update_character(ctx.author.id, valid_attrs[attr], value)
        if attr == 'hp':
            db_manager.update_character(ctx.author.id, 'hp_current', value)
        await ctx.send(f'✅ **{attr.upper()}** definido para **{value}** para {ctx.author.display_name}.')
    else:
        await ctx.send(f'❌ Atributo inválido. Use: {", ".join(valid_attrs.keys())}')

@bot.command(name='hp')
async def adjust_hp(ctx, delta: int):
    char = db_manager.get_character(ctx.author.id)
    if not char:
        await ctx.send('❌ Você não tem uma ficha criada. Use `-gab-set hp 10` primeiro.')
        return
    
    current_hp = char[9]
    max_hp = char[8]
    new_hp = max(0, min(max_hp, current_hp + delta))
    
    db_manager.update_character(ctx.author.id, 'hp_current', new_hp)
    
    # Visual feedback for damage/healing
    if delta < 0:
        await ctx.send(f'💥 **{ctx.author.display_name}** recebeu **{-delta}** de dano! HP: {current_hp} -> **{new_hp}**/{max_hp}')
    elif delta > 0:
        await ctx.send(f'💖 **{ctx.author.display_name}** curou **{delta}** de vida! HP: {current_hp} -> **{new_hp}**/{max_hp}')
    else:
        await ctx.send(f'❤️ HP de **{ctx.author.display_name}**: **{new_hp}**/{max_hp}')

@bot.command(name='sheet')
async def show_sheet(ctx):
    char = db_manager.get_character(ctx.author.id)
    if not char:
        await ctx.send('❌ Você não tem uma ficha criada. Use `-gab-set` para começar.')
        return
    
    embed = discord.Embed(title=f"Ficha de RPG - {ctx.author.display_name}", color=discord.Color.blue())
    embed.add_field(name="💪 FOR", value=f"{char[2]} ({db_manager.get_modifier(char[2]):+})", inline=True)
    embed.add_field(name="🏃 DES", value=f"{char[3]} ({db_manager.get_modifier(char[3]):+})", inline=True)
    embed.add_field(name="🛡️ CON", value=f"{char[4]} ({db_manager.get_modifier(char[4]):+})", inline=True)
    embed.add_field(name="🧠 INT", value=f"{char[5]} ({db_manager.get_modifier(char[5]):+})", inline=True)
    embed.add_field(name="🧘 SAB", value=f"{char[6]} ({db_manager.get_modifier(char[6]):+})", inline=True)
    embed.add_field(name="✨ CAR", value=f"{char[7]} ({db_manager.get_modifier(char[7]):+})", inline=True)
    embed.add_field(name="❤️ HP", value=f"{char[9]}/{char[8]}", inline=False)
    
    await ctx.send(embed=embed)

# Atalho para rolagem direta se não encontrar comando
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('-gab-'):
        # Process commands first
        ctx = await bot.get_context(message)
        if ctx.command:
            await bot.invoke(ctx)
            return

        # If not a command, try to roll as a dice expression
        expression = message.content.replace('-gab-', '').strip()
        if expression:
            char = db_manager.get_character(message.author.id)
            rolled, total = dice_logic.roll_dice(expression, char)
            if rolled:
                await message.channel.send(f'🎲 **{message.author.display_name}** rolou: `{expression}`\nResultados: `{rolled}`\n**Total: {total}**')
                return

if __name__ == '__main__':
    if not TOKEN:
        print("ERRO: DISCORD_TOKEN não encontrado no arquivo .env")
    else:
        bot.run(TOKEN)
