# src/music_tag_cleanup_toolkit/cli.py
# import mutagen
#
#
# def main():
#     print("Hello from music-tag-cleanup-toolkit-icm!")
#
#
# if __name__ == "__main__":
#     main()

import typer

app = typer.Typer(help="Music Tag Cleanup Toolkit for Indian Classical Music")


@app.command()
def extract(
    input_dir: str = typer.Option(..., help="Directory containing the music files"),
    output_file: str = typer.Option(..., help="Output JSON file to store metadata"),
):
    """Extract metadata from music files and save to JSON."""
    typer.echo(f"Extracting from: {input_dir}")
    typer.echo(f"Saving to: {output_file}")
    # TODO: implement extract logic


@app.command()
def write(
    input_json: str = typer.Option(..., help="Input JSON with metadata"),
    target_dir: str = typer.Option(
        ..., help="Directory containing music files to write to"
    ),
):
    """Write metadata back to music files."""
    typer.echo(f"Loading metadata from: {input_json}")
    typer.echo(f"Applying to files in: {target_dir}")
    # TODO: implement write logic


# You can add more commands: clean, load, etc.
