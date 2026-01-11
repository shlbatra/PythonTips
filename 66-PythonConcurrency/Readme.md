- Python not support parallel computing
Global Interpretor Lock effectivily making Python code single threaded.
Ways around - multiple processes 
Multiple processes doing things at the same time

- Concurrency works well since Python 3.10
Tasks have I/O or networking waits where other tasks can be done.
Still doing one thing where another process runs while a process is waiting for a task to finish
Run CPU bound operations while waiting for IO bound operations
Run multiple AI calls at the same time.

- asyncio package
async - run function concurrently
await - order of execution when concurrent statement is complete ex. wait for databse operation

- Event Loop manages async tasks
Executuon of multiple tasks as part of event loop.

- FastAPI using asyncio

- Thread limitations
Due to GIL, not allow true parallel execution, ayncio - single threaded so less complexity,
Works as Event Loop + Queues

TaskGroup similar to Gather - start various task concurrently. Better work with exceptions or cancelled tasks


