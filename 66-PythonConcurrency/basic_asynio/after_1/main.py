from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService

import asyncio

#Before: Each operation blocks the thread completely. If device.connect() takes 2 seconds, the program freezes for 2 seconds.
#After_1: When hitting await, control returns to the event loop. If device.connect() is waiting on network I/O, other tasks could run (though in this example, tasks are still sequential with await in a loop).
#Note: After_1 is async-ready but still sequential because each await waits before moving to the next. True concurrency would use asyncio.gather() or TaskGroup to run multiple operations simultaneously.

async def main() -> None:
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    hue_light_id = await service.register_device(hue_light)
    speaker_id = await service.register_device(speaker)
    toilet_id = await service.register_device(toilet)

    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN),
    ]

    # run the programs
    await service.run_program(wake_up_program)
    await service.run_program(sleep_program)


if __name__ == "__main__":
    asyncio.run(main())