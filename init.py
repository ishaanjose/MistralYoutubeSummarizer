import click
from modules.summarize_video import summarize_video
@click.group()
def cli():
    pass

@cli.command()
@click.argument('yt_url', type=str)
def summarize(yt_url):
    """Summarizes a YouTube video. Format summarize <youtube_url>"""
    click.echo(f'Summary: {summarize_video(yt_url)}')

if __name__ == '__main__':
    cli()
