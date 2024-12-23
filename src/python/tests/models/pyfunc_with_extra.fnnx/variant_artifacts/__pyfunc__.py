from fnnx.variants.pyfunc import PyFunc
import json
import numpy as np


class TestFunc(PyFunc):

    def warmup(self):
        pass

    def compute(self, inputs, dynamic_attributes):
        val3 = self.fnnx_context.get_value("val3")
        val1p = self.fnnx_context.get_filepath("val1.json")
        val2p = self.fnnx_context.get_filepath("subdir/val2.json")

        with open(val1p, "r") as f:
            val1 = json.load(f)
        with open(val2p, "r") as f:
            val2 = json.load(f)
        out = np.asarray(val1) + np.asarray(val2) + np.asarray(val3)
        return {"y": out}

    async def compute_async(self, inputs, dynamic_attributes):
        return self.compute(inputs, dynamic_attributes)
