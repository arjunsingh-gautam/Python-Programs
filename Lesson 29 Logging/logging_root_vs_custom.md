# Python Logging: `root` logger vs custom logger

## What `code_4.py` does

`code_4.py` calls:

```python
logging.basicConfig(filename='demo.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

That configures the **root logger** for the entire Python process. Any log message emitted through the root logger, or through any child logger that propagates to root, can be written to `demo.log`.

## What `code_7.py` does

`code_7.py` creates a custom logger:

```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('demo3.log')
logger.addHandler(file_handler)
```

However, it never disables propagation.

By default:

- `logger.propagate == True`
- child logger messages propagate to the ancestor logger chain
- the final ancestor is the root logger

So even though `code_7.py` has its own file handler writing to `demo3.log`, the same messages also travel upward to the root logger.

## Why `code_7.py` logs appear in `code_4.py`'s log file

If both modules run in the same interpreter and the root logger is already configured by `code_4.py`:

1. `code_4.py` configures the root logger with `basicConfig(...)`
2. `code_7.py` creates a module-level logger and adds a handler
3. `code_7.py` logger emits messages
4. messages are written by `code_7.py` handler to `demo3.log`
5. because propagation is still enabled, messages also flow to the root logger
6. root logger writes them to `demo.log`

Therefore, `demo.log` receives `code_7.py` output even though `code_7.py` created its own logger.

## Important logging facts

- `logging.basicConfig()` configures the **root** logger globally.
- Any logger created with `logging.getLogger(name)` is a child of root.
- Child loggers use root handlers unless `propagate` is disabled or they have their own handlers and propagation is controlled.
- A custom logger is not isolated just by calling `getLogger(...)` and adding a handler.

## How to prevent cross-logging

Option 1: disable propagation on the custom logger

```python
logger.propagate = False
```

Option 2: configure logging in one central place only, and do not call `basicConfig()` in imported modules

Option 3: use separate logging configurations for different modules and avoid root logger handlers when you want strict separation.

## Practical fix for `code_7.py`

Add this after adding the file handler:

```python
logger.propagate = False
```

Then `code_7.py` will write only to `demo3.log` and not to the root logger's `demo.log`.

## Summary

- `code_4.py` uses the root logger via `basicConfig`
- `code_7.py` uses a custom logger, but it still propagates to root
- root logger has a handler to `demo.log`
- so `code_7.py` output also ends up in `demo.log`

This is not a bug in `code_7.py` alone; it is the normal behavior of Python logging propagation when the root logger is configured globally.
