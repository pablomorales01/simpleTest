
def greeting(name: str) -> str:
    name = name.strip() if name else "World"
    return f"Hello, {name}!"
