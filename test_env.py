# test_env.py
from dotenv import load_dotenv
import os
import pathlib

env_path = pathlib.Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

print("Key is:", os.getenv("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"))