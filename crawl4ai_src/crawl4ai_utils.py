### A simple adaptive web crawler using Crawl4AI to be setup as an MCP.
### See adaptive web crawling here: https://docs.crawl4ai.com/core/adaptive-crawling/

import json
import asyncio
import logging
from typing import List, Dict, Any
from crawl4ai import AsyncWebCrawler, AdaptiveCrawler, AdaptiveConfig, BrowserConfig, LLMConfig

from crawl4ai_src.logger import redirect_stdout_to_logger

## Create a basic adaptive crawler with Crawl4AI
class AdaptiveCrawl:
    """
    A minimal Crawl4AI adaptive crawler that:

    1. Accepts a list of seed URLs and a query string.
    2. Runs an adaptive crawl using the statistical method.
    3. Returns a single markdown string containing URL + content
       for the most relevant pages.
    """

    def __init__(self, top_k: int = 10) -> None:
        """
        Args
        -------
        top_k : int
            Number of pages to include in the markdown.
        """
        self.top_k = top_k

    async def _crawl_single(self, seed_url: str, query: str) -> List[Dict[str, Any]]:
        """
        Runs AdaptiveCrawler.digest for one seed URL.

        Args
        -------
        seed_url: str
            The URL from which to start crawling.
        query: str
            The query against which to search.

        Returns
        -------
        dict:
            A dictionary of the top-scoring pages with keys:
                - url
                - content
                - score
        """

        ## Settings
        browser_config = BrowserConfig(
            verbose=False,
        )
        
        ##################################
        ##### Statistical method #########
        ##################################
        config = AdaptiveConfig(
            # stop crawling at this confidence level
            confidence_threshold=0.7,   
            # or stop when 20 total pages crawled
            max_pages=20,
            # only take top 3 relevant links for each page
            top_k_links=3,
            # if info gain for a page is less than this, 
            # skip page and move to next
            min_gain_threshold=0.05,
        )


        ##################################
        ##### Embedding method ###########
        ##################################
        #config = AdaptiveConfig(
        #    # use embedding model instead of statisical method
        #    strategy="embedding",
        #    max_pages=15,
        #    top_k_links=5,
        #    min_gain_threshold=0.05,
        #    # number of different queries based on original
        #    n_query_variations=10,
        #    # below this, content deemed irrelevant
        #    embedding_min_confidence_threshold=0.1
        #)

        ## Model to use for embeddings
        #config.embedding_llm_config = {
        #    'provider': 'ollama/nomic-embed-text',
        #    'api_token': 'no-token-needed'
        #}


        ## Run the adaptive crawler
        async with AsyncWebCrawler(
            config=browser_config
        ) as crawler:
            adaptive = AdaptiveCrawler(crawler, config)

            with redirect_stdout_to_logger(logging.INFO):
                await adaptive.digest(start_url=seed_url, query=query)

            pages = adaptive.get_relevant_content(top_k=self.top_k)
            return pages


    ## Function to use for MCP tool
    async def run(self, seed_urls: List[str], query: str) -> str:
        """
        Run the adaptive crawler for a list of seed URLs.

        Args
        -------
        seed_urls : List[str]
            A list of URLs from which to start crawling.
        query : str
            The query guiding the crawl.

        Returns
        -------
        str:
            Content of top-scoring pages in Markdown format.
        """
        all_pages: List[Dict[str, Any]] = []

        ## Adaptive crawl each URL
        for url in seed_urls:
            pages = await self._crawl_single(url, query)
            all_pages.extend(pages)

        # Build Markdown
        md_parts: List[str] = []
        for i, page in enumerate(all_pages):
            header = f"# Source {i}"
            link = f"URL: {page['url']}\n"
            content = page.get("content", "").strip()

            if not content:
                continue
            md_parts.append(header + "\n " + link + "\n --- \n" + content + "\n")

        return "\n".join(md_parts) or "No relevant content found for the query."