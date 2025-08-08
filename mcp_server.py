from mcp.server.fastmcp import FastMCP
import httpx

# Config
API_BASE_URL = "http://localhost:8000"  # your FastAPI server
OAUTH_TOKEN = None  # Will store after login

# Create MCP app
app = FastMCP("PathFactory MCP Server")

# Function to login and get OAuth token
async def get_oauth_token(username="agent", password="agent123"):
    global OAUTH_TOKEN
    if OAUTH_TOKEN:
        return OAUTH_TOKEN
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{API_BASE_URL}/token",
            data={
                "grant_type": "password",
                "username": username,
                "password": password
            }
        )
        resp.raise_for_status()
        OAUTH_TOKEN = resp.json()["access_token"]
        return OAUTH_TOKEN

# Helper to call API with token
async def call_api(endpoint: str):
    token = await get_oauth_token()
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{API_BASE_URL}{endpoint}",
            headers={"Authorization": f"Bearer {token}"}
        )
        resp.raise_for_status()
        return resp.json()

# Register MCP tools
@app.tool()
async def content_library() -> dict:
    """Fetch content library items"""
    return await call_api("/content_library/")

@app.tool()
async def recommendations() -> dict:
    """Fetch recommendations"""
    return await call_api("/recommendations/")

@app.tool()
async def conversations() -> dict:
    """Fetch conversations"""
    return await call_api("/conversations/")

@app.tool()
async def topics() -> dict:
    """Fetch topics"""
    return await call_api("/topics/")

@app.tool()
async def engagement() -> dict:
    """Fetch engagement data"""
    return await call_api("/engagement/")

@app.tool()
async def collection() -> dict:
    """Fetch collection data"""
    return await call_api("/collection/")

# Start MCP server
if __name__ == "__main__":
    app.run()
