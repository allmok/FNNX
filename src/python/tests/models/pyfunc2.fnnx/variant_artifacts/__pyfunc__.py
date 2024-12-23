from fnnx.variants.pyfunc import PyFunc
from compute import compute  # type: ignore


class TestFunc(PyFunc):

    def warmup(self):
        pass

    def compute(self, inputs, dynamic_attributes):
        return {"y": compute(inputs["x"])}

    async def compute_async(self, inputs, dynamic_attributes):
        return {"y": compute(inputs["x"])}
