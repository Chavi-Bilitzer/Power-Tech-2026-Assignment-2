"""Power Tech 2026 - Assignment 2. Starter file. Do not rename this file and do not change its structure unless the assignment sheet tells you to. """

<<<<<<< HEAD
GREETING = "Hi"
=======
GREETING = "Shalom"
>>>>>>> feature/greeting
VERSION = "1.0"

def greet(name):
    """Return a greeting for the given name."""
    return f"{GREETING}, {name}!"

def farewell(name):
    """Return a farewell message for the given name."""
    return f"Goodbye, {name}!"

def app_info():
    """Return basic information about the app."""
    return {"app": "power-tech", "version": VERSION}

if __name__ == "__main__":
    print(greet("Power Tech"))
    print(app_info())
