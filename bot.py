import os
from prompt import COOLBLUE_SYSTEM_PROMPT

# ─────────────────────────────────
# Coolblue AI Bot - Simple Version
# (بدون API - برای تمرین)
# ─────────────────────────────────

def simulate_bot(user_message):
    """
    این تابع پیام کاربر رو می‌گیره
    و prompt رو آماده می‌کنه برای Claude
    """
    
    print("\n" + "="*50)
    print("COOLBLUE AI BOT - BLAUW")
    print("="*50)
    print(f"\n👤 Customer: {user_message}")
    print("\n📋 System Prompt Ready:")
    print("-"*30)
    print("✅ Role: Blauw - Coolblue Assistant")
    print("✅ Rules: Loaded")
    print("✅ Examples: Loaded")
    print("✅ Language Detection: Active")
    print("-"*30)
    print("\n💡 To get response:")
    print("1. Copy system prompt from prompt.py")
    print("2. Open claude.ai")
    print("3. Paste system prompt + this message:")
    print(f"\n   '{user_message}'")
    print("\n" + "="*50)

# ─────────────────────────────────
# تست با ۳ مشتری مختلف
# ─────────────────────────────────

if __name__ == "__main__":
    
    # تست ۱ - انگلیسی
    simulate_bot("Hi, I'm Tom. My phone stopped working after 1 week!")
    
    # تست ۲ - هلندی  
    simulate_bot("Hoi, ik ben Anna. Wanneer komt mijn bestelling aan?")
    
    # تست ۳ - مشکل فوری
    simulate_bot("My order was charged twice! This is unacceptable!")