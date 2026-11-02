# Lab 01 – Câu hỏi

1. **Vì sao dùng `git mv`?** Lệnh này vừa chuyển/đổi tên tệp, vừa đưa thay đổi vào Git để Git dễ theo dõi lịch sử tệp.
2. **`release/lab01` có phải baseline không?** Có. Đây là nhánh ghi lại trạng thái bài Lab 01 đã nộp.
3. **Vì sao không commit thẳng lên `master`, dù làm một mình?** Làm qua nhánh và PR giúp xem lại thay đổi, giữ lịch sử rõ ràng và tập đúng quy trình làm việc nhóm.
4. **`--global` được lưu ở đâu và khác `--local` thế nào?** `--global` lưu trong cấu hình người dùng (thường là `~/.gitconfig`) và áp dụng cho mọi repo của người dùng. `--local` lưu trong `.git/config` của repo hiện tại và chỉ áp dụng cho repo đó.
