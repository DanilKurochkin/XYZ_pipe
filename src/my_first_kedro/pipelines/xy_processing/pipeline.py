from kedro.pipeline import Pipeline, node

from .nodes import merge_xy, calculate_length

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            #сначала объединям
            node(
                func = merge_xy,
                inputs=["X", "Y", "params:XY_parameters"],
                outputs="XY",
                name="merger"
            ),
            #потом считаем длину
            node(
                func=calculate_length,
                inputs="XY",
                outputs="XYLength",
                name="calculator"
            ),
        ]
    )