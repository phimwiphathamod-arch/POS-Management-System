# My Shop Web App

เว็บไซต์ร้านค้าออนไลน์ที่พัฒนาด้วย Django สำหรับแสดงสินค้า เพิ่มลงตะกร้า และจัดการคำสั่งซื้อแบบง่าย ๆ

## ภาพตัวอย่างหน้าเว็บ

### หน้า Home

<img width="1502" height="737" alt="image" src="https://github.com/user-attachments/assets/768b9b01-774e-4664-9d3a-774c27a15c81" />

### หน้า Products

<img width="1523" height="638" alt="image" src="https://github.com/user-attachments/assets/3e83c60f-c19f-4128-8a0a-b4f2a8ff36f2" />

### หน้า Cart
![Uploading image.png…]()


## ฟีเจอร์หลัก

- หน้าแสดงสินค้าและหมวดหมู่
- ค้นหาสินค้าและดูรายละเอียดสินค้า
- เพิ่มสินค้าเข้า ตะกร้า
- ปรับจำนวนสินค้าในตะกร้า
- หน้า Checkout และการชำระเงิน
- ระบบผู้ใช้และจัดการโปรไฟล์

## วิธีรันโปรเจกต์

1. สร้าง virtual environment
   ```bash
   python -m venv venv
   ```

2. เปิด environment
   ```bash
   .\venv\Scripts\activate
   ```

3. ติดตั้ง dependency ที่จำเป็น
   ```bash
   pip install django pillow
   ```

4. รัน migration
   ```bash
   python manage.py migrate
   ```

5. เริ่มเซิร์ฟเวอร์
   ```bash
   python manage.py runserver
   ```

6. เปิดบราวเซอร์ที่
   ```text
   http://127.0.0.1:8000/
   ```

## โครงสร้างโปรเจกต์

- user/templates: หน้า HTML ของเว็บไซต์
- user/views.py: ควบคุม Logic ของการแสดงผลและการทำงานต่าง ๆ
- user/models.py: โมเดลสินค้า ผู้ใช้ และคำสั่งซื้อ
- myApp/settings.py: การตั้งค่าโปรเจกต์

## หมายเหตุ

โปรเจกต์นี้ยังมีฟีเจอร์เพิ่มเติมที่สามารถขยายต่อได้ เช่น ระบบ admin, การจัดการคำสั่งซื้อ, การแจ้งเตือน, และระบบชำระเงินจริงต่อไป
