import os
import shutil

temp_dir = os.environ.get('TEMP')

if temp_dir:
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Hata: {e}")

print("Geçici dosyalar temizlendi.")
