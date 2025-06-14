import os

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

def generate_video_prompt(topic: str) -> str:
    """Generate a video prompt using OpenAI if available."""
    if openai is None:
        return f"Create a Veo3 AI video about {topic}, focusing on key visuals and smooth transitions."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in writing video prompts for the Veo3 AI video platform."},
                {"role": "user", "content": f"Create a detailed video prompt about {topic}."}
            ],
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as exc:
        print("Error contacting OpenAI:", exc)
        return f"Create a Veo3 AI video about {topic}."

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
