import asyncio

import typer

from src.infrastructure.db.seed import seed_initial_data

app = typer.Typer(help="Aiti Guru CLI")


@app.command()
def seed():
    typer.echo("Seeding database...")
    asyncio.run(seed_initial_data())
    typer.echo("Done")

