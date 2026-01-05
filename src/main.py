from core.solver import NumericalSolver
from utils.config import load_config
import numpy as np

def run_simulation():
    # 1. Load Configuration
    cfg = load_config("configs/default.yaml")
    
    # 2. Setup Mock Mesh (In reality, load via src/data/loader.py)
    mock_mesh = np.eye(100) 
    
    # 3. Initialize and Run
    solver = NumericalSolver(mock_mesh, {"type": "dirichlet"})
    results = solver.solve()
    
    print(f"Simulation {cfg.project_name} completed. Result shape: {results.shape}")

if __name__ == "__main__":
    run_simulation()
