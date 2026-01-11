from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService
from typing import Awaitable, Any

import asyncio

# Specific to processing all messageas in a program
#   │ Pattern   │ for loop with await     │ asyncio.gather()         │
#   ├───────────┼─────────────────────────┼──────────────────────────┤
#   │ Execution │ Sequential (one-by-one) │ Concurrent (all at once) │
#   ├───────────┼─────────────────────────┼──────────────────────────┤
#   │ I/O waits │ Each waits for previous │ All wait simultaneously  │
#   ├───────────┼─────────────────────────┼──────────────────────────┤
#   │ Speed     │ Sum of all durations    │ Duration of slowest task │


async def run_sequence(*funcs: Awaitable) -> None:
    for func in funcs:
        await func

async def run_concurrent(*funcs: Awaitable) -> None:
    await asyncio.gather(*funcs)


async def main() -> None:
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    hue_light_id, speaker_id, toilet_id = await asyncio.gather(
        service.register_device(hue_light),
        service.register_device(speaker),
        service.register_device(toilet),
    )
    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
    ]
    await service.run_program(wake_up_program)

    # sleep_program = [
    #     Message(hue_light_id, MessageType.SWITCH_OFF),
    #     Message(speaker_id, MessageType.SWITCH_OFF),
    #     Message(toilet_id, MessageType.FLUSH),
    #     Message(toilet_id, MessageType.CLEAN),
    # ]
    await run_concurrent(
        service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
        service.send_msg(Message(speaker_id, MessageType.SWITCH_OFF)),
        run_sequence(
            service.send_msg(Message(toilet_id, MessageType.FLUSH)),
            service.send_msg(Message(toilet_id, MessageType.CLEAN)),
        )
    )


if __name__ == "__main__":
    asyncio.run(main())