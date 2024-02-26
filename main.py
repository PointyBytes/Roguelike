#!/usr/bin/env python3
import traceback

import tcod

from game.exceptions import QuitWithoutSaving
import game.input_handlers
import game.setup_game


def save_game(handler: game.input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, game.input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    screen_width = 80
    screen_height = 50

    # The old tileset from the tutorial. Will try out another tileset below.
    # tileset = tcod.tileset.load_tilesheet(
    #    "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    # )
    tileset = tcod.tileset.load_tilesheet(
        "data/TiledFont.png", 32, 10, tcod.tileset.CHARMAP_TCOD
    )

    handler: game.input_handlers.BaseEventHandler = game.setup_game.MainMenu()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, game.input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), game.error
                        )
        except QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
