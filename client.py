"""
MCP Client Module
-----------------
This module implements a simple Model Context Protocol (MCP) client.
It uses standard input/output (stdio) transport to spawn an MCP server subprocess,
initializes an MCP session, lists available tools, and executes a tool.
"""

# asyncio: Provides infrastructure for writing single-threaded concurrent code using coroutines,
# multiplexing I/O access over sockets and other resources, and running sub-processes.
import asyncio

# mcp.ClientSession: Manages the lifetime of a client session with the MCP server, including protocol handshake.
# mcp.StdioServerParameters: Configures the execution environment (command, arguments, env vars) for the stdio server.
from mcp import ClientSession, StdioServerParameters
# stdio_client: A context manager that launches the server process and returns the read/write streams.
from mcp.client.stdio import stdio_client


async def main():
    """
    Main asynchronous function that coordinates the MCP client's execution lifecycle.
    
    Tasks performed:
    1. Sets up the server parameters to run 'server.py' using python.
    2. Spawns the server process and obtains standard I/O read/write streams.
    3. Establishes a ClientSession and initializes the protocol handshake with the server.
    4. Retrieves and displays all tools exposed by the MCP server.
    5. Calls the 'add' tool to add two integers and displays the result.
    """
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # Initialize the session and perform handshake with the server
            await session.initialize()

            # Retrieve the list of tools registered on the server
            tools = await session.list_tools()

            print("Available tools:")
            for tool in tools.tools:
                print("-", tool.name)

            # Call the 'add' tool on the server with parameters a=5 and b=7
            result = await session.call_tool(
                "add",
                {
                    "a": 5,
                    "b": 17
                }
            )

            print("Result:", result.content)


# Start the asyncio event loop and run the main routine
asyncio.run(main())