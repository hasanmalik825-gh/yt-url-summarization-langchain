from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader

async def get_web_text(url: str):
    loader = UnstructuredURLLoader(
        urls=[url],
        ssl_verify=False,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    )
    docs = loader.load()
    return docs

async def get_youtube_text(url: str):
    loader = YoutubeLoader.from_youtube_url(
        youtube_url=url
        )
    docs = loader.load()
    return docs