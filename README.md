# Ableton Agent Project Documentation

## Overview
Ableton Agent is a Python-based project designed to provide intelligent agents for various tasks. It includes tools, middleware, and configurations for seamless integration and functionality.

## Project Structure
The project is organized as follows:

```
ableton_agent/
├── .gitignore
├── .python-version
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── uv.lock
├── src/
│   ├── agents/
│   │   ├── grader_agent.py
│   │   ├── retrival_agent.py
│   ├── llm_config/
│   │   ├── chat_model.py
│   │   ├── embedding_model.py
│   │   ├── vector_store_config.py
│   ├── middleware/
│   │   ├── tool_error_handling.py
│   ├── prompts/
│   │   ├── generate_response_prompt.md
│   │   ├── grader_prompt.md
│   │   ├── prompt_loader.py
│   ├── tools/
│   │   ├── grader_tool.py
│   │   ├── quality_of_life_tools.py
│   │   ├── retrieval_tool.py
```

## Key Components

### Agents
- **grader_agent.py**: Handles grading tasks.
- **retrival_agent.py**: Manages retrieval operations.

### LLM Configuration
- **chat_model.py**: Configuration for chat-based models.
- **embedding_model.py**: Handles embedding models.
- **vector_store_config.py**: Configuration for vector storage.

### Middleware
- **tool_error_handling.py**: Middleware for managing tool errors.

### Prompts
- **generate_response_prompt.md**: Template for generating responses.
- **grader_prompt.md**: Template for grading tasks.
- **prompt_loader.py**: Loads and manages prompts.

### Tools
- **grader_tool.py**: Tool for grading operations.
- **quality_of_life_tools.py**: Tools for enhancing user experience.
- **retrieval_tool.py**: Tool for retrieval tasks.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/VajraM-dev/ABLTN.AI.git
   ```
2. Navigate to the project directory:
   ```
   cd ableton_agent
   ```
3. Install dependencies:
   ```
   uv sync
   ```

## Usage
Run the main script to start the application:
```
uv run main.py
```

## Future Work
- Improving the quality of results.
- Adding Web Search Agent
- Adding Capability to Search Youtube Tutorials and Suggest Tips and Tricks.
- Making it Deployment ready with FastAPI, Docker. 
- We are also planning to release the agent as paid service.
- There are also plans to integrate the agent with Max For Live to make it easily accessible in Ableton. 