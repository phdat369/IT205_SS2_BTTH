
# Tên bệnh nhân
# Năm sinh
# Số ngày bị bệnh
# Nhiệt độ cơ thể (°C)
# Chi phí khám


# Tên không được để trống
# Năm sinh phải nằm trong khoảng hợp lệ (1900 → năm hiện tại)
# Số ngày bị bệnh ≥ 0
# Nhiệt độ nằm trong khoảng 30 → 45°C
# Chi phí khám > 0

# 3. Tính toán thông tin
# Tính tuổi bệnh nhân
# Tính phụ phí = 10% chi phí khám
# Tính tổng chi phí = chi phí khám + phụ phí
 

# 4. Phân loại tình trạng sức khỏe
# Dựa vào nhiệt độ và số ngày bị bệnh:

# Nếu nhiệt độ > 38°C và số ngày bệnh > 3 → "Nguy hiểm"
# Nếu nhiệt độ > 38°C → "Sốt cao"
# Nếu nhiệt độ > 37.5°C → "Sốt nhẹ"
# Ngược lại → "Bình thường"
 

# 5. Đánh giá mức độ ưu tiên (Nested If)
# Nếu tình trạng là "Nguy hiểm":
# Nếu tuổi > 60 → "Cấp cứu"
# Ngược lại → "Ưu tiên cao"
# Các trường hợp khác:
# → "Bình thường"
# 6. Đánh giá mức chi phí (Toán tử 3 ngôi)
# Nếu tổng chi phí > 500000 → "Cao"
# Ngược lại → "Thấp"
from datetime import datetime
import sys 
full_name = input("Nhập tên bệnh nhân: ")
year = int(input("Nhập năm sinh : "))
sick_days = int(input("Nhập số ngày bị bệnh : "))
tem_body = float(input("Nhập nhiệt độ cơ thể độ °C :"))
fee = float(input("Nhập chi phí khám : "))


if not full_name :
    print("Tên không được để trống ")
    sys.exit()
elif year < 1900 or year > datetime.now().year:
    print("Năm sinh phải nằm trong khoảng hợp lệ (1900 → năm hiện tại)")
    sys.exit()
elif sick_days < 0 :
    print ("Số ngày bị bệnh ≥ 0")
    sys.exit()
elif  tem_body < 30  or tem_body > 45 :
    print("Nhiệt độ nằm trong khoảng 30 → 45°C")
    sys.exit()
elif fee <= 0 :
    print("Chi phí khám > 0")
    sys.exit()



age = datetime.now().year - year
print (age)
total_fee = fee*(1.1)

if tem_body > 38 and sick_days > 3 :
    wanted = "Nguy hiểm"
elif tem_body > 38:
    wanted = "Sốt cao"
elif tem_body > 37.5:
    wanted = "Sốt nhẹ"
else :
    wanted = "Bình thương"

if wanted == "Nguy hiểm":
    if age > 60 :
        level = "Cấp cứu"
    else :
        level = "Ưu tiên cao"
else:
    level = "Bình thường"

status = "Cao" if total_fee > 500000 else "Thấp"


print("--- kết quả ---")
print(f"Tên: {full_name}")
print(f"Tuổi: {age}")
print(f"Nhiệt độ: {tem_body}°C")
print(f"Số ngày bệnh: {sick_days}")

print(f"Tình trạng: {wanted}")
print(f"Mức độ ưu tiên: {level}")

print(f"Tổng chi phí: {total_fee} VND")
print(f"Mức chi phí: {status}")