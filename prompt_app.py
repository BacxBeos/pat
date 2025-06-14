import os

try:
    import openai
except ImportError as exc:
    openai = None
    OPENAI_IMPORT_ERROR = exc
else:
    OPENAI_IMPORT_ERROR = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if openai is None:
    raise ImportError(
        "The 'openai' package is required. Install it with 'pip install openai'."
    )

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    raise EnvironmentError(
        "Please set the OPENAI_API_KEY environment variable to your OpenAI key"
    )

def generate_video_prompt(topic: str) -> str:
    """Generate a video prompt for Veo3 using OpenAI GPT"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in writing video prompts for the Veo3 AI video platform."},
            {"role": "user", "content": f"Create a detailed video prompt about {topic}."}
        ],
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()

def suggest_test_prompts() -> list:
    """Return a few example prompts users can test"""
    return [
        "Landscape timelapse of a sunset over the mountains",
        "Abstract shapes morphing with vibrant neon colors",
        "Slow-motion close-up of raindrops on a window",
    ]


def main() -> None:
    """Run an interactive prompt generator session."""
    while True:
        topic = input("Enter your video topic (or 'q' to quit): ").strip()
        if topic.lower() in {"q", "quit", "exit"}:
            break
        if not topic:
            print("Please provide a topic.\n")
            continue

        print("\nGenerating AI video prompt...\n")
        try:
            prompt = generate_video_prompt(topic)
        except Exception as exc:
            print("Error generating prompt:", exc)
            break

        print("Prompt:\n", prompt, "\n")
        print("Here are some test prompts you can try in Veo3:")
        for test in suggest_test_prompts():
            print("-", test)
        print()


if __name__ == "__main__":
    main()
