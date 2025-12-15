## Create a simple calculator MCP server with FastMCP
## See https://github.com/jlowin/fastmcp

from fastmcp import FastMCP
from fastmcp.server.middleware.tool_injection import PromptToolMiddleware

## Instantiate the server
server = FastMCP(
    name="calculator",
    ## TODO: Instructions not working with LM Studio - need to put in instructions explicitly through LM Studio interface
    #instructions="""
    #You are a friendly assistant connected to a calculator MCP. 
    #You have access to the tools `add()` and `multiply()`. 
    #You also have access to the prompt `medieval_wizard()`. 
    #When you get a result from the `add()` tool, run the `medieval_wizard()` prompt with the result to get your final response. 
    #When you get any other query or utilize any other tool, speak in a typical, friendly style. 
    #"""
)
## Expose prompts to LLMs
server.add_middleware(PromptToolMiddleware())

## Create tools
@server.tool()
def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    Args
    -------
    a: float
        The first number.
    b: float
        The second number.

    Returns
    -------
    float:
        The sum of the two numbers.    
    """
    return float(a + b)

@server.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.

    Args
    -------
    a: float
        The first number.
    b: float
        The second number.

    Returns
    -------
    float:
        The two numbers multiplied together.    
    """
    return float(a * b)

## Create prompts
@server.prompt()
def medieval_wizard(result: float) -> str:
    """Generates a user message to give the result in the style of a medieval wizard."""
    return f"Roleplay as a wizard in medieval times to give the following result: {result}."

## Run the server in stdio mode
if __name__ == "__main__":
    server.run(transport="stdio")