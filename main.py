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

        self.show_question("first")

    def show_question(self, tag="first"):
        match tag:
            case "first":
                self.current_id = 0
            case "last":
                self.current_id = n_questions - 1
            case "previous":
                self.current_id = (self.current_id - 1) % n_questions
            case "next":
                self.current_id = (self.current_id + 1) % n_questions
            case "random":
                self.current_id = randrange(0, len(questions))

        self.update(Markdown(
            f"> *{questions[self.current_id]}*"
            "\n\n"
            f"{self.current_id:0>3} {"[random]" if tag == "random" else ""}"
        ))


class Chai(App):
    def compose(self) -> None:
        self.question = Question()
        yield self.question

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"

    def on_key(self, event) -> None:
        match event.key:
            case 'n' | 'k':
                self.question.show_question("next")
            case 'p' | 'j':
                self.question.show_question("previous")
            case 'h' | 'f':
                self.question.show_question("first")
            case 'l':
                self.question.show_question("last")
            case "r":
                self.question.show_question("random")
            case 'q':
                sys.exit(0)
            case _:
                return


if __name__ == "__main__":
    app = Chai()
    app.run()
