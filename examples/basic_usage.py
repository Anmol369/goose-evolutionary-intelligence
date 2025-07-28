#!/usr/bin/env python3
"""
Basic Usage Examples
Simple examples for community developers
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from goose_evo import MinimalViableEcosystem


def basic_example():
    """Basic usage example"""
    print("<1 Basic Goose Evolutionary Intelligence Example\n")

    # Initialize ecosystem
    ecosystem = MinimalViableEcosystem()

    # Process a simple request
    response = ecosystem.process_request(
        "I need to optimize this database query for better performance"
    )

    print("=� Request: Database query optimization")
    print(f"<� Constraint Type: {response['constraint_analysis']['constraint_type']}")
    print(f"=� Reality Alignment: {response['reality_alignment']:.1%}")
    print(f">� Learning Patterns: {response['ecosystem_status']['learned_patterns']}")
    print(f"� Solution Type: {response['solution_type']}")


def pattern_learning_example():
    """Example showing pattern learning over time"""
    print("\n>� Pattern Learning Example\n")

    ecosystem = MinimalViableEcosystem()

    # First request - learning phase
    print("1� First security request (learning):")
    demo1 = ecosystem.demonstrate_learning(
        "Implement secure user authentication system", feedback=True
    )
    print(demo1[:200] + "...\n")

    # Second similar request - pattern application
    print("2� Similar security request (applying learned pattern):")
    demo2 = ecosystem.demonstrate_learning(
        "Build secure login with session management", feedback=True
    )
    print(demo2[:200] + "...\n")

    print(f"=� Total patterns learned: {len(ecosystem.evolution.dna_patterns)}")
    print(f"�  Total time saved: {ecosystem.verification_time_saved:.0f} seconds")


if __name__ == "__main__":
    basic_example()
    pattern_learning_example()
