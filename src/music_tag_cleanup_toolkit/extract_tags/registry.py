# registry.py
from models.audio_format import AudioFormat
from extract.mp3_metadata_extractor import MP3MetadataExtractor
from extract.flac_metadata_extractor import FLACMetadataExtractor


def get_extractor_for_format(audio_format: AudioFormat):
    if audio_format == AudioFormat.MP3:
        return MP3MetadataExtractor()
    elif audio_format == AudioFormat.FLAC:
        return FLACMetadataExtractor()
    else:
        raise NotImplementedError(f"No extractor for format: {audio_format}")
