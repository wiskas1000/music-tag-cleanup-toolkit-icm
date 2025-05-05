from mutagen.flac import FLAC
from .base_metadata_extractor import AudioMetadataExtractor


class FLACMetadataExtractor(AudioMetadataExtractor):
    def extract(self):
        audio = FLAC(self.file_path)
        tags = dict(audio.tags or {})
        return {
            "path": str(self.file_path),
            "tags": tags,
            "format": "flac",
        }
