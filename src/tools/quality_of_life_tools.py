from langchain.tools import tool

@tool
def clarify(question: str) -> dict:
    """
    Ask user for clarification when input is ambiguous or incomplete.
    
    Args:
        question: Specific question to resolve ambiguity
        
    Returns:
        dict with 'question' key for the LLM to present to user
    """
    return {"action": "clarify", "question": question}

@tool
def confirm_action(action: str, details: dict) -> dict:
    """
    Request user confirmation before executing sensitive operations.
    
    Args:
        action: Description of action to confirm
        details: Relevant context for the action
        
    Returns:
        dict with confirmation prompt
    """
    return {"action": "confirm", "operation": action, "details": details}

@tool
def flag_content(reason: str, severity: str) -> dict:
    """
    Flag potentially harmful or policy-violating content.
    
    Args:
        reason: Why content is flagged
        severity: 'low' | 'medium' | 'high' | 'critical'
        
    Returns:
        dict with flag metadata
    """
    return {"action": "flag", "reason": reason, "severity": severity}

@tool
def suggest_alternative(original_query: str, alternatives: list[str]) -> dict:
    """
    Offer alternatives when original request cannot be fulfilled.
    
    Args:
        original_query: The original user request
        alternatives: List of viable alternatives
        
    Returns:
        dict with suggestions
    """
    return {"action": "suggest", "original": original_query, "alternatives": alternatives}

@tool
def request_context(missing_info: list[str]) -> dict:
    """
    Request additional context needed to complete task.
    
    Args:
        missing_info: List of specific information needed
        
    Returns:
        dict with context request
    """
    return {"action": "context", "needed": missing_info}