#!/usr/bin/env python3
"""
LinkedIn Auto-Apply Bot
Main entry point for the application
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main_application import LinkedInJobBot

def main():
    """Main entry point"""
    print("🚀 LinkedIn Auto-Apply Bot")
    print("=" * 40)
    
    bot = LinkedInJobBot()
    bot.run()

if __name__ == "__main__":
    main()