
import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(current_dir):
    if filename.endswith(('.jpg','.png','.gif')):
        os.makedirs('Images', exist_ok=True)
        shutil.move(filename, 'Images')
    elif filename.endswith(('.mp3','.wav','.flac')):
        os.makedirs('Audio', exist_ok=True)
        shutil.move(filename, 'Audio')
    elif filename.endswith(('.mp4','.mov','.avi')):
        os.makedirs('Video', exist_ok=True)
        shutil.move(filename, 'Video')
    elif filename.endswith(('.doc','.docx','.pdf','.txt')):
        os.makedirs('Documents', exist_ok=True)
        shutil.move(filename, 'Documents')
    elif filename.endswith(('.zip','.rar')):
        os.makedirs('Compressed', exist_ok=True)
        shutil.move(filename, 'Compressed')
    elif filename.endswith('.exe'):
        os.makedirs('Executables', exist_ok=True    )
        shutil.move(filename, 'Executables')

print("all done")