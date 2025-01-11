import os
import platform

def shutdown():
    """Shuts down the computer."""
    system_platform = platform.system().lower()
    
    if "windows" in system_platform:
        os.system("shutdown /s /t 0")  # For Windows
    elif "linux" in system_platform or "darwin" in system_platform:
        os.system("shutdown now")  # For Linux and macOS
    else:
        print("Unsupported operating system.")

# Call the function to test (use with caution)
# shutdown()
