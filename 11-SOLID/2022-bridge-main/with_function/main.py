import logging

from stream.dslr_camera import dslr_camera
from stream.twitch_stream import TwitchStreamingService
from stream.webcam import webcam
from stream.youtube_stream import YouTubeStreamingService


def main() -> None:
    # setup logging
    logging.basicConfig(level=logging.INFO)

    # create a device and a streaming service
    #pass method here instead of instance of class
    service = YouTubeStreamingService(webcam)

    # start streaming
    reference = service.start_stream()
    service.fill_buffer(reference)
    service.stop_stream(reference)

    # create another device and streaming service
    service2 = TwitchStreamingService(dslr_camera)

    # start streaming there as well
    reference2 = service2.start_stream()
    service2.fill_buffer(reference2)
    service2.stop_stream(reference2)


if __name__ == "__main__":
    main()
