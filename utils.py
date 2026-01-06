import subprocess

def run_file_command(path):
    try:
        output = subprocess.check_output(
            ["file", path],
            stderr=subprocess.STDOUT
        )
        return output.decode().strip()
    except Exception:
        return "file command not available"