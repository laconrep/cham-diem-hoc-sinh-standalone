# HỆ THỐNG SUB-AGENT CHẤM ĐIỂM BÀI THI TOÁN HỌC (THPT, CĐN01)
> **Chủ nhiệm hệ thống**: ThS. Nguyễn Văn Sang - Khoa Cơ bản - Trường Cao đẳng Nghề số 1 - BQP  
> **Sub-agent**: `cham-diem-hoc-sinh` (Gemini Multimodal Vision & Visual Red-Pen Logic)  
> **Tiêu chuẩn khảo thí**: Chương trình Giáo dục phổ thông (GDPT) 2018 - Cấu trúc đề 4 phần (Thang điểm 10)

---

## 📌 BẢN ĐỘC LẬP — NGUỒN GỐC & LƯU Ý

Repo này là bản độc lập, tách từ [sanginnova/cham-diem-hoc-sinh](https://github.com/sanginnova/cham-diem-hoc-sinh) (ThS. Nguyễn Văn Sang). So với bản gốc, bản này đã:

- **Gỡ toàn bộ đường dẫn cứng** (`D:\TOAN\...`, `C:\Users\ADMIN\...`) — mọi đường dẫn giờ tính tương đối từ thư mục repo qua `config.py`, chạy được trên bất kỳ máy nào.
- **Gỡ dữ liệu học sinh thật**: file Excel kết quả và danh sách 43 học sinh trong code đã được thay bằng 2 học sinh mẫu ẩn danh. Muốn chấm lớp của mình, thay danh sách mẫu trong `cham_diem_core.py` (`STUDENT_RESULTS`) bằng danh sách của bạn.
- **Link Google Drive** chuyển vào `config.py` (`DRIVE_FOLDER_URL`) — dán link thư mục của bạn vào đó trước khi chạy `sync_drive.py`.

> ⚖️ **Bản quyền**: bản gốc không có file LICENSE, tác giả giữ bản quyền theo mặc định. Bản độc lập này chỉ dùng cho mục đích cá nhân/học tập — **xin phép tác giả trước khi dùng lại, chia sẻ rộng rãi hay đưa vào sản phẩm khác.**

---

## 🌟 TỔNG QUAN

Hệ thống cung cấp giải pháp khép kín 100% tự động hóa chấm điểm bài thi Toán học từ ảnh chụp bài làm học sinh lưu trữ trên Google Drive:
1. **Tự động đồng bộ**: Tải và quản lý ảnh bài làm trực tiếp từ Google Drive (`sync_drive.py`).
2. **Mắt thần Gemini Vision**: Nhận diện thông tin học sinh, lớp, mã đề thi (101, 102, 103, 104), phân biệt chính xác vết chì tô thật và vết chì tẩy xóa mờ.
3. **Chấm trắc nghiệm Dead-Center (≤ 2px)**:
   - **Phần I (3,0đ)**: 12 câu ABCD - Khoanh tròn đỏ ôm khít tâm ô chì học sinh tô.
   - **Phần II (2,0đ)**: 2 câu Đúng/Sai (8 ý) theo barem phân bước chuẩn Bộ: 1 ý = 0,1đ; 2 ý = 0,25đ; 3 ý = 0,5đ; 4 ý = 1,0đ.
   - **Phần III (2,0đ)**: 4 câu Trả lời ngắn - Soi đối chiếu cả ô số viết tay và các cột OMR.
4. **Chấm tự luận Logic 4 bước (Phần IV - 3,0đ)**:
   - **Không chỉ nhìn đáp án**: Soi từng dòng biến đổi toán học, điều kiện xác định, quy tắc đạo hàm và lập luận cực trị.
   - **Phát hiện lỗi logic đại số & ngụy biện**: Chỉ rõ vị trí sai (`0,00đ [✗]`), đóng dấu điểm từng bước (`+0,25đ [✓]`) dóng thẳng hàng ở lề phải bài làm.
5. **Typography Tiếng Việt Có Dấu 100%**: Sử dụng Engine TrueType Arial Bold sắc nét, chuẩn mực Sư phạm.
6. **Báo cáo Excel Đa Tầng**: Tự động xuất file `Ket_Qua_Cham_Diem_Giua_Ky_1_Lop12.xlsx` gồm 4 sheet chi tiết kèm Sheet tô màu đối soát từng câu.

---

## 📂 CẤU TRÚC REPOSITORY

```text
├── SKILL.md                      # Định nghĩa Sub-agent chuẩn Antigravity
├── cham_diem_core.py             # Engine chấm điểm, đối soát đáp án và xuất Excel 4 Sheet
├── tao_bo_anh_da_cham.py         # Engine xuất bộ ảnh đã chấm đỏ (Typography có dấu & Logic)
├── sync_drive.py                 # Module đồng bộ ảnh bài làm từ Google Drive
├── CHAY_CHAM_DIEM.bat            # Script chạy tự động 1-click dành cho Giáo viên
├── Ket_Qua_Cham_Diem_...xlsx     # File báo cáo kết quả chi tiết
└── docs/
    └── samples/                  # Ảnh mẫu bài làm đã chấm đỏ trực quan
```

---

## 🚀 HƯỚNG DẪN SỬ DỤNG

### 0. Cài đặt lần đầu
```bash
# Cài thư viện Python
pip install -r requirements.txt

# Cài thêm phần mềm Tesseract OCR (ocr_de.py cần):
# - Windows: tải tại https://github.com/UB-Mannheim/tesseract/wiki
# - Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-vie
```

Mở `config.py` và dán link thư mục Google Drive chứa ảnh bài làm vào `DRIVE_FOLDER_URL` (để trống thì `sync_drive.py` sẽ báo và dừng lại).

### 1. Chạy 1-Click tự động
Giáo viên chỉ cần nhấp đúp vào:
```cmd
CHAY_CHAM_DIEM.bat
```

### 2. Chạy qua Command Line
```bash
# 1. Đồng bộ ảnh bài làm từ Google Drive
python sync_drive.py

# 2. Chấm điểm và xuất báo cáo Excel
python cham_diem_core.py

# 3. Xuất toàn bộ ảnh bài làm đã chấm đỏ sư phạm
python tao_bo_anh_da_cham.py
```

---

## ⚖️ BẢN QUYỀN
Hệ thống được thiết kế và phát triển bởi **ThS. Nguyễn Văn Sang** - Khoa Cơ bản - Trường Cao đẳng Nghề số 1 - BQP.

