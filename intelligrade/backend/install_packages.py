# Install required packages for DOCX support
import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

if __name__ == "__main__":
    packages = ["python-docx", "PyPDF2"]
    
    print("🔧 Installing required packages for file processing...")
    
    for package in packages:
        install_package(package)
    
    print("\n🎉 Package installation complete!")
    print("Now restart the backend server to use the new packages.")