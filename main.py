import typer
import logging

app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def create_html(route_id: int, direction_id: int, time_interval: int):

    print(route_id, direction_id, time_interval)


if __name__ == "__main__":
    # logger
    logging.basicConfig(level=logging.INFO, filename="tmp/speed_visualizer.log", filemode="w",
                        format='(%(levelname)s) %(asctime)s : %(message)s')

    # commands manager
    app()
