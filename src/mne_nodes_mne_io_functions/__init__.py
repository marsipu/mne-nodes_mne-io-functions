"""MNE I/O function plugin registration and packaged resources."""

from pathlib import Path

PLUGIN_NAME = "mne-io-functions"
PLUGIN_GITHUB = "https://github.com/marsipu/mne-nodes_mne-io-functions"
CONFIG_PATH = Path(__file__).parent / "mne_io_functions_config.json"
SCRIPT_PATH = Path(__file__).parent / "mne_io_functions.py"
