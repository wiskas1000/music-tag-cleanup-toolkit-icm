from pathlib import Path
from .dispatcher import get_extractor_for_file


def extract_metadata_from_dir(input_dir: str) -> list[dict]:
    results = []
    for file_path in Path(input_dir).rglob("*"):
        if file_path.suffix.lower() not in {".mp3", ".flac"}:
            continue
        try:
            print(file_path)
            # extractor = get_extractor_for_file(file_path)
            # metadata = extractor.extract()
            # results.append(metadata)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    return results
