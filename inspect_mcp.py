
import inspect
from mcp.server.fastmcp import FastMCP

print("Inspecting FastMCP...")
print(f"FastMCP signature: {inspect.signature(FastMCP.__init__)}")

mcp = FastMCP("test")
print(f"Settings attributes: {dir(mcp.settings)}")

if hasattr(mcp, 'run_streamable_http_async'):
    print(f"run_streamable_http_async signature: {inspect.signature(mcp.run_streamable_http_async)}")

# Check if we can access the underlying app or middleware
print("FastMCP dir:", dir(mcp))
