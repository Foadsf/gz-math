import sys
import yaml

try:
    with open('.github/workflows/windows-ci.yml', 'r') as f:
        workflow = yaml.safe_load(f)
except Exception as e:
    print(f"Failed to parse workflow: {e}")
    sys.exit(1)

# Find configure step
configure_step_found = False
for job in workflow.get('jobs', {}).values():
    for step in job.get('steps', []):
        if step.get('name') == 'Configure':
            configure_step_found = True
            run_cmd = step.get('run', '')
            if 'SKIP_PYBIND11' in run_cmd:
                print("Error: SKIP_PYBIND11 is still present in the Configure step.")
                sys.exit(1)

if not configure_step_found:
    print("Error: Could not find 'Configure' step in workflow.")
    sys.exit(1)

try:
    with open('.github/ci/windows/pixi.toml', 'r') as f:
        content = f.read()
        if 'pybind11' not in content:
            print("Error: pybind11 not found in pixi.toml")
            sys.exit(1)
except Exception as e:
    print(f"Failed to read pixi.toml: {e}")
    sys.exit(1)

print("All checks passed.")
sys.exit(0)
