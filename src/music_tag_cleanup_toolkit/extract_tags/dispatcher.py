from pathlib import Path
from .mp3_metadata_extractor import MP3MetadataExtractor
from .flac_metadata_extractor import FLACMetadataExtractor
from .base_metadata_extractor import AudioMetadataExtractor


def get_extractor_for_file(file_path: Path) -> AudioMetadataExtractor:
    ext = file_path.suffix.lower()
    if ext == ".mp3":
        return MP3MetadataExtractor(file_path)
    elif ext == ".flac":
        return FLACMetadataExtractor(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
