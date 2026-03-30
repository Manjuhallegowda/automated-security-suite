import subprocess
import sys

def run_security_scan():
    """Automates SAST scanning using Bandit."""
    print("--- Starting Security Scan (Bandit) ---")
    result = subprocess.run(["bandit", "-r", "src/"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Security vulnerabilities found!")
        print(result.stdout)
        # Exit with error to fail the CI/CD pipeline if issues exist
        sys.exit(1)
    print("No critical vulnerabilities detected. Scan passed.")

if __name__ == "__main__":
    run_security_scan()