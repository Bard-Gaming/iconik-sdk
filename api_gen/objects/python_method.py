from api_gen.objects.python_function import PythonFunction


class PythonMethod(PythonFunction):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_parameter("self")
