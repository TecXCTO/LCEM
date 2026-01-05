from pydantic import BaseModel, Field

class SimulationConfig(BaseModel):
    project_name: str = "Structural_Analysis_2026"
    tolerance: float = Field(default=1e-6, gt=0)
    max_iterations: int = Field(default=1000, ge=1)
    use_gpu: bool = True

def load_config(path: str) -> SimulationConfig:
    # In a real app, load from YAML or JSON
    return SimulationConfig()
