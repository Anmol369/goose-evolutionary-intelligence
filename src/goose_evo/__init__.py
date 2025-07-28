#!/usr/bin/env python3
"""
Goose Evolutionary Intelligence
Seven-Dimensional Self-Improving AI Agent Framework
"""

from .foundation import FoundationIntelligence, RealityConstraint
from .process import ProcessIntelligence
from .evolution import EvolutionIntelligence, EvolutionaryPattern
from .harmony import HarmonyIntelligence
from .pattern_store import JSONPatternStore
from .ecosystem import MinimalViableEcosystem, run_grant_demonstration

__version__ = "0.1.0"
__all__ = [
    "FoundationIntelligence",
    "RealityConstraint", 
    "ProcessIntelligence",
    "EvolutionIntelligence",
    "EvolutionaryPattern",
    "HarmonyIntelligence",
    "JSONPatternStore",
    "MinimalViableEcosystem",
    "run_grant_demonstration"
]