from langchain.agents import create_agent
from src.llm_config.chat_model import response_model as llm
from pydantic import BaseModel, Field
from langchain.agents.structured_output import ToolStrategy
from typing import Literal

class GradeDocuments(BaseModel):  
    """Grade documents using a binary score for relevance check."""

    binary_score: Literal["yes", "no"] = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
    )

GRADE_PROMPT = (
    "You are a grader assessing relevance of a retrieved document to a user question. \n "
    "Here is the retrieved document: \n\n {context} \n\n"
    "Here is the user question: {question} \n"
    "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n"
    "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."
)

agent = create_agent(
    llm, 
    system_prompt=GRADE_PROMPT,
    response_format=ToolStrategy(GradeDocuments)
)