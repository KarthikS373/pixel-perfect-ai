import importlib
import os
from pathlib import Path

from typing import Union


def generate_filename(original_filename, *options):
    name, ext = os.path.splitext(original_filename)
    for v in options:
        if v:
            name += "_%s" % v
    name += ext

    return name


def parse_size(size):
    if isinstance(size, int):
        return [size, size]

    if isinstance(size, (tuple, list)):
        if len(size) == 1:
            return size + type(size)(size)
        
        return size

    try:
        thumbnail_size = [int(x) for x in size.lower().split("x", 1)]
    except ValueError:
        raise ValueError(
            "Bad thumbnail size format. Valid format is INTxINT."
        )

    if len(thumbnail_size) == 1:
        thumbnail_size.append(thumbnail_size[0])

    return thumbnail_size


def aspect_to_string(size):
    if isinstance(size, str):
        return size

    return "x".join(map(str, size))


IMG_SUFFIX = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}


def glob_img(p: Union[Path, str], recursive: bool = False):
    p = Path(p)
    if p.is_file() and p.suffix in IMG_SUFFIX:
        yield p
    else:
        if recursive:
            files = Path(p).glob("**/*.*")
        else:
            files = Path(p).glob("*.*")

        for it in files:
            if it.suffix not in IMG_SUFFIX:
                continue
            yield it
