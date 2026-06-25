print("ตรวจจับความเร็ว")
kilometer = int(input("ความเร็วรถ km/h :"))
if kilometer <80:
    print("\nปลอดภัย")
elif kilometer <101:
    print("\nเตือน")
elif kilometer <121:
    print("\nเสียงถูกปรับ")
else:
    print("\nผิดกฎหมาย ปรับทันที")
    print("โดยนายสัณหณัฐ วีรบรรจง ม.4/4 เลขที่3")