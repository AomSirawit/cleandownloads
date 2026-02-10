import os
import shutil

# กำหนด folder ที่ต้องการจัดระเบียบ
source_dir = '/Users/aomsirawit/Downloads'

# กำหนดประเภทไฟล์และโฟลเดอร์เป้าหมาย
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.webp', '.svg', '.ico', '.raw'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.rtf', '.odt', '.pages', '.numbers', '.key'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm', '.vob'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.wma', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.pkg', '.dmg', '.iso'],
    'Web_Development': ['.html', '.css', '.scss', '.sass', '.js', '.ts', '.jsx', '.tsx', '.php', '.vue', '.blade.php'], 
    'Scripts_and_Code': ['.py', '.sh', '.bat', '.rb', '.go', '.c', '.cpp', '.java', '.swift'],
    'Data_and_Config': ['.json', '.xml', '.yml', '.yaml', '.md', '.ini', '.conf', '.env', '.log', '.geojson'],
    'Database': ['.sql', '.db', '.sqlite', '.sqlite3', '.dump'],
    'Executables_and_Fonts': ['.exe', '.msi', '.app', '.otf', '.ttf', '.woff', '.woff2'],
}

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # ข้ามโฟลเดอร์
    if os.path.isdir(file_path):
        continue

    # หานามสกุลไฟล์
    file_ext = os.path.splitext(filename)[1].lower()

    #ตรวจสอบและย้ายไฟล์
    moved = False   
    for folder, ext_list in file_types.items():
        if file_ext in ext_list:
            # สร้างโฟลเดอร์ถ้ายังไม่มี
            target_folder = os.path.join(source_dir, folder)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # ป้องกันบันทึกไฟล์ทับกัน
            base_name = os.path.splitext(filename)[0]
            new_filename = filename
            counter = 1

            while os.path.exists(os.path.join(target_folder, new_filename)):
                new_filename = f"{base_name}({counter}){file_ext}"
                counter += 1

            destination_path = os.path.join(target_folder, new_filename)

            # ย้ายไฟล์
            try: 
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} -> {folder}/{new_filename}")
            except Exception as e:
                print(f"Error moving file {filename}: {e}")

            moved = True
            break