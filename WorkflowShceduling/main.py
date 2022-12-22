import json
import sys


config_path = "/home/m812262/Simulator/OptimizationProblems/WorkflowShceduling/config/default_config.json"
with open(config_path, "r", encoding="utf-8") as f:
    arguments = json.loads(f.read())
    Problem_Settings = arguments.get("Problem")
    Generator_Settings = arguments.get("Generator_Settings")
    Tasks_Settings = arguments.get("Tasks_Settings")
    Algorithm_Parameter = arguments.get("Algorithm_Parameter")
f.close()
