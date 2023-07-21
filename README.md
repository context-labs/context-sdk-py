<h1><a href="https://usecontext.io" target="_blank">Context</a> Python SDK</h1>

<h4 align="center">⚡ Python SDK for accessing the <a href="https://usecontext.io" target="_blank">Context API</a> ⚡</h4>
<div align="center">
    <a href="https://opensource.org/licenses/MIT">
	  <img alt="Twitter URL" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
	<a href="https://pypi.org/project/context-sdk/">
	  <img alt="pypi Package" src="https://badge.fury.io/py/context-sdk.svg" />
  </a>
  <a href="https://twitter.com/context_labs">
	  <img alt="Twitter URL" src="https://img.shields.io/twitter/url?label=Follow%20%40contextbots&style=social&url=https%3A%2F%2Ftwitter.com%2Fautodoc_"  />
    </a>
</div>

- [How to use it](#how-to-use-it)
  - [Instantiate the SDK](#instantiate-the-sdk)
  - [Search for documents/snippets](#search-for-documentssnippets)

## How to use it

### Instantiate the SDK

```py
from context import ContextSdk, ContextSdkConfig

sdk = ContextSdk(
    ContextSdkConfig(
        api_key="", # your API key
    )
)
```

### Search for documents/snippets

```py
bot_id = "k7rB5_3JT"
query = "How can I get started with Helius?"
top_k = 1
result = self.sdk.search(bot_id, query, top_k)

print(result) # will be a list of snippets
```
