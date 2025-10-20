from src.agents.grader_agent import agent, GradeDocuments, GRADE_PROMPT

def grader_tool(query: str, chunks: list[str]) -> dict:
    """
    A tool to grade the AI's response based on the provided context chunks.
    """

    prompt = GRADE_PROMPT.format(question=query, context=chunks)

    result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})

    if isinstance(result["structured_response"], GradeDocuments):
        if result["structured_response"].binary_score.lower() == 'yes':
            return "The retrieved chunks/context is relevant to the user query."
    else:
        return "The retrieved chunks/context is not relevant to the user query. Retry by refining the query."