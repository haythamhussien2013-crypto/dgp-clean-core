import hashlib
import time
import math

# ده "المفتاح السري" اللي بيميز كودك عن أي حد تاني
# غير الكلمات دي لأي جملة سرية تانية من اختيارك
SECRET_SEED = "Haytham_AL_Abasiry_Secure_Key_2026"

def generate_secure_otp(seed, interval=180):
    # حساب الوقت الحالي مقسوم على 3 دقائق (180 ثانية)
    time_step = math.floor(time.time() / interval)
    
    # دمج الوقت مع المفتاح السري وتشفيرهم بـ SHA-256
    raw_data = f"{seed}{time_step}".encode()
    hash_digest = hashlib.sha256(raw_data).hexdigest()
    
    # تحويل جزء من التشفير لرقم من 6 خانات
    otp = int(hash_digest[:8], 16) % 1000000
    return f"{otp:06d}"

if __name__ == "__main__":
    print("-" * 30)
    print("نظام الأمان المطور - هيثم الأباصيري")
    print("-" * 30)
    
    while True:
        current_otp = generate_secure_otp(SECRET_SEED)
        print(f"كود الأمان الحالي (صالح لـ 3 دقائق): {current_otp}")
        
        # تحديث الكود كل 10 ثواني للتأكد
        time.sleep(10)
