# CleanDownload 

โปรแกรม Python สำหรับจัดระเบียบไฟล์ในโฟลเดอร์ Downloads โดยอัตโนมัติ โดยแยกประเภทไฟล์เข้าโฟลเดอร์ต่างๆ ตามนามสกุล

## คุณสมบัติ

- จัดระเบียบไฟล์จากโฟลเดอร์ Downloads อัตโนมัติ
- แยกไฟล์ตามประเภทเข้าโฟลเดอร์ต่างๆ 10 หมวดหมู่:
  - **Images**: ไฟล์รูปภาพ (jpg, png, gif, heic, svg, webp, ico, raw)
  - **Documents**: เอกสาร (pdf, doc, docx, xlsx, ppt, txt, csv, pages, numbers, key)
  - **Videos**: วิดีโอ (mp4, avi, mkv, mov, webm, vob)
  - **Music**: ไฟล์เสียง (mp3, wav, flac, m4a, aac, ogg)
  - **Archives**: ไฟล์บีบอัด (zip, rar, tar, gz, 7z, pkg, dmg, iso)
  - **Web_Development**: ไฟล์พัฒนาเว็บ (html, css, scss, js, ts, jsx, tsx, php, vue)
  - **Scripts_and_Code**: โค้ดและสคริปต์ (py, sh, bat, rb, go, c, cpp, java, swift)
  - **Data_and_Config**: ไฟล์ข้อมูลและการตั้งค่า (json, xml, yml, yaml, md, ini, conf, env, log)
  - **Database**: ไฟล์ฐานข้อมูล (sql, db, sqlite, sqlite3, dump)
  - **Executables_and_Fonts**: โปรแกรมและฟอนต์ (exe, msi, app, otf, ttf, woff, woff2)
- สร้างโฟลเดอร์อัตโนมัติหากยังไม่มี
- จัดการชื่อไฟล์ซ้ำอัตโนมัติ (เพิ่มหมายเลขต่อท้าย)
- ไม่กระทบกับโฟลเดอร์ย่อยที่มีอยู่แล้ว
- แสดงผลการย้ายไฟล์แบบเรียลไทม์

## ความต้องการ

- Python 3.x
- ไม่ต้องติดตั้ง library เพิ่มเติม (ใช้ `os` และ `shutil` ที่มีมาในตัว)

## การใช้งาน

1. **แก้ไขพาธโฟลเดอร์**: แก้ไขตัวแปร `source_dir` ใน [script.py](script.py) ให้ชี้ไปยังโฟลเดอร์ที่ต้องการจัดระเบียบ:
   ```python
   source_dir = '/Users/aomsirawit/Downloads'
   ```

2. **รันสคริปต์**:
   ```bash
   python3 script.py
   ```

3. **ผลลัพธ์**: โปรแกรมจะย้ายไฟล์เข้าโฟลเดอร์ตามประเภทโดยอัตโนมัติและแสดงความคืบหน้า

## การปรับแต่ง

คุณสามารถเพิ่มนามสกุลไฟล์หรือประเภทโฟลเดอร์ใหม่ได้ใน dictionary `file_types`:

```python
file_types = {
    'ชื่อโฟลเดอร์': ['.นามสกุล1', '.นามสกุล2', ...],
    # ...
}
```

### ตัวอย่างการเพิ่มหมวดหมู่ใหม่

```python
file_types = {
    # ... หมวดหมู่เดิม
    'Design': ['.psd', '.ai', '.sketch', '.fig', '.xd'],
    '3D_Models': ['.obj', '.fbx', '.blend', '.stl'],
}
```

## ตัวอย่างผลลัพธ์

```
Moved: document.pdf -> Documents/document.pdf
Moved: photo.jpg -> Images/photo.jpg
Moved: video.mp4 -> Videos/video.mp4
Moved: script.py -> Scripts_and_Code/script.py
Moved: document.pdf -> Documents/document(1).pdf  # ชื่อซ้ำ จะเพิ่มหมายเลข
```

## วิธีการทำงาน

1. สแกนทุกไฟล์ในโฟลเดอร์ที่ระบุ
2. ตรวจสอบนามสกุลไฟล์
3. สร้างโฟลเดอร์ย่อยตามประเภทหากยังไม่มี
4. ย้ายไฟล์เข้าโฟลเดอร์ที่เหมาะสม
5. จัดการชื่อไฟล์ซ้ำโดยเพิ่มหมายเลขต่อท้าย

## ข้อควรระวัง

- สคริปต์จะข้ามโฟลเดอร์ย่อยที่มีอยู่แล้ว (จะจัดระเบียบเฉพาะไฟล์ระดับบนสุด)
- หากมีไฟล์ชื่อซ้ำในโฟลเดอร์ปลายทาง จะเพิ่มหมายเลขต่อท้ายอัตโนมัติ เช่น `file(1).pdf`, `file(2).pdf`
- แนะนำให้สำรองข้อมูลสำคัญก่อนรันครั้งแรก
- ตรวจสอบว่าได้กำหนดพาธโฟลเดอร์ถูกต้องก่อนรัน

## การมีส่วนร่วม

สามารถ Fork โปรเจกต์และส่ง Pull Request หรือเปิด Issue เพื่อแจ้งปัญหาและข้อเสนอแนะได้

## License

MIT License - ดูรายละเอียดใน [LICENSE](LICENSE)

## ผู้พัฒนา

**AomSirawit**

---

⭐ ถ้าโปรเจกต์นี้มีประโยชน์ อย่าลืมให้ Star นะครับ!
