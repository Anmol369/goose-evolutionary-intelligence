#!/usr/bin/env python3
"""
Pattern Store
Persistent storage for evolutionary patterns
"""

import json
import os
from pathlib import Path
from typing import Dict, Any


class JSONPatternStore:
    """Simple JSON-based pattern persistence"""
    
    def __init__(self, storage_path: str = None):
        if storage_path is None:
            # Default to ~/.goose_evo/patterns.json
            home_dir = Path.home()
            self.storage_dir = home_dir / '.goose_evo'
            self.storage_path = self.storage_dir / 'patterns.json'
        else:
            self.storage_path = Path(storage_path)
            self.storage_dir = self.storage_path.parent
        
        # Ensure directory exists
        self._ensure_storage_directory()
    
    def _ensure_storage_directory(self):
        """Create storage directory if it doesn't exist"""
        try:
            self.storage_dir.mkdir(parents=True, exist_ok=True)
        except (OSError, PermissionError):
            # Fallback to in-memory storage if filesystem is unwritable
            self.storage_path = None
    
    def save_patterns(self, patterns: Dict[str, Any]) -> bool:
        """Save patterns to persistent storage"""
        if self.storage_path is None:
            return False
        
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(patterns, f, indent=2)
            return True
        except (OSError, PermissionError, json.JSONEncodeError):
            return False
    
    def load_patterns(self) -> Dict[str, Any]:
        """Load patterns from persistent storage"""
        if self.storage_path is None or not self.storage_path.exists():
            return {}
        
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except (OSError, PermissionError, json.JSONDecodeError):
            return {}
    
    def clear_patterns(self) -> bool:
        """Clear all stored patterns"""
        if self.storage_path is None:
            return True
        
        try:
            if self.storage_path.exists():
                self.storage_path.unlink()
            return True
        except (OSError, PermissionError):
            return False