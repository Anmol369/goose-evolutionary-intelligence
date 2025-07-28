# Contributing to Goose Evolutionary Intelligence

Thank you for your interest in contributing to the seven-dimensional self-improving AI framework! This project implements natural intelligence patterns proven over 4 billion years of evolution.

## Development Workflow

### Fork → Feature Branch → Pull Request

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR-USERNAME/goose-evolutionary-intelligence.git
   cd goose-evolutionary-intelligence
   ```

2. **Set up development environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install in development mode
   pip install -e .
   pip install -e .[dev]
   ```

3. **Create feature branch**
   ```bash
   # Always branch from master
   git checkout master
   git pull upstream master
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Follow the seven-dimensional architecture principles
   - Add tests for new functionality
   - Update documentation as needed
   - Ensure changes align with natural intelligence patterns

5. **Run pre-commit checks**
   ```bash
   # Install pre-commit hooks
   pre-commit install
   
   # Run all checks manually
   pre-commit run --all-files
   ```

6. **Test your changes**
   ```bash
   # Run the test suite
   pytest tests/ -v
   
   # Run benchmarks to ensure no performance regression
   python examples/benchmark.py --runs 3
   
   # Test CLI functionality
   goose-evo-demo --help
   goose-evo-demo --trace
   ```

7. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   - Go to GitHub and create a Pull Request
   - Use the PR template to describe your changes
   - Link any related issues

## Pre-commit Hooks

This project uses pre-commit hooks to maintain code quality:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100, --extend-ignore=E203,W503]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--ignore-missing-imports]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

Install and activate:
```bash
pip install pre-commit
pre-commit install
```

## Code Style Guidelines

### Seven-Dimensional Architecture
- Each component should embody one of the seven intelligence dimensions
- Maintain separation of concerns between dimensions
- Ensure all dimensions work in harmony

### Python Style
- Follow PEP 8 with 100-character line limit
- Use type hints for all function signatures
- Write docstrings for all public methods
- Use meaningful variable names that reflect natural intelligence concepts

### Testing
- Write tests for all new functionality
- Aim for >90% code coverage
- Include integration tests for CLI features
- Add benchmark tests for performance-critical changes

### Documentation
- Update README.md if adding user-facing features
- Add docstrings with examples for complex functions
- Update architecture documentation for structural changes

## Contribution Areas

### 🌱 Foundation Intelligence
- Reality constraint detection improvements
- New constraint types and validation
- Physics-based constraint modeling

### ⚛️ Process Intelligence
- Cognitive load optimization algorithms
- Human-computer interaction improvements
- Information architecture enhancements

### 🧬 Evolution Intelligence
- Learning algorithm improvements
- Pattern storage optimizations
- DNA encoding enhancements

### 🎵 Harmony Intelligence
- Multi-agent coordination protocols
- Consensus algorithms
- Resonance pattern matching

### 🏹 Survival Intelligence
- Verification time reduction techniques
- Performance optimization
- Bottleneck elimination strategies

### 📊 Scale Intelligence
- Scalability improvements
- Distributed system support
- Emergence pattern recognition

### 🌌 Orchestration Intelligence
- Meta-learning algorithms
- System evolution capabilities
- Auto-improvement mechanisms

## Issue Guidelines

### Bug Reports
- Use the bug report template
- Include system information and reproduction steps
- Provide benchmark results if performance-related

### Feature Requests
- Align with seven-dimensional framework
- Explain how it eliminates verification bottlenecks
- Consider natural intelligence patterns

### Performance Issues
- Include benchmark results
- Specify which intelligence dimension is affected
- Provide profiling information if available

## Review Process

1. **Automated Checks**: All PRs must pass CI/CD pipeline
2. **Code Review**: At least one maintainer approval required
3. **Benchmark Review**: Performance regression analysis
4. **Documentation Review**: Ensure docs are updated
5. **Integration Testing**: Manual testing of new features

## Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes for significant contributions
- Pattern attribution for algorithm improvements

## Questions?

- Open a discussion on GitHub
- Join our community channels
- Review existing issues and documentation

---

*"Things don't change the world, people change the world by using things."*

Thank you for helping build the future of verification-free AI development!