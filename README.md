# Trình Tạo Prompt Video AI

Ứng dụng này hỗ trợ tạo prompt cho nền tảng Veo3 bằng cách sử dụng mô hình GPT của OpenAI (nếu có). Nếu không cài đặt `openai` hoặc không có API key, ứng dụng sẽ sử dụng mẫu prompt đơn giản.

## Yêu cầu
- Python 3.8+
- (Tùy chọn) gói `openai`
- (Tùy chọn) biến môi trường `OPENAI_API_KEY`

Cài đặt gói tùy chọn:
```bash
pip install openai
```

## Cách sử dụng

Chạy ứng dụng:
```bash
python prompt_app.py
```

Ứng dụng sẽ liên tục hỏi bạn nhập chủ đề video cho tới khi bạn nhập `q` để thoát. Với mỗi chủ đề, ứng dụng tạo prompt và gợi ý một số prompt mẫu để thử ngay trên Veo3.

## Lưu ý

Nếu thiếu gói `openai` hoặc API key, ứng dụng chỉ tạo prompt dự phòng. Khi có kết nối và API key, ứng dụng sẽ gọi OpenAI để sinh prompt chi tiết.
