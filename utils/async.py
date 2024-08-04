import asyncio


async def fetch_data(url):
    print(f"Fetching data from {url}...")
    await asyncio.sleep(2)  # Simulate network delay
    print(f"Data fetched from {url}")
    return f"Data from {url}"


async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    tasks = [fetch_data(url) for url in urls]

    # Run tasks concurrently
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


asyncio.run(main())
