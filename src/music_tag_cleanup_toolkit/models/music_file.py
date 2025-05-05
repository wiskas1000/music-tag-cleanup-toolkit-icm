from dataclasses import dataclass
from .audio_format import AudioFormat


@dataclass
class MusicFile:
    path: str
    format: AudioFormat

    @property
    def filename(self) -> str:
        return os.path.basename(self.path)
