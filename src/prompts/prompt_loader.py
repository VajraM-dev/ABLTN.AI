from string import Template

prompt_dict = {
    "response_prompt": "src/prompts/generate_response_prompt.md",
    "grading_prompt": "src/prompts/grader_prompt.md",
}

def load_system_prompt(prompt_location: str, additional_context: str = "") -> str:
    """Load and populate the system prompt template."""

    # Load template
    with open(prompt_dict[prompt_location]) as f:
        template = Template(f.read())

    # Populate
    system_prompt = template.substitute(
        additional_context=additional_context
    )

    return system_prompt