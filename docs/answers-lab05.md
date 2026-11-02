# Lab 05 – Câu hỏi

1. **Vì sao không merge cả nhánh hotfix vào `master`?** Nhánh hotfix có cả commit tăng phiên bản `1.0.1`, có thể xung đột với phiên bản `1.1.0` trên `master`. Chỉ cherry-pick commit sửa lỗi để đưa đúng phần cần thiết.
2. **Vì sao Phần A chưa gắn tag `v1.1.0`?** Vì còn phải đưa hotfix vào `release/lab05`. Gắn tag sớm sẽ cố định một bản chưa có sửa lỗi; sau đó phải phát hành thêm `v1.1.1`.
3. **Upstream first so với release first có ưu, nhược điểm gì?** Upstream first sửa và kiểm thử trên `master` trước, rồi lan truyền sang các bản phát hành: dễ quản lý một bản sửa chung nhưng có thể khó áp dụng vào bản cũ. Release first sửa trực tiếp trên phiên bản đã phát hành: phù hợp vá bản cũ nhưng cần lan truyền cẩn thận để các nhánh không lệch nhau.
4. **Quên lan truyền bản sửa sang `release/lab05`, lệnh nào phát hiện?** Vòng lặp kiểm tra ở Phần F, chạy lần lượt trên `v1.0.1`, `v1.1.0` và `master`. Nếu `v1.1.0` không in ra `1`, bản sửa chưa có trên release đó.
