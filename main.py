from questions import QUESTIONS
from random import randrange
from rich.markdown import Markdown
import sys
from textual.app import App
from textual.widgets import Static

class Question(Static):
    def on_mount(self) -> None:
        self.styles.text_align = "left"
        self.styles.margin = 0, 0
        self.styles.padding = 2, 4
        self.next_question()

    def next_question(self) -> None:
        idx = randrange(0, len(QUESTIONS))
        self.update(Markdown(f"> *{QUESTIONS[idx]}*\n\n{idx:0>3}"))

class Chai(App):
    def compose(self) -> None:
        self.question = Question()
        yield self.question

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"

    def on_key(self, event) -> None:
        match event.key:
            case key if key in "nphjkl":
                self.question.next_question()
            case 'q':
                sys.exit(0)

if __name__ == "__main__":
    app = Chai()
    app.run()
