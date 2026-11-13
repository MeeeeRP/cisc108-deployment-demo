from drafter import *
from dataclasses import dataclass

set_website_title("Corgi Count")
set_site_information(author="Maya Perry",
                     description="Increment the number of corgi puppies you have.",
                     sources="",
                     planning="planning.pdf",
                     links=["https://github.com/MeeeeeRP/cisc108-deployment-demo"]
                     )

hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    return Page(state, [
        "Current # of puppies: " + str(state.count) + "\n",
        Button("+1", "increment"),
        Button("+5", "increment_5"),
        Button("-1", "decrement"),
        Button("Reset", "reset_count")
    ])


@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)


@route
def decrement(state: State) -> Page:
    if state.count>0:
        state.count = state.count - 1
    return index(state)


@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)

@route
def increment_5(state:State) ->Page:
    state.count+=5
    return index(state)

assert_state(increment(State(0)), State(1))
assert_state(reset_count(State(7)), State(0))
assert_has(index(State(3)), "Current # of puppies: 3")

start_server(State(5))
