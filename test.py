import asyncio

from src.conf.config import settings
from src.services.llm import GPT

if __name__ == '__main__':
    gpt_agent = GPT(api_key=settings.openai_api_key)
    lang = 'ukrainian'
    topic = "Кетчуп 'Торчин' - кетчуп з найкращих томатів до вашого столу"
    symbols_count = 500
    keywords = ['Торчин', 'кетчуп', 'томати']
    keywords_frequency = 8
    style = 'Продаючій'

    prompt = f"""Write SEO text for a blog in {lang} language with a length of approximately {symbols_count} characters on the topic "{topic}".\n\
    Use the following keywords: {', '.join(keywords)}. The frequency of repetition of keywords should be {keywords_frequency}.\n\
    The style of the text should be {style}."""
    print(prompt)
    answer = asyncio.run(gpt_agent.get_response(prompt=prompt))

    print(answer)
