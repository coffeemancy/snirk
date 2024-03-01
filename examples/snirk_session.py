import asyncio
import sys
from pprint import pprint
from snirk import Snirk
from snirk.api import SnirkError

import examples.snirk_types as st


async def main():
    # discover all SNI devices
    try:
        devices = await Snirk().list_devices()
    except SnirkError as exc:
        print(f"{exc}.\nIs SNI server running?")
        sys.exit(1)

    # handle some requests for each SNI device
    for device in devices:
        async with Snirk.session(uri=device.uri) as snirk:
            print(f"Device URI: {snirk.device.uri}")
            responses = await snirk.multi_read(*st.AlttprAddresses)

        memdata = st.AlttprMemData(responses)
        pprint(memdata)


if __name__ == "__main__":
    asyncio.run(main())
