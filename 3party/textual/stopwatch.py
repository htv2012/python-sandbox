#!/usr/bin/env python3
from time import monotonic
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static


class TimeDisplay(Static):
    """A widget to display elapsed time."""
    start_time = reactive(monotonic)
    time = reactive(0.0)

    def on_mount(self):
        """Handle when the widget is added to the app."""
        self.set_interval(1 / 60, self.update_time)

    def update_timej


class StopWatch(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "stopwatch.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(*[StopWatch() for _ in range(4)])

    def action_toggle_dark(self):
        """An action to toggle dark mode."""
        self.dark = not self.dark


def main():
    """Entry"""
    app = StopwatchApp()
    app.run()


if __name__ == "__main__":
    main()
