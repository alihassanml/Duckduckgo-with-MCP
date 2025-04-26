import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq  
from mcp_use import MCPAgent, MCPClient


async def main():
    load_dotenv()
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }
    client = MCPClient.from_dict(config)
    llm = ChatGroq(model="deepseek-r1-distill-llama-70b")  
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    result = await agent.run(
        "Find the best restaurant in San Francisco",
    )
    print(f"\nResult: {result}")

    
if __name__ == "__main__": 
    asyncio.run(main())
