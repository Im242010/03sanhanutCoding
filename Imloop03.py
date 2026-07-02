import random
my_number = random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("ตัวเลขของคุณ: "))
        attempts += 1
        
        if  guess < my_number:
            print("น้อยไป")
        elif guess > my_number:
            print("เกินไปจ้า")
        else:
            print(f"ถูกต้อง คำตอบคือ{my_number}")
            print(f"คุณใช้จำนวนการทายทั้งหมด {attempts} ครั้ง")
            break

    except ValueError:
        print("ใส่เลขที่ถูกต้อง")