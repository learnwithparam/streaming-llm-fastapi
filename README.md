# Streaming LLM Applications with FastAPI

![learnwithparam.com](https://www.learnwithparam.com/ai-bootcamp/opengraph-image)

Build an AI story generator that adapts to user input. Learn to stream LLM responses in real-time with Server-Sent Events, master temperature and max_tokens for creativity control, and implement content safety guardrails.

> Start learning at [learnwithparam.com](https://learnwithparam.com). Regional pricing available with discounts of up to 60%.

## What You'll Learn

- Stream LLM responses in real-time using Server-Sent Events (SSE)
- Master temperature and max_tokens to control creativity and output length
- Build effective prompts using proven patterns and structures
- Handle streaming responses and update UI in real-time
- Implement the Provider Pattern for multi-model support

## Tech Stack

- **FastAPI** - High-performance async Python web framework
- **Server-Sent Events** - Real-time streaming protocol
- **LLM Provider Pattern** - Supports Fireworks, OpenRouter, Gemini, OpenAI
- **Pydantic** - Data validation and type safety
- **Docker** - Containerized development

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (installed automatically by `make setup`)
- An API key from any supported LLM provider

### Quick Start

```bash
# One command to set up and run
make dev

# Or step by step:
make setup          # Create .env and install dependencies
# Edit .env with your API key
make run            # Start the FastAPI server
```

### With Docker

```bash
make build          # Build the Docker image
make up             # Start the container
make logs           # View logs
make down           # Stop the container
```

### API Documentation

Once running, open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Challenges

Work through these incrementally to build the full application:

1. **The First Story** - Basic API call to an LLM
2. **The Reliable Story** - Prompt engineering (role, context, format)
3. **The Creative Story** - Temperature, top_p, max_tokens control
4. **The Real-Time Story** - Streaming with Server-Sent Events
5. **The Safe Story** - Input validation and content guardrails
6. **The Complex Story** - Advanced prompting (few-shot, chain-of-thought)
7. **The Polished Story** - Pre/post-processing pipelines
8. **The Continuing Story** - Context and memory (bonus)

## Makefile Targets

```
make help           Show all available commands
make setup          Initial setup (create .env, install deps)
make dev            Setup and run (one command!)
make run            Start FastAPI server
make build          Build Docker image
make up             Start container
make down           Stop container
make clean          Remove venv and cache
```

## Learn more

- Start the course: [learnwithparam.com/courses/streaming-llm-applications](https://www.learnwithparam.com/courses/streaming-llm-applications)
- AI Bootcamp for Software Engineers: [learnwithparam.com/ai-bootcamp](https://www.learnwithparam.com/ai-bootcamp)
- All courses: [learnwithparam.com/courses](https://www.learnwithparam.com/courses)
