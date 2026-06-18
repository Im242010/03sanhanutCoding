print("คะแนนรวม")
point1 = int(input("คะแนนรวิชา 1: "))
point2 = int(input("คะแนนรวิชา 2: "))
point3 = int(input("คะแนนรวิชา 3: "))
total_point = point1 + point2 + point3
average = total_point/3

if total_point <60 : 
    print("1คะแนนรวมของคุณ = ", total_point)
    print("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("ควรปรับปรุง")
elif average < 80:
    print("ผ่าน")
else:
    print("ดีเยี่ยม")
    print("นายสัณหณัฐ วีรบรรจง ม.4/4 เลขที่390")