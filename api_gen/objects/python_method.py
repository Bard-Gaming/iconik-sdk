from api_gen.objects.python_function import PythonFunction


__all__ = ["PythonMethod"]


class PythonMethod(PythonFunction):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_parameter("self")
