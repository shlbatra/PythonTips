# Refactor Steps 1
1. In tracking.py, fix Staging be Enum
2. In tracking.py, Abstract class only have abstract methods -> Prefer Protocol for duct typing and not rquire abstract methods
3. In tracking.py, Add abstract methods that are defined in TensorBoardExperiment - set_stage and flush methods
4. In metrics.py, Convert all types to Float
5. In models.py, Not good idea to keep storing intermediate values in same variable - Sequence of processing - Use Functional Composition (Sequential in Torch)

# Refactor Steps 2
1. In metrics.py, make metrics dataclass -> turn class member variables to instance variables and simplify initialization and remove string representation/reset method
2. Add runner.py - Information Expert principle -> assign responsibility to information expert -> based on structure of data flows. main.py has lot of responsibilities so separate out things, Runner class for each epoch run be it train or test. 
3. main.py -> Simplify based on changes in runner.py

# Refactor Steps 2
1. main.py is still complicated calling lot of things, add to running.py -> call everything to run experiment - run_epoch method 
2. config cleanup (can use Hydra), for hyperparams pass as contants
3. Data Loading clean up -> load_data.py -> add data config to main.py instead - seperate load with validating data. Simplify dataset.py irrespective of train/val

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
