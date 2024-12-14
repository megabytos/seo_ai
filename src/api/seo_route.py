from fastapi import APIRouter

from src.services.llm import GPT
from src.schemas.seo_schema import PromptModel, OutputBlogModel

router = APIRouter(prefix="/seo", tags=["seo"])


@router.post("/generate_blog", response_model=OutputBlogModel)
async def generate_blog(request: PromptModel):
    print(request)

    gpt_agent = GPT(api_key=request.api_key)
    prompt = f"""Write SEO text for a blog in {request.lang} language with a length of approximately {request.symbols_count} characters on the topic "{request.topic}".\n\
    Use the following keywords: {', '.join(request.keywords)}. The frequency of repetition of keywords should be {request.keywords_frequency}.\n\
    The style of the text should be {request.style}."""

    print(prompt)
    answer = await gpt_agent.get_response(prompt=prompt)

    return {"content": answer}
