print("โปรแกรมแม่สูตรคูณ Lv.2")
s = int(input("สูตรคูณเริ่มต้น แม่: "))
e = int(input("สูตรคูรตัวท้าย คือ: "))
for n in range(s,e+1):
 print("สูตรคูณแม่",n)
 for i in range(1,13):
     print(n,"x",i,"=",n*i)
print("โดย สัณหณัฐ วีรบรรจง เลขที่ 3")