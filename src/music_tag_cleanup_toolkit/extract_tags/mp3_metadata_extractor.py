from mutagen.mp3 import MP3
from .base_metadata_extractor import AudioMetadataExtractor


class MP3MetadataExtractor(AudioMetadataExtractor):
    def extract(self):
        audio = MP3(self.file_path)
        tags = dict(audio.tags or {})
        return {
            "path": str(self.file_path),
            "tags": tags,
            "format": "mp3",
        }
