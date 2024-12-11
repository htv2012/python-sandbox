#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


theme_toggle = {
    "textual-dark": "textual-light",
    "textual-light": "textual-dark",
}

class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("t", "toggle_dark", "Toggle theme"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = theme_toggle[self.theme]
#        self.theme = (
#            "textual-dark" if self.theme == "textual-light" else "textual-light"
#        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
