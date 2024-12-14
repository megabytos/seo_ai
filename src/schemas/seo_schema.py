from typing import Optional, List

from pydantic import BaseModel, Field
from enum import Enum


class Languages(str, Enum):
    """
    Enum for user languages
    """

    UA = "ukrainian"
    EN = "english"


class AIModel(str, Enum):
    """
    Enum for AI models
    """

    GPT_4O_MINI = "gpt-4o-mini"
    GPT_3_5 = "gpt-3.5-turbo"
    GPT_4O = "gpt-4o"


class PromptModel(BaseModel):
    api_key: str = Field(min_length=2, max_length=550)
    model: AIModel
    lang: Languages
    topic: str = Field(min_length=5, max_length=100)
    symbols_count: int = Field(min=100, default=100)
    keywords_frequency: float = Field(ge=1.0, le=8.0)
    keywords: List[str] = Field(min_items=1)
    style: str = Field(min_length=5, max_length=100)
    worker: Optional[str] = Field(min_length=5, max_length=100)


class OutputBlogModel(BaseModel):
    content: str
