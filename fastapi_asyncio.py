import asyncio
from datetime import datetime

import httpx



async def fetch_url(url: str) ->tuple[int, str]:
    client = httpx.AsyncClient()
    response = await client.get(url)
    return response.status_code, response.text[:50]



async def main():
    urls = [
        "https://postman-echo.com/delay/1",
        "https://postman-echo.com/delay/2",
        "https://postman-echo.com/delay/3",
    ]

    results = await asyncio.gather(*map(fetch_url, urls))

    for status_code, text in results:
        print(status_code, text)


if __name__ == "__main__":
    start_time = datetime.now()
    asyncio.run(main())
    print(datetime.now() - start_time)