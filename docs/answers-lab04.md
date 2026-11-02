# Lab 04 – Câu hỏi

1. **Vì sao chuẩn bị trên `master` trước, không sửa trên nhánh release?** `master` là nơi phát triển tiếp. Nhánh release cần giữ đúng phiên bản được phát hành; sửa trực tiếp sẽ làm thay đổi baseline.
2. **Vì sao `release/*` không merge ngược vào `master`? So với GitFlow?** Nhánh release chỉ giữ bản đã phát hành, còn tính năng mới nằm trên `master`; merge ngược có thể đưa trạng thái cũ vào `master`. GitFlow thường có `develop` và merge nhánh release về cả `main` lẫn `develop`.
3. **Vì sao lên `1.0.0`, không phải `0.4.0`?** `1.0.0` đánh dấu phiên bản ổn định đầu tiên, sẵn sàng dùng. `0.4.0` vẫn thể hiện phần mềm đang trong giai đoạn chưa ổn định.
