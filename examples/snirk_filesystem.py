import asyncio
from pathlib import Path
from snirk import SnirkFilesystem


async def main():
    contents = "Hello, SNI World."
    example_file = "/example/hello.txt"
    example_dir = str(Path(example_file).parent)

    async with SnirkFilesystem.session(kind="fxpakpro") as snirk:
        print(f"* Device URI: {snirk.device.uri}")

        print(f"* Making directory: {example_dir}...")
        await snirk.make_directory(example_dir)

        print(f"* Putting file: {example_file}...")
        await snirk.put_file(contents.encode(), example_file)

        print(f"* Reading directory: {example_dir}...")
        dirs = await snirk.read_directory(example_dir)
        print([en.name for en in dirs.entries if en.name not in [".", ".."]])

        print(f"* Reading file: {example_file}...")
        lines = await snirk.get_file(example_file)
        print(lines)

        print(f"* Removing file: {example_file}...")
        await snirk.remove_file(example_file)

        print(f"* Re-reading directory: {example_dir}...")
        dirs = await snirk.read_directory(example_dir)
        print([en.name for en in dirs.entries if en.name not in [".", ".."]])


if __name__ == "__main__":
    asyncio.run(main())
