#!/usr/bin/env python3
"""
Process Intelligence
Cognitive Optimization (7±2 principle)
"""

from typing import List
from .foundation import RealityConstraint


class ProcessIntelligence:
    """Human cognitive architecture optimization"""

    def __init__(self):
        self.cognitive_patterns = {}
        self.miller_rule_violations = 0

    def optimize_cognitive_load(
        self, solution: str, constraint: RealityConstraint
    ) -> str:
        """Structure solution for optimal human cognitive processing"""
        # Check for cognitive overload indicators
        complexity_indicators = [
            "microservice",
            "architecture",
            "complex",
            "multiple",
            "many",
        ]
        is_complex = any(
            indicator in constraint.context.lower()
            for indicator in complexity_indicators
        )

        # Miller's Rule: 7±2 items max
        lines = solution.split("\n")
        words = constraint.context.split()

        if len(words) > 15 or is_complex or len(lines) > 7:
            # Apply cognitive chunking
            chunked = self._chunk_complex_solution(constraint.context, solution)
            self.cognitive_patterns["chunking_applied"] = True
            return chunked

        # Add cognitive markers for high reality constraints
        if constraint.reality_level > 0.8:
            return f"🔥 REALITY CONSTRAINT: {constraint.causal_mechanism}\n\n{solution}"

        return solution

    def _chunk_complex_solution(self, request: str, solution: str) -> str:
        """Break complex requests into cognitively manageable components"""
        # Extract key components from request
        components = []
        component_keywords = {
            "Authentication": ["auth", "login", "security", "permission"],
            "Performance": ["caching", "performance", "optimization", "speed"],
            "Monitoring": ["monitoring", "logging", "tracking", "metrics"],
            "Infrastructure": ["load balancing", "database", "sharding", "scaling"],
            "Communication": ["message queuing", "distributed", "microservice"],
            "Observability": ["tracing", "debugging", "error handling"],
        }

        request_lower = request.lower()
        for component, keywords in component_keywords.items():
            if any(keyword in request_lower for keyword in keywords):
                components.append(component)

        if not components:
            components = ["Architecture", "Implementation", "Configuration"]

        # Limit to 7±2 components (Miller's Rule)
        if len(components) > 7:
            components = components[:7]

        result = "🧠 COGNITIVE OPTIMIZATION APPLIED\n"
        result += f"Breaking down complex system into {len(components)} manageable components:\n\n"

        for i, component in enumerate(components, 1):
            result += f"**{i}. {component}**\n"
            result += f"   - Implementation strategy for {component.lower()}\n"
            result += "   - Integration points with other components\n"
            result += "   - Performance and security considerations\n\n"

        result += "💡 **Next Steps:**\n"
        result += "1. Implement components in order of dependency\n"
        result += "2. Test each component individually before integration\n"
        result += "3. Monitor system performance at each stage\n"

        return result

    def _chunk_solution(self, lines: List[str]) -> str:
        """Break solution into 7±2 cognitive chunks"""
        chunks = []
        current_chunk = []

        for line in lines:
            current_chunk.append(line)
            if len(current_chunk) >= 5:  # Stay within 7±2
                chunks.append("\n".join(current_chunk))
                current_chunk = []

        if current_chunk:
            chunks.append("\n".join(current_chunk))

        # Present as numbered steps for cognitive clarity
        result = "COGNITIVE OPTIMIZATION APPLIED:\n\n"
        for i, chunk in enumerate(chunks, 1):
            result += f"Step {i}:\n{chunk}\n\n"

        return result
