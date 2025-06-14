# AI Video Prompt Generator

This application helps generate prompts for the Veo3 AI video platform using OpenAI's GPT models. It can also suggest example prompts for testing.

## Requirements

- Python 3.8+
- `openai` Python package
- An OpenAI API key set in the `OPENAI_API_KEY` environment variable

Install dependencies:
```bash
pip install openai
```

## Usage

Run the interactive prompt generator:

```bash
python prompt_app.py
```

The app will keep asking for topics until you type `q` to quit. For each topic, it generates a prompt and lists a few suggested prompts you can test directly in Veo3.

## Disclaimer

This script calls the OpenAI API. If running inside a restricted environment without internet access, the API request will fail.
