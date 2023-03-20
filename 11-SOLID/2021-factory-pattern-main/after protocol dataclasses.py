"""
Basic video exporting example
"""

import pathlib
from dataclasses import dataclass
from typing import Protocol, Type


class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""

    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter:
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec."""

    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter:
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter
    
@dataclass 
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]
    #here control over parameters provide
    def __call__(self) -> MediaExporter:
        return MediaExporter(self.video_class(), self.audio_class()) #pass optional parameters here - more control
    
    

# reading export here
def read_factory() -> MediaExporterFactory:
    """Constructs an exporter factory based on the user's preference."""
    #factory here tuple of classes
    factories = {
        "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
        "high": MediaExporterFactory(H264Hi422PVideoExporter, AACAudioExporter),
        "master": MediaExporterFactory(LosslessVideoExporter, WAVAudioExporter),
    }
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        try:
            return factories[export_quality]
        except KeyError:
            print(f"Unknown output quality option: {export_quality}.")

# now main doing export only - split responsibility
#less coupling -> dont need to know exporter code 
def main(exporter: MediaExporter) -> None:
    """Main function."""
    # fac = read_exporter() # define fn here directly

    # prepare the export
    exporter.video.prepare_export("placeholder_for_video_data")
    exporter.audio.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    exporter.video.do_export(folder)
    exporter.audio.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_factory() #depedency inversion using abstract class
    #use the factory to create media exporter
    media_exporter = factory()
    # perform the exporting job
    main(media_exporter)  #depedency injection
