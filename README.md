# AI-Zoomcamp
AI-assisted development projects covering React/TS, FastAPI, Django agents, MCP workflows, CI/CD automation, and n8n low-code AI workflows.

# Snake-Game

This project was built as part of an AI coding course focused on **AI-assisted development**.  
The goal was to practice using modern AI tools to generate, debug, and build a full React application.

## Tools Used
- **ChatGPT / Claude / DeepSeek** – coding assistance & debugging  
- **GitHub Copilot / Cursor** – in-editor AI suggestions  
- **Bolt / Lovable** – project bootstrapping  
- **Vite + React** – frontend framework and dev environment  
- **Tailwind CSS** (optional) – UI styling

## How to Run
npm install
npm run dev

## Anthropic Computer Use – AI Agent Automation

As part of this project, I explored **Anthropic’s Computer Use agent**, an advanced demo that runs a full virtual desktop inside Docker and allows an AI model to interact with the system like a human. This setup enabled Claude to open files, edit code, navigate the UI, and automate multi-step tasks inside a simulated computer environment.

This experimentation helped me understand how next-generation AI agents can support engineering workflows—such as debugging, environment setup, documentation, and hands-off task execution—demonstrating how AI can streamline real development processes.
### Run the Anthropic Computer Use Demo
-bash
docker run \
  -e ANTHROPIC_API_KEY=$ANROPHIC_API_KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest

After the container starts, open the virtual desktop in your browser:
http://localhost:8080

