import sys
sys.path.append('../')

from enkanetwork import EnkaNetworkAPI, Language
import asyncio
import logging
from pprint import pprint

async def main():
    client = EnkaNetworkAPI(lang=Language.JP,debug=True)
    resp = await client.fetch_user_by_uid(854440964)
    pprint({c.name:c.skills for c in resp.characters})
    print("fetch user OK")

asyncio.run(main())