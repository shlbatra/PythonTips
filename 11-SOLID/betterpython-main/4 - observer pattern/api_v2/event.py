# subscribers subscribe to diff event and post event then notify subscribers.

subscribers = dict()  #event: list of subscribers

def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn) #fn append to event type that needs to be notified

def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)


