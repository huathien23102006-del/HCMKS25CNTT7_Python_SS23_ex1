"""
Phần 1: Phân tích & Tái cấu trúc thư mục (Architecture Review)
Vì sao from math import * là Anti-pattern?

Nó nhập toàn bộ hàm, hằng số của math vào namespace hiện tại → dễ gây xung đột tên (ví dụ: sqrt có thể bị ghi đè).

Làm mất tính tường minh: khi đọc code, không biết hàm đến từ đâu.

Gây khó khăn cho việc bảo trì và debug.

Cách tốt hơn:
import math
# hoặc chỉ import hàm cần dùng
from math import sqrt
Tệp đặc biệt để biến thư mục thành Package trong Python

Đó là __init__.py.

Vai trò: đánh dấu thư mục là một Python Package, cho phép import các module bên trong. Có thể chứa logic khởi tạo hoặc để trống.

Sơ đồ cây thư mục sau khi tối ưu hóa

rikkei_logistics/
├── core/
│   ├── __init__.py
│   ├── geo_calculator.py
│   └── time_estimator.py
├── utils/
│   ├── __init__.py
│   └── file_helper.py
├── main.py
└── shipments_data.py   # (tuỳ chọn, tách dữ liệu ra riêng)
Phần 2: Triển khai Code sạch & Modularization
"""

from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
import datetime

shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00",
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00",
    },
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

if create_log_dir("logs"):
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
else:
    print("[INFO] Thư mục log đã tồn tại, bỏ qua.")

print("---------------------------------------------------------------------------")

for s in shipments:
    distance = calculate_distance(
        s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"]
    )
    eta = predict_eta(s["depart"], distance)
    deadline = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")

    status = (
        "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
        if eta <= deadline
        else "🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc "
        + deadline.strftime("%H:%M:%S")
        + ")"
    )

    print(f"[CHUYẾN XE {s['id']}]")
    print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
    print(f" + Thời gian khởi hành: {s['depart']}")
    print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" + Trạng thái: {status}\n")

print("========================================================")
