from pathlib import Path, PurePath, PureWindowsPath


def get_path(x: str) -> PurePath:
    if "\\" in x:
        return PureWindowsPath(x)
    else:
        return Path(x)
