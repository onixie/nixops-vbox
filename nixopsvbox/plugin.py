import os.path
import nixops.plugins

@nixops.plugins.hookimpl
def nixexprs():
    expr_path = os.path.realpath(os.path.dirname(__file__) + "/../../../../share/nix/nixops-vbox")
    if not os.path.exists(expr_path):
        expr_path = os.path.realpath(os.path.dirname(__file__) + "/../../../../../share/nix/nixops-vbox")
    if not os.path.exists(expr_path):
        expr_path = os.path.dirname(__file__) + "/../nix"

    return [
        expr_path
    ]

@nixops.plugins.hookimpl
def load():
    return [
        "nixopsvbox.resources",
        "nixopsvbox.backends.virtualbox",
    ]
