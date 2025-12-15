## Create a basic Crawl4AI MCP server with FastMCP
## See https://github.com/jlowin/fastmcp
##  and https://github.com/unclecode/crawl4ai

from fastmcp import FastMCP
from crawl4ai_src.crawl4ai_utils import AdaptiveCrawl

## Instantiate the server
mcp = FastMCP("crawl")

## Create tools
@mcp.tool()
async def crawl(seed_urls: list[str], query: str, top_k: int = 10) -> str:
    """Crawl one or more seed URLs for content relevant to a query.

    Parameters
    ----------
    seed_urls : List[str]
        List of starting URLs.
    query : str
        Search query to filter the crawled content.
    top_k : int, optional
        Number of top results to return (default 10).
    """
    crawler = AdaptiveCrawl(top_k=top_k)
    return await crawler.run(seed_urls, query)

## Run the server in stdio mode
if __name__ == "__main__":
    mcp.run(transport="stdio")
