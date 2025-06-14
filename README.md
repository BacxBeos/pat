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

Run the script and enter a topic when prompted:

```bash
python prompt_app.py
```

The script will generate a prompt for the given topic and display a few suggested prompts that you can try directly in Veo3.

## Disclaimer

This script calls the OpenAI API. If running inside a restricted environment without internet access, the API request will fail.
