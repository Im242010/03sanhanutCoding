print("โปรแกรมคำนวณคะแนนรวม\n")

maths = int(input("คะแนนสอบคณิตศาสตร์"))
English = int(input("คะแนนสอบภาษาอังกฤษ"))
Social = int(input("คะแนนสอบสังคม"))

total_score = maths + English + Social
average = total_score/3
if average < 60:
    print("คะแนนรวม 3 วิชา") , total_score
    print("คะแนนเฉลี่ย 3 วิชา") , average
    print("ควรปรับปรุง")
elif average > 80:
    print("ผ่าน")
else:
    print("คะแนนรวม 3 วิชา")
    print("คะแนนเฉลี่ย 3 วิชา",total_score/3)
    print("ดีเยี่ยม")