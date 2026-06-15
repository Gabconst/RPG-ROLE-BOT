import db_manager
import dice_logic

def test_db():
    print("Testando Banco de Dados...")
    db_manager.init_db()
    db_manager.update_character(123, 'strength', 18)
    char = db_manager.get_character(123)
    assert char[2] == 18
    print("✅ Banco de Dados OK!")

def test_dice():
    print("Testando Lógica de Dados...")
    # Test simple roll
    rolled, total = dice_logic.roll_dice("1d1")
    assert total == 1
    
    # Test with attributes
    char = (123, "Test", 16, 10, 10, 10, 10, 10, 10, 10) # STR 16 -> +3
    rolled, total = dice_logic.roll_dice("1d1+for", char)
    assert total == 4
    print("✅ Lógica de Dados OK!")

if __name__ == '__main__':
    test_db()
    test_dice()
