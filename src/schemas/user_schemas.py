"""Pydantic schemas for LLM response."""

from enum import Enum
from pydantic import BaseModel, Field


class Sentiment(str, Enum):
    like = "like"
    dislike = "dislike"
    neutral = "neutral"


class ResponseNecessity(str, Enum):
    yes = "yes"
    no = "no"


class Crisis(str, Enum):
    yes = "yes"
    no = "no"


class UserMessageStatus(BaseModel):
    sentiment: Sentiment = Field(
        ...,
        description="Sentiment of the user toward the received message. One of: 'like', 'dislike', 'neutral'.",
    )
    response_necessity: ResponseNecessity = Field(
        ...,
        description="Whether the user requires a response. One of: 'yes', 'no'.",
    )
    crisis: Crisis = Field(
        ...,
        description="Whether the user is in immediate distress or crisis. One of: 'yes', 'no'.",
    )
