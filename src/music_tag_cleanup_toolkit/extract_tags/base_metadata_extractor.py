# base_extractor.py
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any
from ..models.music_file import MusicFile


class BaseMetadataExtractor(ABC):
    @abstractmethod
    def extract(self, music_file: MusicFile) -> dict:
        pass


class AudioMetadataExtractor(ABC):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    @abstractmethod
    def extract(self) -> Dict[str, Any]:
        pass
