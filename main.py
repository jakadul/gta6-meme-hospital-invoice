"""Entrypoint for the make.fun gta6-meme-x-01 entry.

Runs the renderer and writes meme.png next to this file. The grader executes
this file; the post itself is the entry, this repo is its source.

    python3 main.py
"""
import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    os.chdir(HERE)
    runpy.run_path(os.path.join(HERE, "make_meme.py"), run_name="__main__")


if __name__ == "__main__":
    main()