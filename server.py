"""
MCP Server Module
-----------------
This module implements a Model Context Protocol (MCP) server using the FastMCP framework.
It exposes tools for arithmetic operations (addition and subtraction) that can be queried
and called by MCP clients.
"""

# mcp.server.fastmcp.FastMCP: A high-level framework class for building MCP servers easily,
# providing decorator-based tools/resources registration and automated command-line running.
from mcp.server.fastmcp import FastMCP

# Create a FastMCP server instance named "MCP-Server"
mcp = FastMCP("MCP-Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of a and b.
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract the second number from the first number.
    
    Parameters:
    a (int): The first integer (minuend).
    b (int): The second integer (subtrahend).
    
    Returns:
    int: The difference of a and b (a - b).
    """
    return a - b

if __name__ == "__main__":
    # Start and run the FastMCP server, exposing the registered tools (add, subtract)
    mcp.run()

