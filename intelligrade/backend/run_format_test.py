import subprocess
import sys

def run_format_test():
    try:
        result = subprocess.run([sys.executable, "test_all_formats.py"], 
                              capture_output=True, text=True, 
                              cwd="c:\\Users\\Administrator\\Desktop\\INTELLIGRADE\\intelligrade\\backend")
        print("🔍 FORMAT TEST RESULTS:")
        print("=" * 60)
        print(result.stdout)
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
        print("=" * 60)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing all answer key formats...")
    success = run_format_test()
    if success:
        print("✅ All format tests passed!")
    else:
        print("❌ Some tests failed!")