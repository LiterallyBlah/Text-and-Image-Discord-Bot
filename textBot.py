import openai

class TextBot:
    def __init__(self, bot_name, ai_model):
        self.bot_name = bot_name
        self.ai_model = ai_model

    def get_response(self, conversation, prompt):
        # send conversation and prompt to openai
        response = openai.Completion.create(
            engine=self.ai_model,
            prompt=f"{conversation}\n{prompt}",
            max_tokens=1500,
            temperature=0.7,
            top_p=0.5
        )

        # format response
        response_text = response['choices'][0]['text']
        response_text = response_text.replace(f"{self.bot_name}: ", "")

        return response_text
