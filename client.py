import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\nChoose Tool")
            print("1. Add")
            print("2. Subtract")

            choice = input("Enter choice: ")

            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if choice == "1":
                tool_name = "add"
            elif choice == "2":
                tool_name = "sub"
            else:
                print("Invalid choice")
                return

            result = await session.call_tool(
                tool_name,
                {
                    "a": a,
                    "b": b
                }
            )

            print("\nResult:", result.content[0].text)


asyncio.run(main())