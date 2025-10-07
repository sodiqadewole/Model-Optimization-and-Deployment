from kfp import dsl
from kfp import compiler

# Define a simple component using a Python function
@dsl.component
def say_hello(name:str) -> str:
    hello_text = f'Hello, {name}'
    print(hello_text)
    return hello_text


# Define the pipeline using the @dsl.pipeline decorator
@dsl.pipeline(
    name='hello-world-pipeline',
    description='Basic pipeline that prints hello with user name.'
)
def hello_pipeline(recipient: str='World')->str:
    '''This pipeline runs the say_hello component'''
    hello_task = say_hello(name=recipient)
    return hello_task.output

if __name__ == '__main__':
    compiler.Compiler().compile(hello_pipeline, 'hello_world_pipeline.yaml')