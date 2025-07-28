"""
Basic Tests for Evolutionary Intelligence Framework
"""

import os
import shutil
import sys
import tempfile
import unittest

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from goose_evo import (  # noqa: E402
    FoundationIntelligence,
    ProcessIntelligence,
    EvolutionIntelligence,
    MinimalViableEcosystem,
    RealityConstraint,
    JSONPatternStore,
)


class TestFoundationIntelligence(unittest.TestCase):

    def setUp(self):
        self.foundation = FoundationIntelligence()

    def test_security_constraint_recognition(self):
        """Test that security constraints are properly recognized"""
        constraint = self.foundation.recognize_constraint(
            "I need secure authentication with rate limiting", {}
        )
        self.assertEqual(constraint.constraint_type, "security")
        self.assertGreater(constraint.reality_level, 0.8)

    def test_memory_constraint_recognition(self):
        """Test that memory constraints are properly recognized"""
        constraint = self.foundation.recognize_constraint(
            "Fix this memory leak in the application", {}
        )
        self.assertEqual(constraint.constraint_type, "memory")
        self.assertGreater(constraint.reality_level, 0.9)


class TestEvolutionIntelligence(unittest.TestCase):

    def setUp(self):
        self.evolution = EvolutionIntelligence()

    def test_pattern_learning(self):
        """Test that patterns are learned and can be applied"""

        # Create a constraint
        constraint = RealityConstraint(
            constraint_type="security",
            reality_level=0.85,
            context="test security",
            causal_mechanism="test",
        )

        # Encode a successful solution
        self.evolution.encode_constraint_solution(constraint, "test solution", True)

        # Check that pattern was learned
        self.assertGreater(len(self.evolution.dna_patterns), 0)

        # Check that pattern can be applied
        learned_solution = self.evolution.apply_learned_pattern(constraint)
        self.assertIsNotNone(learned_solution)


class TestEcosystemIntegration(unittest.TestCase):

    def setUp(self):
        self.ecosystem = MinimalViableEcosystem()

    def test_end_to_end_processing(self):
        """Test complete ecosystem processing"""
        response = self.ecosystem.process_request("Build secure login system")

        # Check that response has all required fields
        required_fields = [
            "solution",
            "solution_type",
            "constraint_analysis",
            "processing_time",
            "reality_alignment",
            "seven_dimensions_active",
        ]

        for field in required_fields:
            self.assertIn(field, response)

        # Check that constraint was properly analyzed
        self.assertIsInstance(response["constraint_analysis"], dict)
        self.assertIn("constraint_type", response["constraint_analysis"])


class TestProcessIntelligence(unittest.TestCase):

    def setUp(self):
        self.process = ProcessIntelligence()

    def test_cognitive_chunking_applied(self):
        """Test that complex solutions are properly chunked"""
        # Create a complex constraint
        constraint = RealityConstraint(
            constraint_type="cognitive_load",
            reality_level=0.9,
            context=(
                "Design complete microservice architecture with authentication, "
                "caching, monitoring, logging, error handling, rate limiting, "
                "load balancing, database sharding, message queuing, and "
                "distributed tracing for enterprise scale"
            ),
            causal_mechanism="Human 7±2 limit",
        )

        solution = "Simple solution"
        result = self.process.optimize_cognitive_load(solution, constraint)

        # Should trigger chunking for complex request
        self.assertIn("COGNITIVE OPTIMIZATION APPLIED", result)
        self.assertTrue(self.process.cognitive_patterns.get("chunking_applied", False))

    def test_reality_constraint_marking(self):
        """Test that high reality constraints are properly marked"""
        constraint = RealityConstraint(
            constraint_type="memory",
            reality_level=0.95,
            context="memory optimization",
            causal_mechanism="Hardware limitation",
        )

        solution = "Optimize memory usage"
        result = self.process.optimize_cognitive_load(solution, constraint)

        # Should add reality constraint marker
        self.assertIn("🔥 REALITY CONSTRAINT", result)
        self.assertIn("Hardware limitation", result)


