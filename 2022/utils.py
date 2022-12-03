from pathlib import Path


def read_file(filename):
    p = Path(__file__).parent / f"inputs/{filename}"

    for row in p.open("r"):
        yield row
