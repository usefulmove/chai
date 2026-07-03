from questions import questions, n_questions
from random import randrange
from rich.markdown import Markdown
import sys
from textual.app import App
from textual.widgets import Static


class Question(Static):
    def __init__(self):
        super().__init__()
        n_questions = len(questions)

    def on_mount(self) -> None:
        # set styling
        self.styles.text_align = "left"
        self.styles.margin = 0, 0
        self.styles.padding = 2, 4
        # select display question
        self.show_first()

    def show_first(self) -> None:
        self.idx = 0
        self.update(Markdown(f"> *{questions[self.idx]}*\n\n{self.idx:0>3}"))

    def show_last(self) -> None:
        self.idx = n_questions - 1
        self.update(Markdown(f"> *{questions[self.idx]}*\n\n{self.idx:0>3}"))

    def show_previous(self) -> None:
        self.idx = (self.idx - 1) % n_questions
        self.update(Markdown(f"> *{questions[self.idx]}*\n\n{self.idx:0>3}"))

    def show_next(self) -> None:
        self.idx = (self.idx + 1) % n_questions
        self.update(Markdown(f"> *{questions[self.idx]}*\n\n{self.idx:0>3}"))

    def show_random(self) -> None:
        self.idx = randrange(0, len(questions))
        self.update(Markdown(f"> *{questions[self.idx]}*\n\n{self.idx:0>3} [random]"))


class Chai(App):
    def compose(self) -> None:
        self.question = Question()
        yield self.question

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"

    def on_key(self, event) -> None:
        match event.key:
            case 'n' | 'j':
                self.question.show_next()
            case 'p' | 'k':
                self.question.show_previous()
            case 'h' | 'f':
                self.question.show_first()
            case 'l':
                self.question.show_last()
            case "r":
                self.question.show_random()
            case 'q':
                sys.exit(0)
            case _:
                return


if __name__ == "__main__":
    app = Chai()
    app.run()
