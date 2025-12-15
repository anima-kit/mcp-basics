# MCP Basics

This repo is dedicated to learning how
 to create MCPs and use them with local solutions.

📚 Each MCP created has a dedicated tutorial: check them out [here][ak-mcps].

The first iteration of this project is to create
 an in-depth guide into what MCP is and how to use it.
  We'll go through an example of using the LangChain's
   docs MCP server in LM Studio.

The next iteration is to create a step-by-step guide
 into how to create our own MCP servers. We'll see how
  to create some simple web crawling servers using
   Crawl4AI, then test them out in LM Studio.

After that, I plan to create a step-by-step guide
 demonstrating how to use both Crawl4AI and Milvus
  MCP servers to gather, store, and query research
   from the web with the agentic platform OpenCode.

Finally, additional modular features that enhance
 deep research can be added to the OpenCode setup.

## Getting started

1. To get started with the repo, clone it, create a virtual environment, and install all the necessary packages

```
git clone https://github.com/anima-kit/mcp-basics.git
uv venv venv
venv/Scripts/activate
uv pip install -r requirements.txt
```

For the [Crawl4AI][crawl4ai] MCP, you'll also need to run:

```
playwright install
```

2. To run any of the MCP servers:

```
fastmcp dev mcp-server.py
```

## Examples

- Calculator (`mcp-calculator.py`): A very simple calculator MCP that outlines how to use various aspects of the [FastMCP][fastmcp] library
- Adaptive web crawler (`mcp-crawl4ai.py`): A minimum web crawler MCP using the adaptive method from the [Crawl4AI][crawl4ai] library.

## Tech

<!-- Disco Theme (Animated) -->
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-disco.svg" alt="Powered by Crawl4AI" width="200"/>
</a> To create web crawling tools

- [FastMCP][fastmcp]: To create MCP servers

## Contributing

See the [contributing guide][CONTRIBUTING]

## License

MIT: See the [license][LICENSE]

<!-- LINKS -->
[ak-mcps]: https://anima-kit.github.io/tutorials/applications/mcp/
[CONTRIBUTING]: CONTRIBUTING.md
[crawl4ai]: https://docs.crawl4ai.com/
[fastmcp]: https://gofastmcp.com/getting-started/welcome
[LICENSE]: LICENSE.md