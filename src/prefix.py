from pathlib import Path, PurePath
from src.utils.paths import get_path
from src.utils.files import skip_byte_order_mark
from src.utils.algo import map_if
from tqdm import tqdm


def change_prefix(
    input_dir: Path, output_dir: Path, input_root: PurePath, output_root: PurePath
) -> None:
    for p in tqdm(input_dir.iterdir()):
        with p.open() as f:
            skip_byte_order_mark(f)
            res = map_if(
                f,
                lambda x: not x.startswith("#"),
                lambda x: str(output_root / get_path(x).relative_to(input_root)),
            )
            with (output_dir / p.name).open("w") as f2:
                f2.writelines(res)
