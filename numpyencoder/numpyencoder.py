import warnings
from packaging.version import parse as parse_version
import json
import numpy as np


# Both np.float_ and np.complex_ were deprecated in Numpy 2.0.0
if np.__version__ < "2.0.0":
    TYPES = {
        "float": (np.float_, np.float16, np.float32, np.float64),
        "complex": (np.complex_, np.complex64, np.complex128),
    }
    warnings.warn(
        f"You are using an old version of Numpy ({np.__version__}), "
        "support for 'np.float_' and 'np.complex_' were deprecated "
        "in Numpy 2.0.0. If you use these datatypes in your code "
        "please consider updating them.",
        category=DeprecationWarning,
    )
else:
    TYPES = {
        "float": (np.float16, np.float32, np.float64),
        "complex": (np.complex64, np.complex128),
    }


class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy data types"""

    def default(self, obj):
        if isinstance(
            obj,
            (
                np.int_,
                np.intc,
                np.intp,
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
            ),
        ):
            return int(obj)

        elif isinstance(obj, TYPES["float"]):
            return float(obj)

        elif isinstance(obj, TYPES["complex"]):
            return {"real": obj.real, "imag": obj.imag}

        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()

        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)):
            return None

        return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    numpy_encoder = NumpyEncoder()
