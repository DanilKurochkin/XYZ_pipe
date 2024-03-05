from kedro.pipeline import Pipeline, node

from .nodes import merge_xy, calculate_length

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func = merge_xy,
                inputs=["X", "Y"],
                outputs="XY",
                name="merger"
            ),
            node(
                func=calculate_length,
                inputs="XY",
                outputs="XYLength",
                name="calculator"
            ),
        ]
    )