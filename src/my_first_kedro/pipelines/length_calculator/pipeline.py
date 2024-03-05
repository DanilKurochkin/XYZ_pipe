from kedro.pipeline import Pipeline, node

from .nodes import merge_xyz, calculate_length

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func = merge_xyz,
                inputs=["X_scaled", "Y_scaled", "Z_scaled"],
                outputs=["XYZ_merged", "null_counter"],
                name="XYZmerger"
            ),
            node(
                func=calculate_length,
                inputs="XYZ_merged",
                outputs="XYZLength",
                name="final_calculator"
            ),
        ]
    )