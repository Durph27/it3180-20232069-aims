# Lab 02 – Câu hỏi

1. **Vì sao phải đồng bộ `master` trước khi tạo PR?** Để kiểm tra nhánh với thay đổi mới nhất, phát hiện xung đột sớm và chắc rằng các thay đổi vẫn hoạt động cùng nhau.
2. **Khi nào không được rebase?** Không rebase nhánh đã push và đang được người khác dùng, vì rebase viết lại lịch sử và có thể làm hỏng lịch sử của họ.
3. **`feature/*` khác `topic/*` ra sao?** `feature/*` chứa một tính năng của sản phẩm; `topic/*` thường chứa một việc nhỏ như tài liệu hoặc cấu hình. Cả hai đều làm trên nhánh riêng và đưa qua PR.
