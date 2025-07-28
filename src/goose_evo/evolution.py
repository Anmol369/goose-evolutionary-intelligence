#!/usr/bin/env python3
"""
Evolution Intelligence
Constraint-to-Capability Transformation
"""

from datetime import datetime
from typing import Dict, Optional
from dataclasses import dataclass
from .foundation import RealityConstraint


@dataclass
class EvolutionaryPattern:
    """Encoded learning from constraint transformation"""

    constraint_signature: str
    transformation_method: str
    success_rate: float
    usage_count: int
    created_at: datetime


class EvolutionIntelligence:
    """Learning system that transforms constraints into capabilities"""

    def __init__(self, pattern_store=None):
        self.dna_patterns: Dict[str, EvolutionaryPattern] = {}
        self.learning_cycles = 0
        self.pattern_store = pattern_store
        self._load_patterns()

    def _load_patterns(self):
        """Load patterns from persistent storage"""
        if self.pattern_store:
            stored_patterns = self.pattern_store.load_patterns()
            for signature, pattern_data in stored_patterns.items():
                self.dna_patterns[signature] = EvolutionaryPattern(
                    constraint_signature=pattern_data["constraint_signature"],
                    transformation_method=pattern_data["transformation_method"],
                    success_rate=pattern_data["success_rate"],
                    usage_count=pattern_data["usage_count"],
                    created_at=datetime.fromisoformat(pattern_data["created_at"]),
                )

    def _save_patterns(self):
        """Save patterns to persistent storage"""
        if self.pattern_store:
            patterns_data = {}
            for signature, pattern in self.dna_patterns.items():
                patterns_data[signature] = {
                    "constraint_signature": pattern.constraint_signature,
                    "transformation_method": pattern.transformation_method,
                    "success_rate": pattern.success_rate,
                    "usage_count": pattern.usage_count,
                    "created_at": pattern.created_at.isoformat(),
                }
            self.pattern_store.save_patterns(patterns_data)

    def encode_constraint_solution(
        self, constraint: RealityConstraint, solution: str, success: bool
    ) -> None:
        """Learn from successful constraint transformations"""
        signature = f"{constraint.constraint_type}_{constraint.reality_level:.1f}"

        if signature in self.dna_patterns:
            # Update existing pattern
            pattern = self.dna_patterns[signature]
            pattern.usage_count += 1
            if success:
                pattern.success_rate = (
                    pattern.success_rate * (pattern.usage_count - 1) + 1.0
                ) / pattern.usage_count
            else:
                pattern.success_rate = (
                    pattern.success_rate * (pattern.usage_count - 1) + 0.0
                ) / pattern.usage_count
        else:
            # Create new evolutionary pattern
            self.dna_patterns[signature] = EvolutionaryPattern(
                constraint_signature=signature,
                transformation_method=solution[:100],  # Store method summary
                success_rate=1.0 if success else 0.0,
                usage_count=1,
                created_at=datetime.now(),
            )

        self.learning_cycles += 1
        self._save_patterns()

    def apply_learned_pattern(self, constraint: RealityConstraint) -> Optional[str]:
        """Apply previously learned constraint transformation"""
        signature = f"{constraint.constraint_type}_{constraint.reality_level:.1f}"

        if signature in self.dna_patterns:
            pattern = self.dna_patterns[signature]
            if pattern.success_rate > 0.7:  # High confidence threshold
                return (
                    f"🧬 LEARNED PATTERN APPLIED (Success Rate: {pattern.success_rate:.1%})\n"
                    + f"Based on {pattern.usage_count} previous transformations:\n\n"
                    + pattern.transformation_method
                )

        return None
