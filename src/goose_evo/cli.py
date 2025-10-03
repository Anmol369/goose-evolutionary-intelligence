#!/usr/bin/env python3
"""
CLI interface for Goose Evolutionary Intelligence
Provides command-line access to the seven-dimensional ecosystem
"""

import argparse
import sys
import json

# Fix Windows console encoding for emoji support
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7, fallback to wrapping
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from .ecosystem import MinimalViableEcosystem
from .pattern_store import JSONPatternStore


def create_parser():
    """Create and configure the CLI argument parser"""
    parser = argparse.ArgumentParser(
        prog="goose-evo-demo",
        description="Seven-Dimensional Self-Improving AI Agents for Goose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--trace",
        action="store_true",
        help="Enable detailed tracing of ecosystem processing",
    )

    parser.add_argument(
        "--persist-store",
        type=str,
        metavar="PATH",
        help="Path to persistent pattern store file (default: memory only)",
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode for continuous learning",
    )

    parser.add_argument(
        "--benchmark", action="store_true", help="Run verification time benchmarks"
    )

    return parser


def setup_ecosystem(args):
    """Initialize the ecosystem based on CLI arguments"""
    pattern_store = None

    if args.persist_store:
        pattern_store = JSONPatternStore(store_path=args.persist_store)
        if args.trace:
            print(f"📁 Using persistent pattern store: {args.persist_store}")
    elif args.trace:
        print("💾 Using in-memory pattern store")

    ecosystem = MinimalViableEcosystem(pattern_store=pattern_store)

    if args.trace:
        print("🌱 Seven-dimensional ecosystem initialized")
        print(f"🧬 Loaded patterns: {len(ecosystem.evolution.dna_patterns)}")

    return ecosystem


def run_interactive_mode(ecosystem, trace=False):
    """Run the ecosystem in interactive mode"""
    print("\n🌱 INTERACTIVE SEVEN-DIMENSIONAL ECOSYSTEM")
    print("Type 'quit' or 'exit' to end session")
    print("Type 'stats' to see ecosystem statistics")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n💬 Your request: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                break
            elif user_input.lower() == "stats":
                stats = {
                    "total_interactions": ecosystem.total_interactions,
                    "learned_patterns": len(ecosystem.evolution.dna_patterns),
                    "verification_time_saved": f"{ecosystem.verification_time_saved:.1f}s",
                }
                print("\n>> Ecosystem Statistics:")
                print(json.dumps(stats, indent=2))
                continue
            elif not user_input:
                continue

            if trace:
                print(f"🔍 Processing: {user_input}")

            # Process the request
            response = ecosystem.process_request(user_input)

            # Display response
            print(f"\n🎯 Response: {response['response']}")
            if trace:
                print(f"🧬 Constraint Analysis: {response['constraint_analysis']}")
                print(f"📈 Reality Alignment: {response['reality_alignment']:.1%}")
                print(f"⚡ Processing Quality: {response['processing_quality']:.1%}")

            # Ask for feedback
            feedback_input = (
                input("\n👍 Was this helpful? (y/n/skip): ").strip().lower()
            )
            if feedback_input in ["y", "yes"]:
                ecosystem.harmony.record_feedback(user_input, response, True)
                print("✅ Positive feedback recorded - pattern strengthened")
            elif feedback_input in ["n", "no"]:
                ecosystem.harmony.record_feedback(user_input, response, False)
                print("📚 Negative feedback recorded - system will adapt")

        except KeyboardInterrupt:
            print("\n\n👋 Session ended by user")
            break
        except EOFError:
            print("\n\n👋 Session ended")
            break

    # Show final statistics
    print("\n>> Final Session Statistics:")
    print(f"🔢 Total interactions: {ecosystem.total_interactions}")
    print(f"🧬 Patterns learned: {len(ecosystem.evolution.dna_patterns)}")
    print(f"⏱️  Verification time saved: {ecosystem.verification_time_saved:.1f}s")


def run_benchmark_mode(ecosystem, trace=False):
    """Run verification time benchmarks"""
    from examples.benchmark import run_benchmarks

    if trace:
        print("🏃 Running verification time benchmarks...")

    try:
        results = run_benchmarks(ecosystem, runs=5, trace=trace)
        print("\n📊 Benchmark Results:")
        print(json.dumps(results, indent=2))
    except ImportError:
        print(
            "❌ Benchmark module not found. Please ensure examples/benchmark.py exists."
        )
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()

    try:
        ecosystem = setup_ecosystem(args)

        if args.benchmark:
            run_benchmark_mode(ecosystem, trace=args.trace)
        elif args.interactive:
            run_interactive_mode(ecosystem, trace=args.trace)
        else:
            # Default: run the grant demonstration
            from .ecosystem import run_grant_demonstration

            if args.trace:
                print("🎬 Running grant demonstration with tracing enabled")
            run_grant_demonstration()

    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        if args.trace:
            import traceback

            traceback.print_exc()
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
