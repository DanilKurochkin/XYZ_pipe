from kedro.pipeline import Pipeline, node, pipeline

from .nodes import scale

def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance = Pipeline(
        [
            #масштабируем
            node(
                func = scale,
                inputs=["values", "params:parameters"],
                outputs="scaled_values",
                name="scaler"
            )
        ]
    )
    
    pipes = []
    for char in ['X', 'Y', 'Z']:
        new_pipe = pipeline(
            pipeline_instance,
            inputs={"values" : char},
            outputs={"scaled_values" : f"{char}_scaled"},
            namespace=char
        )
        pipes.append(new_pipe)
    
    return sum(pipes)