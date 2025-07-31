import os

# تأكد إن الملف هذا موجود مع السكربت
file_path = "test.py"

# 775 = rwxrwxr-x
os.chmod(file_path, 0o775)

print(f"Permissions for '{file_path}' changed to rwxrwxr-x (775)")
