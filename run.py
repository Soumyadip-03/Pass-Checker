#!/usr/bin/env python3
"""
Enhanced Password Strength Checker
Run script for development and production
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """Main entry point"""
    try:
        # Import and run the Reflex app
        from password_strength_checker.password_strength_checker import app
        
        # Check if running in development mode
        if len(sys.argv) > 1 and sys.argv[1] == "--dev":
            print("🚀 Starting Password Strength Checker in development mode...")
            print("📱 Frontend: http://localhost:3000")
            print("🔧 Backend: http://localhost:8000")
            print("💡 Press Ctrl+C to stop")
        
        # Run the app
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you've installed all dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down Password Strength Checker...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()