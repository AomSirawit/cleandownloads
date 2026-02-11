import os
import shutil

source_dir = 'your_path'

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

if not os.path.exists(source_dir):
    print(f"Error: ไม่พบโฟลเดอร์ {source_dir}")
else:
    print(f"Start organizing: {source_dir}")
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # ข้ามถ้าเป็นโฟลเดอร์
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        
        target_folder_name = 'Others' 
        for folder, ext_list in file_types.items():
            if file_ext in ext_list:
                target_folder_name = folder
                break 
        
        # เริ่มกระบวนการย้าย
        target_folder = os.path.join(source_dir, target_folder_name)
        
        # สร้างโฟลเดอร์ถ้ายังไม่มี
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # ป้องกันชื่อซ้ำ (Running number)
        base_name = os.path.splitext(filename)[0]
        new_filename = filename
        counter = 1
        while os.path.exists(os.path.join(target_folder, new_filename)):
            new_filename = f"{base_name}({counter}){file_ext}"
            counter += 1

        destination_path = os.path.join(target_folder, new_filename)

        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} -> {target_folder_name}/{new_filename}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

    print("เสร็จสิ้น!")