import os
import warnings

from src.parse_args import parse_args
from src.server import main

def set_mps_fallback():
    """
    Set an environment variable to enable MPS fallback for PyTorch.
    """
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

def ignore_user_warnings():
    """
    Ignore UserWarning warnings.
    """
    warnings.simplefilter("ignore", UserWarning)

def entry_point():
    """
    Entry point for the application.
    """
    set_mps_fallback()
    ignore_user_warnings()
    args = parse_args()
    main(args)
