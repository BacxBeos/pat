import unittest
import prompt_app

class TestPromptApp(unittest.TestCase):
    def test_generate_without_openai(self):
        saved_openai = prompt_app.openai
        prompt_app.openai = None
        try:
            topic = "chủ đề thử"
            result = prompt_app.generate_video_prompt(topic)
            self.assertIn(topic, result)
        finally:
            prompt_app.openai = saved_openai

    def test_suggest_test_prompts(self):
        prompts = prompt_app.suggest_test_prompts()
        self.assertIsInstance(prompts, list)
        self.assertTrue(len(prompts) > 0)

    def test_generate_with_openai_stub(self):
        class DummyCompletion:
            @staticmethod
            def create(model, messages, max_tokens):
                return type('Response', (), {
                    'choices': [type('Choice', (), {'message': {'content': 'ok'}})()]
                })()

        class DummyOpenAI:
            ChatCompletion = DummyCompletion

        saved_openai = prompt_app.openai
        prompt_app.openai = DummyOpenAI()
        try:
            result = prompt_app.generate_video_prompt('chủ đề test')
            self.assertEqual(result, 'ok')
        finally:
            prompt_app.openai = saved_openai

if __name__ == '__main__':
    unittest.main()
