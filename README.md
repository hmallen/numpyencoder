# numpyencoder

Custom Python JSON encoder for handling Numpy data types.

**Example Use:**

```python
from numpyencoder import NumpyEncoder

numpy_data = np.array([0, 1, 2, 3])

with open(json_file, 'w') as file:
    json.dump(numpy_data, file, indent=4, sort_keys=True,
              separators=(', ', ': '), ensure_ascii=False,
              cls=NumpyEncoder)
```
