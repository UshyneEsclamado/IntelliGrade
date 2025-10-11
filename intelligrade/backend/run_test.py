import subprocess
import sys

def run_test():
    # Run the test
    try:
        result = subprocess.run([sys.executable, "test_user_format.py"], 
                              capture_output=True, text=True, cwd="c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend")
        print("STDOUT:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
    except Exception as e:
        print(f"Error running test: {e}")

if __name__ == "__main__":
    print("🚀 Running user format test...")
    run_test()