class TestJSONPatternStore(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.pattern_file = os.path.join(self.temp_dir, "test_patterns.json")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_save_and_load_patterns(self):
        """Test basic save and load functionality"""
        store = JSONPatternStore(self.pattern_file)

        patterns = {
            "test_pattern": {
                "constraint_signature": "security_0.8",
                "transformation_method": "test method",
                "success_rate": 0.85,
                "usage_count": 5,
                "created_at": "2024-01-01T00:00:00",
            }
        }

        # Save patterns
        result = store.save_patterns(patterns)
        self.assertTrue(result)

        # Load patterns
        loaded = store.load_patterns()
        self.assertEqual(loaded, patterns)

    def test_clear_patterns(self):
        """Test pattern clearing functionality"""
        store = JSONPatternStore(self.pattern_file)

        # Save some patterns first
        patterns = {"test": "data"}
        store.save_patterns(patterns)

        # Verify they exist
        loaded = store.load_patterns()
        self.assertEqual(loaded, patterns)

        # Clear patterns
        result = store.clear_patterns()
        self.assertTrue(result)

        # Verify they're gone
        loaded = store.load_patterns()
        self.assertEqual(loaded, {})

    def test_load_nonexistent_file(self):
        """Test loading from non-existent file returns empty dict"""
        store = JSONPatternStore(os.path.join(self.temp_dir, "nonexistent.json"))
        loaded = store.load_patterns()
        self.assertEqual(loaded, {})


class TestPatternPersistence(unittest.TestCase):

    def setUp(self):
        # Create temporary directory for test patterns
        self.temp_dir = tempfile.mkdtemp()
        self.pattern_file = os.path.join(self.temp_dir, "test_patterns.json")
        self.pattern_store = JSONPatternStore(self.pattern_file)

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.temp_dir)

    def test_pattern_persistence_across_instances(self):
        """Test that learned patterns persist across two MinimalViableEcosystem instances"""
        # Create first ecosystem instance
        ecosystem1 = MinimalViableEcosystem(pattern_store=self.pattern_store)

        # Create a constraint and encode a solution
        constraint = RealityConstraint(
            constraint_type="security",
            reality_level=0.85,
            context="test security pattern",
            causal_mechanism="Attack surface reality",
        )

        ecosystem1.evolution.encode_constraint_solution(
            constraint, "Test security solution", True
        )
        initial_pattern_count = len(ecosystem1.evolution.dna_patterns)

        # Verify pattern was learned
        self.assertGreater(initial_pattern_count, 0)

        # Create second ecosystem instance with same pattern store
        ecosystem2 = MinimalViableEcosystem(pattern_store=self.pattern_store)

        # Verify patterns were loaded
        self.assertEqual(len(ecosystem2.evolution.dna_patterns), initial_pattern_count)

        # Verify the specific pattern exists and can be applied
        learned_solution = ecosystem2.evolution.apply_learned_pattern(constraint)
        self.assertIsNotNone(learned_solution)
        self.assertIn("LEARNED PATTERN APPLIED", learned_solution)

    def test_pattern_store_fallback(self):
        """Test that system falls back gracefully when pattern store is unavailable"""
        # Create ecosystem with no pattern store
        ecosystem = MinimalViableEcosystem(pattern_store=None)

        # Should still work, just without persistence
        response = ecosystem.process_request("Test security request")
        self.assertIn("solution", response)
        self.assertIn("constraint_analysis", response)


class TestHarmonyIntelligence(unittest.TestCase):

    def setUp(self):
        from goose_evo import HarmonyIntelligence

        self.foundation = FoundationIntelligence()
        self.process = ProcessIntelligence()
        self.evolution = EvolutionIntelligence()
        self.harmony = HarmonyIntelligence(
            self.foundation, self.process, self.evolution
        )

    def test_orchestrate_response_new_solution(self):
        """Test orchestrated response for new constraints"""
        response = self.harmony.orchestrate_response("Need secure database connection")

        # Check response structure
        self.assertIn("solution", response)
        self.assertIn("solution_type", response)
        self.assertIn("constraint_analysis", response)
        self.assertIn("processing_time", response)
        self.assertIn("reality_alignment", response)

        # Should be new generation since no learned patterns
        self.assertEqual(response["solution_type"], "NEW_GENERATION")

    def test_record_feedback(self):
        """Test feedback recording functionality"""
        response = self.harmony.orchestrate_response("Test security request")

        # Record positive feedback
        initial_patterns = len(self.evolution.dna_patterns)
        self.harmony.record_feedback("Test security request", response, True)

        # Should have learned a new pattern
        self.assertGreater(len(self.evolution.dna_patterns), initial_patterns)


