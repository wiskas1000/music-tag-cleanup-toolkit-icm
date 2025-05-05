# src/music_tag_cleanup_toolkit/cli.py
import typer
import os
from dotenv import load_dotenv
from music_tag_cleanup_toolkit.extract_tags.runner import extract_metadata_from_dir


app = typer.Typer(
    help="Music Tag Cleanup Toolkit for Indian Classical Music", no_args_is_help=True
)


def get_env(var_name: str, default: str) -> str:
    """Load environment variable with fallback."""
    load_dotenv()
    return os.getenv(var_name, default)


@app.command()
def extract(
    music_base_dir: str = typer.Option(
        get_env("MUSIC_BASE_DIR", "./data/music"),
        help="Directory containing the music files",
    ),
    metadata_base_dir: str = typer.Option(
        get_env("METADATA_BASE_DIR", "./data/metadata.json"),
        help="Output JSON file to store metadata",
    ),
):
    """Extract metadata from music files and save to JSON."""
    typer.echo(f"Extracting from: {music_base_dir}")
    typer.echo(f"Saving to: {metadata_base_dir}")
    # TODO: implement extract logic
    print(f"extract")
    metadata = extract_metadata_from_dir(music_base_dir)


@app.command()
def write(
    input_json: str = typer.Option(..., help="Input JSON with metadata"),
    target_dir: str = typer.Option(..., help="Target directory to write tags to"),
):
    """Write metadata back to music files."""
    typer.echo(f"Loading metadata from: {input_json}")
    typer.echo(f"Applying to: {target_dir}")
    # TODO: implement write logic


def main():
    app()


if __name__ == "__main__":
    main()
