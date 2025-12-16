"""Configuration module for setting up Hugging Face cache directories."""
import os
from pathlib import Path

def setup_hf_cache():
    """Set up Hugging Face cache directories in the user's home directory."""
    default_cache = Path.home() / "..cache" / "huggingface"

    os.environ.setdefault("HF_HOME", str(default_cache))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(default_cache / "transformers"))
    os.environ.setdefault("HF_DATASETS_CACHE", str(default_cache / "datasets"))

    return default_cache