class TestAdvancedEcosystemScenarios(unittest.TestCase):

    def setUp(self):
        self.ecosystem = MinimalViableEcosystem()

    def test_demonstrate_learning_with_feedback(self):
        """Test the complete learning demonstration cycle"""
        demo_result = self.ecosystem.demonstrate_learning(
            "Implement secure authentication system", feedback=True
        )

        self.assertIn("SEVEN-DIMENSIONAL ECOSYSTEM DEMONSTRATION", demo_result)
        self.assertIn("LEARNING ENCODED", demo_result)

        # Should have saved verification time
        self.assertGreater(self.ecosystem.verification_time_saved, 0)

    def test_demonstrate_learning_negative_feedback(self):
        """Test learning demonstration with negative feedback"""
        demo_result = self.ecosystem.demonstrate_learning(
            "Bad request example", feedback=False
        )

        self.assertIn("LEARNING OPPORTUNITY", demo_result)

    def test_calculate_verification_time_complexity(self):
        """Test verification time calculation with different complexity levels"""
        # Simple request
        simple_response = self.ecosystem.process_request("Fix memory leak")
        simple_time = self.ecosystem._calculate_verification_time(
            "Fix memory leak", simple_response
        )

        # Complex request
        complex_response = self.ecosystem.process_request(
            (
                "Design complex enterprise microservice architecture with "
                "multiple distributed components"
            )
        )
        complex_time = self.ecosystem._calculate_verification_time(
            (
                "Design complex enterprise microservice architecture with "
                "multiple distributed components"
            ),
            complex_response,
        )

        # Complex should take longer
        self.assertGreater(complex_time, simple_time)

    def test_multiple_interactions_increase_patterns(self):
        """Test that multiple interactions increase learned patterns"""
        # Start with fresh ecosystem to avoid seeded demo patterns
        fresh_ecosystem = MinimalViableEcosystem()
        # Clear any seeded patterns
        fresh_ecosystem.evolution.dna_patterns.clear()
        initial_patterns = len(fresh_ecosystem.evolution.dna_patterns)

        # Process several requests with different constraint types
        requests = [
            "Secure authentication system with rate limiting",
            "Database performance optimization with caching",
            "Memory leak detection and garbage collection",
            "Load balancing configuration for microservices",
        ]

        for request in requests:
            fresh_ecosystem.demonstrate_learning(request, feedback=True)

        # Should have learned more patterns
        final_patterns = len(fresh_ecosystem.evolution.dna_patterns)
        self.assertGreater(final_patterns, initial_patterns)


class TestGrantDemonstration(unittest.TestCase):

    def test_run_grant_demonstration(self):
        """Test that grant demonstration runs without errors"""
        import io
        import sys

        # Capture stdout to avoid cluttering test output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            from goose_evo import run_grant_demonstration

            # This should run without exceptions
            run_grant_demonstration()

            # Get the output
            output = captured_output.getvalue()

            # Check for key demonstration elements
            self.assertIn("GRANT DEMONSTRATION", output)
            self.assertIn("VERIFICATION BOTTLENECK ELIMINATION", output)
            self.assertIn("SCENARIO 1", output)
            self.assertIn("SCENARIO 2", output)
            self.assertIn("SCENARIO 3", output)

        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__


class TestConstraintTypeRecognition(unittest.TestCase):

    def setUp(self):
        self.foundation = FoundationIntelligence()

    def test_latency_constraint_recognition(self):
        """Test latency constraint recognition"""
        constraint = self.foundation.recognize_constraint(
            "API response is slow and timing out", {}
        )
        self.assertEqual(constraint.constraint_type, "latency")
        self.assertGreater(constraint.reality_level, 0.8)

    def test_scalability_constraint_recognition(self):
        """Test scalability constraint recognition"""
        constraint = self.foundation.recognize_constraint(
            "Need to scale microservice under load", {}
        )
        self.assertEqual(constraint.constraint_type, "scalability")
        self.assertGreater(constraint.reality_level, 0.7)

    def test_cognitive_load_constraint_recognition(self):
        """Test cognitive load constraint recognition"""
        constraint = self.foundation.recognize_constraint(
            "This is too complex and overwhelming with many components", {}
        )
        self.assertEqual(constraint.constraint_type, "cognitive_load")
        self.assertGreater(constraint.reality_level, 0.8)

    def test_artificial_constraint_fallback(self):
        """Test fallback to artificial constraint for unknown patterns"""
        constraint = self.foundation.recognize_constraint(
            "Something completely unrelated to known patterns", {}
        )
        self.assertEqual(constraint.constraint_type, "artificial")
        self.assertEqual(constraint.reality_level, 0.3)


if __name__ == "__main__":
    unittest.main()
