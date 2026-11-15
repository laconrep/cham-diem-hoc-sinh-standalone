# -*- coding: utf-8 -*-
"""
Cấu hình dùng chung cho hệ thống chấm điểm Toán 12.

Mọi đường dẫn đều tính tương đối từ thư mục chứa file này (BASE_DIR),
nên repo chạy được trên bất kỳ máy nào mà không cần sửa code.
Chỉ cần sửa các giá trị dưới đây (hoặc để mặc định).
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Thư mục ảnh bài làm (đầu vào) và ảnh đã chấm đỏ (đầu ra)
ANH_BAI_LAM_DIR = BASE_DIR / "anh_bai_lam"
ANH_DA_CHAM_DIR = BASE_DIR / "anh_da_cham"

# File Excel báo cáo kết quả (được tạo mới mỗi lần chạy cham_diem_core.py)
EXCEL_PATH = BASE_DIR / "Ket_Qua_Cham_Diem_Giua_Ky_1_Lop12.xlsx"

# Link thư mục Google Drive chứa ảnh bài làm (sync_drive.py dùng link này).
# Dán link thư mục Drive của bạn vào đây. Để trống thì sync_drive.py sẽ
# báo và dừng lại thay vì tải nhầm thư mục của người khác.
DRIVE_FOLDER_URL = ""
