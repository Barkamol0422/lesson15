import os

def shutdown():
    """Shuts down the computer."""
    os.system("shutdown /s /t 0" if os.name == "nt" else "sudo shutdown now")

# Uncomment the line below to run the shutdown function
# shutdown()
