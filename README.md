# CleanDownload

โปรแกรม Python สำหรับจัดระเบียบไฟล์ในโฟลเดอร์ Downloads โดยอัตโนมัติ โดยแยกประเภทไฟล์เข้าโฟลเดอร์ต่างๆ ตามนามสกุล

## คุณสมบัติ

- จัดระเบียบไฟล์จากโฟลเดอร์ Downloads อัตโนมัติ
- แยกไฟล์ตามประเภทเข้าโฟลเดอร์ต่างๆ 10 หมวดหมู่:
  - **Images**: ไฟล์รูปภาพ (jpg, png, gif, heic, svg, ฯลฯ)
  - **Documents**: เอกสาร (pdf, doc, xlsx, ppt, ฯลฯ)
  - **Videos**: วิดีโอ (mp4, avi, mkv, mov, ฯลฯ)
  - **Music**: ไฟล์เสียง (mp3, wav, flac, ฯลฯ)
  - **Archives**: ไฟล์บีบอัด (zip, rar, tar, dmg, ฯลฯ)
  - **Web_Development**: ไฟล์พัฒนาเว็บ (html, css, js, php, ฯลฯ)
  - **Scripts_and_Code**: โค้ดและสคริปต์ (py, sh, java, swift, ฯลฯ)
  - **Data_and_Config**: ไฟล์ข้อมูลและการตั้งค่า (json, xml, yml, md, ฯลฯ)
  - **Database**: ไฟล์ฐานข้อมูล (sql, db, sqlite, ฯลฯ)
  - **Executables_and_Fonts**: โปรแกรมและฟอนต์ (exe, app, ttf, ฯลฯ)
- สร้างโฟลเดอร์อัตโนมัติหากยังไม่มี
- ไม่กระทบกับโฟลเดอร์ย่อยที่มีอยู่แล้ว

## ความต้องการ

- Python 3.x
- ไม่ต้องติดตั้ง library เพิ่มเติม (ใช้ `os` และ `shutil` ที่มีมาในตัว)

## การใช้งาน

1. แก้ไขตัวแปร `source_dir` ใน [script.py](script.py) ให้ชี้ไปยังโฟลเดอร์ที่ต้องการจัดระเบียบ:
   ```python
   source_dir = '/Users/aomsirawit/Downloads'
   ```

2. รันสคริปต์:
   ```bash
   python3 script.py
   ```

3. โปรแกรมจะย้ายไฟล์เข้าโฟลเดอร์ตามประเภทโดยอัตโนมัติ

## การปรับแต่ง

คุณสามารถเพิ่มนามสกุลไฟล์หรือประเภทโฟลเดอร์ใหม่ได้ใน dictionary `file_types`:

```python
file_types = {
    'ชื่อโฟลเดอร์': ['.นามสกุล1', '.นามสกุล2', ...],
    # ...
}
```

## ตัวอย่างผลลัพธ์

```
Moved: document.pdf to Documents
Moved: photo.jpg to Images
Moved: video.mp4 to Videos
Moved: script.py to Scripts_and_Code
```

## ข้อควรระวัง

- สคริปต์จะข้ามโฟลเดอร์ย่อยที่มีอยู่แล้วใน Downloads
- หากมีไฟล์ชื่อซ้ำในโฟลเดอร์ปลายทาง อาจมีการเขียนทับไฟล์เดิม
- แนะนำให้สำรองข้อมูลสำคัญก่อนรันครั้งแรก

## License

MIT License - ดูรายละเอียดใน [LICENSE](LICENSE)

## ผู้พัฒนา

AomSirawit
