import os
import argparse

try:
    import openai
except ImportError:
    openai = None
    print(
        "Warning: 'openai' package is not installed. Using fallback prompt generation."
    )

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if openai is not None:
    if OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
    else:
        print(
            "Warning: OPENAI_API_KEY not set. Falling back to simple prompt generation."
        )
        openai = None

# Interface messages and sample test prompts in English and Vietnamese
MESSAGES = {
    "en": {
        "enter": "Enter your video topic (or 'q' to quit): ",
        "empty": "Please provide a topic.\n",
        "generating": "\nGenerating AI video prompt...\n",
        "prompt": "Prompt:\n",
        "tests": "Here are some test prompts you can try in Veo3:",
    },
    "vi": {
        "enter": "Nh\u1eadp ch\u1ee7 \u0111\u1ec1 video (ho\u1eb7c 'q' \u0111\u1ec3 tho\u00e1t): ",
        "empty": "Vui l\u00f2ng nh\u1eadp ch\u1ee7 \u0111\u1ec1.\n",
        "generating": "\n\u0110ang t\u1ea1o prompt AI cho video...\n",
        "prompt": "Prompt:\n",
        "tests": "M\u1ed9t s\u1ed1 prompt th\u1eed b\u1ea1n c\u00f3 th\u1ec3 d\u00f9ng v\u1edbi Veo3:",
    },
}

TEST_PROMPTS = {
    "en": [
        "Landscape timelapse of a sunset over the mountains",
        "Abstract shapes morphing with vibrant neon colors",
        "Slow-motion close-up of raindrops on a window",
    ],
    "vi": [
        "C\u1ea3nh time-lapse ho\u00e0ng h\u00f4n tr\u00ean d\u00e3y n\u00fai",
        "H\u00ecnh kh\u1ed1i tr\u1ee3u t\u01b0\u1ee3ng bi\u1ebfn \u0111\u1ed5i v\u1edbi m\u00e0u neon r\u1ef1c r\u1ee1",
        "Chuy\u1ec3n \u0111\u1ed9ng ch\u1eadm c\u1eadn c\u1ea3nh gi\u1ecdt m\u01b0a tr\u00ean c\u1eeda s\u1ed5",
    ],
}

def generate_video_prompt(topic: str, lang: str) -> str:
    """Generate a video prompt using OpenAI if available."""
    if openai is None:
        if lang == "vi":
            return f"T\u1ea1o video Veo3 AI v\u1ec1 {topic}, t\u1eadp trung v\u00e0o h\u00ecnh \u1ea3nh ch\u00ednh v\u00e0 chuy\u1ec3n c\u1ea3nh m\u01b0\u1ee3t m\u00e0."
        return f"Create a Veo3 AI video about {topic}, focusing on key visuals and smooth transitions."

    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant specialized in writing video prompts for the Veo3 AI video platform." + (" Respond in Vietnamese." if lang == "vi" else ""),
            },
            {"role": "user", "content": f"Create a detailed video prompt about {topic}."},
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as exc:
        print("Error contacting OpenAI:", exc)
        return f"Create a Veo3 AI video about {topic}."

def suggest_test_prompts(lang: str) -> list:
    """Return a few example prompts users can test"""
    return TEST_PROMPTS[lang]


def parse_args():
    parser = argparse.ArgumentParser(description="AI Video Prompt Generator")
    parser.add_argument(
        "--lang",
        choices=["en", "vi"],
        default="en",
        help="Interface language",
    )
    return parser.parse_args()


def main() -> None:
    """Run an interactive prompt generator session."""
    args = parse_args()
    lang = args.lang
    msg = MESSAGES[lang]
    while True:
        topic = input(msg["enter"]).strip()
        if topic.lower() in {"q", "quit", "exit"}:
            break
        if not topic:
            print(msg["empty"])
            continue

        print(msg["generating"])
        try:
            prompt = generate_video_prompt(topic, lang)
        except Exception as exc:
            print("Error generating prompt:", exc)
            break

        print(msg["prompt"], prompt, "\n")
        print(msg["tests"])
        for test in suggest_test_prompts(lang):
            print("-", test)
        print()


if __name__ == "__main__":
    main()
