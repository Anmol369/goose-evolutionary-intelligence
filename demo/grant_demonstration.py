"""
Grant Demonstration Script
Simplified runner for grant committee demonstration
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from goose_evo import run_grant_demonstration

if __name__ == "__main__":
    print("STARTING GRANT COMMITTEE DEMONSTRATION")
    print("=" * 50)
    run_grant_demonstration()

