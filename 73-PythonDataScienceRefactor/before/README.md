# Install requirements

```shell
uv sync
```

# Application entry point

```shell
uv run python main.py
```

# Tensorboard

To start Tensorboard:

```shell
uv run tensorboard --logdir runs
```

The output will be something like:

```shell
TensorBoard 2.6.0 at http://localhost:6006/ (Press CTRL+C to quit)
```

Follow the instructions printed to the terminal to view Tensorboard in a browser.
