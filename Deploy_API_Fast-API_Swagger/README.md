## Setup Project

1. `pip install poetry` (or safer, follow the instructions: https://python-poetry.org/docs/#installation)
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`. NOTE: if having troubles (recent versions like python 3.12 may show errors), you can switch to a different python version by `poetry env use <PYTHON_BINARY>`, for example `poetry env use $(which python3)`. If you are having trouble with this, ensure you are using a 3.8.x Python version (`python --version`).
3. `[UNIX]`: Run the FastAPI server via poetry with the bash script: first make the run file executable with `chmod +x run.sh` and then `poetry run ./run.sh`
   
   `[WINDOWS]`: Run the FastAPI server via poetry with the Python command: `poetry run python main.py`
4. Open http://localhost:8001/

To stop the server, press CTRL+C

If you get stuck, checkout the [troubleshooting readme](../troubleshooting/README.md)
