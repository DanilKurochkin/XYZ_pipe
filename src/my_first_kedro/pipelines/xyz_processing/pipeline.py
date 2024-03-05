from kedro.pipeline import Pipeline, node

from .nodes import merge_xyz, calculate_length

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func = merge_xyz,
                inputs=["XYLength", "Z"],
                outputs="XYZ",
                name="XYZmerger"
            ),
            node(
                func=calculate_length,
                inputs="XYZ",
                outputs="XYZLength",
                name="final_calculator"
            ),
        ]
    )