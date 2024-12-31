from fnnx.variants.pyfunc import PyFunc


class TestFunc(PyFunc):
    def warmup(self):
        pass

    def compute(self, inputs, dynamic_attributes):
        prefix = inputs["x"]["prefix"]
        return {"y": {"out": f"{prefix} world"}}

    async def compute_async(self, inputs, dynamic_attributes):
        return {"y": self.compute(inputs, dynamic_attributes)}
