#!/usr/bin/env python3
"""
Foundation Intelligence
Reality Interface & Constraint Recognition
"""

from typing import Dict
from dataclasses import dataclass


@dataclass
class RealityConstraint:
    """Real vs artificial constraint distinction"""
    constraint_type: str
    reality_level: float  # 0.0 = artificial, 1.0 = physics-based
    context: str
    causal_mechanism: str


class FoundationIntelligence:
    """Reality-aligned constraint recognition"""
    
    def __init__(self):
        self.reality_patterns = {}
        self.constraint_history = []
    
    def recognize_constraint(self, user_input: str, context: Dict) -> RealityConstraint:
        """Distinguish real vs artificial limitations"""
        # Enhanced pattern recognition with fuzzy matching
        real_patterns = {
            'memory': {
                'keywords': ['memory', 'ram', 'heap', 'leak', 'allocation', 'garbage'],
                'reality': 0.95, 'mechanism': 'Hardware limitation'
            },
            'latency': {
                'keywords': ['latency', 'speed', 'performance', 'slow', 'timeout', 'response'],
                'reality': 0.9, 'mechanism': 'Network physics'
            },
            'security': {
                'keywords': ['security', 'secure', 'auth', 'authentication', 'login', 'permission', 'access', 'rate limiting', 'throttling'],
                'reality': 0.85, 'mechanism': 'Attack surface reality'
            },
            'cognitive_load': {
                'keywords': ['complex', 'complicated', 'overwhelming', 'many', 'multiple', 'confusing'],
                'reality': 0.9, 'mechanism': 'Human 7±2 limit'
            },
            'scalability': {
                'keywords': ['scale', 'scaling', 'load', 'concurrent', 'distributed', 'microservice'],
                'reality': 0.8, 'mechanism': 'System physics'
            }
        }
        
        input_lower = user_input.lower()
        best_match = None
        highest_score = 0
        
        for pattern_type, pattern_data in real_patterns.items():
            score = sum(1 for keyword in pattern_data['keywords'] if keyword in input_lower)
            if score > highest_score:
                highest_score = score
                best_match = (pattern_type, pattern_data)
        
        if best_match and highest_score > 0:
            pattern_type, pattern_data = best_match
            constraint = RealityConstraint(
                constraint_type=pattern_type,
                reality_level=pattern_data['reality'],
                context=user_input,
                causal_mechanism=pattern_data['mechanism']
            )
            self.constraint_history.append(constraint)
            return constraint
        
        # Default: treat as artificial constraint
        return RealityConstraint(
            constraint_type="artificial",
            reality_level=0.3,
            context=user_input,
            causal_mechanism="Assumed limitation"
        )