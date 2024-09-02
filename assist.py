import shelve
import anthropic

from contextlib import contextmanager


@contextmanager
def exercise_tracker():
    db = shelve.open('tracker.db')
    try:
        yield db
    finally:
        db.close()


def tryit():
    client = anthropic.Client()
    stream = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        model="claude-3-opus-20240229",
        stream=True,
    )
    for event in stream:
        print(event.type)
