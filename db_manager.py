import sqlite3
import os

# Define o caminho do banco de dados relativo a este arquivo
DB_PATH = os.path.join(os.path.dirname(__file__), 'rpg_bot.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            strength INTEGER DEFAULT 10,
            dexterity INTEGER DEFAULT 10,
            constitution INTEGER DEFAULT 10,
            intelligence INTEGER DEFAULT 10,
            wisdom INTEGER DEFAULT 10,
            charisma INTEGER DEFAULT 10,
            hp_max INTEGER DEFAULT 10,
            hp_current INTEGER DEFAULT 10
        )
    ''')
    conn.commit()
    conn.close()

def get_character(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM characters WHERE user_id = ?', (user_id,))
    char = cursor.fetchone()
    conn.close()
    return char

def update_character(user_id, field, value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if character exists
    cursor.execute('SELECT 1 FROM characters WHERE user_id = ?', (user_id,))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO characters (user_id) VALUES (?)', (user_id,))
    
    cursor.execute(f'UPDATE characters SET {field} = ? WHERE user_id = ?', (value, user_id))
    conn.commit()
    conn.close()

def get_modifier(value):
    return (value - 10) // 2
