# DuckDuckGo Search with MCP Agent

This project demonstrates how to use **DuckDuckGo MCP Server** with a **LangChain Groq LLM** agent to perform intelligent search tasks via MCP (Micro Component Protocol).

---

## Features
- **MCP Server Integration** (DuckDuckGo search)
- **Groq LLM** (`deepseek-r1-distill-llama-70b`) for reasoning
- **Async Python execution**
- **Simple and modular**

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/alihassanml/Duckduckgo-with-MCP.git
cd Duckduckgo-with-MCP
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```
(Include libraries like `langchain_groq`, `python-dotenv`, etc. in your `requirements.txt`.)

3. **Set up your `.env` file**:

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. **Install the MCP Server**:

```bash
uvx -y duckduckgo-mcp-server
```

*(Make sure `uvx` is installed. If not, install it.)*

---

## Usage

Run the main script:

```bash
python main.py
```

This will:
- Start the MCP client
- Connect to the `duckduckgo-mcp-server`
- Use the Groq LLM to perform a smart search
- Print the result

---

## Example Code

```python
import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq  
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()
    config = {
        "mcpServers": {
            "ddg-search": {
                "command": "uvx",
                "args": ["-y", "duckduckgo-mcp-server"]
            }
        }
    }
    client = MCPClient.from_dict(config)
    llm = ChatGroq(model="deepseek-r1-distill-llama-70b")
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    result = await agent.run("Find the best restaurant in San Francisco")
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Resources
- [DuckDuckGo MCP Server](https://www.npmjs.com/package/duckduckgo-mcp-server)
- [LangChain Groq Documentation](https://python.langchain.com/docs/integrations/llms/groq)
- [Micro Component Protocol (MCP)](https://github.com/openbionics/mcp)

---

## License
This project is licensed under the MIT License.
