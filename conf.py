from documenteer.conf.guide import *

# Fix sphinx-prompt extension name
extensions = [
    ext if ext != "sphinx-prompt" else "sphinx_prompt"
    for ext in extensions
]
