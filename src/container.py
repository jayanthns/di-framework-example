import inspect

class DIContainer:
    def __init__(self):
        self.registry = {}

    def register(self, cls):
        self.registry[cls.__name__] = cls

    def resolve(self, cls):
        if cls.__name__ in self.registry:
            dependencies = self.get_dependencies(cls)
            resolved_dependencies = [self.resolve(dep) for dep in dependencies]
            return self.registry[cls.__name__](*resolved_dependencies)
        else:
            raise Exception(f"Class {cls.__name__} is not registered in the container.")

    def get_dependencies(self, cls):
        dependencies = []
        if hasattr(cls, "__init__"):
            init_signature = inspect.signature(cls.__init__)
            parameters = init_signature.parameters.values()
            for param in parameters:
                if param.name != "self":
                    dependency_cls = param.annotation
                    if dependency_cls == inspect.Parameter.empty:
                        raise Exception(f"Unable to resolve dependency for parameter '{param.name}' in class '{cls.__name__}'")
                    dependencies.append(dependency_cls)
        return dependencies
