import os

try:
    import openai
except ImportError:
    openai = None
    print(
        "Cảnh báo: chưa cài đặt gói 'openai'. Dùng cách tạo prompt dự phòng."
    )

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if openai is not None:
    if OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
    else:
        print(
            "Cảnh báo: OPENAI_API_KEY chưa thiết lập. Dùng cách tạo prompt đơn giản."
        )
        openai = None

# Thông điệp giao diện và các prompt mẫu
MESSAGES = {
    "enter": "Nhập chủ đề video (hoặc 'q' để thoát): ",
    "empty": "Vui lòng nhập chủ đề.\n",
    "generating": "\nĐang tạo prompt AI cho video...\n",
    "prompt": "Prompt:\n",
    "tests": "Một số prompt thử bạn có thể dùng với Veo3:",
}

TEST_PROMPTS = [
    "Cảnh time-lapse hoàng hôn trên dãy núi",
    "Hình khối trợu tượng biến đổi với màu neon rực rỡ",
    "Chuyển động chậm cận cảnh giọt mưa trên cửa sổ",
]

def generate_video_prompt(topic: str) -> str:
    """Tạo prompt video sử dụng OpenAI nếu có."""
    if openai is None:
        return (
            f"Tạo video Veo3 AI về {topic}, tập trung vào hình ảnh chính và chuyển cảnh mượt mà."
        )

    try:
        messages = [
            {
                "role": "system",
                "content": "Bạn là trợ lý chuyên viết prompt video cho nền tảng Veo3 AI. Trả lời bằng tiếng Việt.",
            },
            {"role": "user", "content": f"Tạo prompt chi tiết cho video về {topic}."},
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as exc:
        print("Lỗi kết nối OpenAI:", exc)
        return f"Tạo video Veo3 AI về {topic}."

def suggest_test_prompts() -> list:
    """Trả về một số prompt mẫu"""
    return TEST_PROMPTS


def main() -> None:
    """Chạy vòng lặp sinh prompt video."""
    msg = MESSAGES
    while True:
        topic = input(msg["enter"]).strip()
        if topic.lower() in {"q", "quit", "exit"}:
            break
        if not topic:
            print(msg["empty"])
            continue

        print(msg["generating"])
        try:
            prompt = generate_video_prompt(topic)
        except Exception as exc:
            print("Lỗi tạo prompt:", exc)
            break

        print(msg["prompt"], prompt, "\n")
        print(msg["tests"])
        for test in suggest_test_prompts():
            print("-", test)
        print()


if __name__ == "__main__":
    main()
