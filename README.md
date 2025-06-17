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

Phản hồi của ứng dụng sẽ hiển thị bằng cả tiếng Việt và tiếng Anh để bạn dễ
dàng theo dõi.

Ứng dụng sẽ liên tục hỏi bạn nhập chủ đề video cho tới khi bạn nhập `q` để thoát. Với mỗi chủ đề, ứng dụng tạo prompt và gợi ý một số prompt mẫu để thử ngay trên Veo3.

## Lưu ý

Nếu thiếu gói `openai` hoặc API key, ứng dụng chỉ tạo prompt dự phòng. Khi có kết nối và API key, ứng dụng sẽ gọi OpenAI để sinh prompt chi tiết.

## Chạy kiểm thử

File `test_prompt_app.py` cung cấp một số bài kiểm thử đơn giản. Bạn có thể chạy bằng lệnh:

```bash
python -m unittest test_prompt_app.py
```

Các kiểm thử sử dụng mô hình giả lập nên không cần cài `openai`.

## Tạo file thực thi (.exe)

Để đóng gói ứng dụng thành tệp `.exe` chạy trên Windows, cài đặt `pyinstaller`:

```bash
pip install pyinstaller
```

Sau đó chạy lệnh sau trong thư mục dự án:

```bash
pyinstaller --onefile prompt_app.py
```

Lệnh trên tạo thư mục `dist` chứa file `prompt_app.exe`. Bạn có thể gửi file này cho người dùng Windows để chạy trực tiếp.
