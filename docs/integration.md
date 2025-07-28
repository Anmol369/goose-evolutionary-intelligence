# 🔌 Integration Guide

## Overview

The Goose Evolutionary Intelligence framework provides a seven-dimensional AI system that eliminates verification bottlenecks through natural intelligence patterns. This guide shows how to integrate the framework into your projects.

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from goose_evo import MinimalViableEcosystem

# Initialize the ecosystem
ecosystem = MinimalViableEcosystem()

# Process a development task
result = ecosystem.process_task("Create a Python function that validates email addresses")

# The system learns from corrections and improves over time
ecosystem.learn_from_feedback(result, "Good structure, but needs better regex pattern")
```

## Seven-Dimensional Integration

### 1. Foundation Intelligence
Reality-aligned constraint recognition for your domain:

```python
from goose_evo import FoundationIntelligence, RealityConstraint

foundation = FoundationIntelligence()

# Define constraints for your domain
constraints = [
    RealityConstraint("performance", "Response time must be < 100ms"),
    RealityConstraint("security", "All inputs must be sanitized"),
    RealityConstraint("maintainability", "Code coverage must be > 80%")
]

foundation.add_constraints(constraints)
```

### 2. Process Intelligence
Human cognitive optimization following the 7±2 principle:

```python
from goose_evo import ProcessIntelligence

process = ProcessIntelligence()

# Chunk complex tasks into manageable pieces
chunked_tasks = process.chunk_task(complex_task, max_items=7)

# Optimize workflow based on cognitive load
optimized_workflow = process.optimize_cognitive_load(workflow)
```

### 3. Evolution Intelligence
Learn from corrections and improve over time:

```python
from goose_evo import EvolutionIntelligence

evolution = EvolutionIntelligence()

# Register patterns from corrections
evolution.learn_pattern(
    context="email validation",
    correction="Use re.IGNORECASE flag for case-insensitive matching",
    improvement_type="enhancement"
)

# Apply learned patterns to new tasks
enhanced_result = evolution.enhance_with_patterns(base_result, context="email validation")
```

### 4. Harmony Intelligence
Multi-agent coordination:

```python
from goose_evo import HarmonyIntelligence

harmony = HarmonyIntelligence()

# Coordinate multiple AI agents
agents = ["code_generator", "test_writer", "reviewer"]
coordinated_result = harmony.coordinate_agents(agents, task)
```

## Integration Patterns

### Web Application Integration

```python
from flask import Flask, request, jsonify
from goose_evo import MinimalViableEcosystem

app = Flask(__name__)
ecosystem = MinimalViableEcosystem()

@app.route('/generate', methods=['POST'])
def generate_code():
    task = request.json['task']
    result = ecosystem.process_task(task)
    return jsonify(result)

@app.route('/feedback', methods=['POST'])
def provide_feedback():
    result_id = request.json['result_id']
    feedback = request.json['feedback']
    ecosystem.learn_from_feedback(result_id, feedback)
    return jsonify({"status": "learned"})
```

### CLI Tool Integration

```python
import click
from goose_evo import MinimalViableEcosystem

@click.command()
@click.option('--task', help='Development task to process')
@click.option('--learn', help='Provide feedback for learning')
def main(task, learn):
    ecosystem = MinimalViableEcosystem()
    
    if task:
        result = ecosystem.process_task(task)
        click.echo(f"Generated: {result}")
    
    if learn:
        ecosystem.learn_from_feedback(learn)
        click.echo("Feedback processed")

if __name__ == '__main__':
    main()
```

### IDE Plugin Integration

```python
class GooseEvoPlugin:
    def __init__(self):
        self.ecosystem = MinimalViableEcosystem()
    
    def on_code_completion(self, context):
        suggestions = self.ecosystem.generate_completions(context)
        return suggestions
    
    def on_error_fix(self, error, code):
        fix = self.ecosystem.suggest_fix(error, code)
        return fix
    
    def on_user_correction(self, original, corrected):
        self.ecosystem.learn_from_correction(original, corrected)
```

## Configuration

### Pattern Store Configuration

```python
from goose_evo import JSONPatternStore

# Use custom pattern storage
pattern_store = JSONPatternStore("custom_patterns.json")
ecosystem = MinimalViableEcosystem(pattern_store=pattern_store)
```

### Reality Constraints Configuration

```python
# Domain-specific constraints
web_constraints = [
    RealityConstraint("security", "All routes must be authenticated"),
    RealityConstraint("performance", "Database queries must use indexes"),
    RealityConstraint("scalability", "Functions must be stateless")
]

ecosystem.foundation.add_constraints(web_constraints)
```

## Advanced Features

### Custom Learning Patterns

```python
from goose_evo import EvolutionaryPattern

# Define custom improvement patterns
pattern = EvolutionaryPattern(
    name="error_handling",
    context_matcher=lambda ctx: "exception" in ctx.lower(),
    improvement_strategy="wrap_in_try_catch",
    confidence=0.8
)

ecosystem.evolution.add_pattern(pattern)
```

### Multi-Project Learning

```python
# Share patterns across projects
shared_store = JSONPatternStore("shared_patterns.json")

project_a = MinimalViableEcosystem(pattern_store=shared_store)
project_b = MinimalViableEcosystem(pattern_store=shared_store)

# Both projects learn from each other's corrections
```

## Best Practices

### 1. Start Small
Begin with basic task processing and gradually add dimensional intelligence:

```python
# Phase 1: Basic processing
ecosystem = MinimalViableEcosystem()
result = ecosystem.process_task(simple_task)

# Phase 2: Add learning
ecosystem.learn_from_feedback(result, feedback)

# Phase 3: Add constraints
ecosystem.foundation.add_constraints(domain_constraints)
```

### 2. Provide Quality Feedback
The system learns from corrections, so provide specific, actionable feedback:

```python
# Good feedback
ecosystem.learn_from_feedback(
    result,
    "Add input validation for null values and use more descriptive variable names"
)

# Poor feedback
ecosystem.learn_from_feedback(result, "This is wrong")
```

### 3. Monitor Learning Progress
Track how the system improves over time:

```python
# Get learning metrics
metrics = ecosystem.get_learning_metrics()
print(f"Patterns learned: {metrics['pattern_count']}")
print(f"Improvement rate: {metrics['improvement_rate']}")
```

## Troubleshooting

### Common Issues

**Issue**: System not learning from feedback
**Solution**: Ensure feedback is specific and context is preserved

**Issue**: Poor performance on domain-specific tasks
**Solution**: Add relevant reality constraints for your domain

**Issue**: Inconsistent results
**Solution**: Verify pattern store persistence and check constraint conflicts

### Debug Mode

```python
# Enable detailed logging
ecosystem = MinimalViableEcosystem(debug=True)

# Check internal state
ecosystem.debug_state()
```

## Support

- **Documentation**: [Technical Architecture](architecture.md)
- **Patterns**: [Natural Intelligence Patterns](natural_patterns.md)
- **Issues**: Create GitHub issues for bugs and feature requests
- **Community**: Join discussions about natural intelligence patterns

## Next Steps

1. Try the basic integration with your current project
2. Add domain-specific reality constraints
3. Implement feedback loops for continuous learning
4. Explore advanced multi-agent coordination patterns

The framework is designed to eliminate verification bottlenecks through natural intelligence patterns proven over 4 billion years of evolution.