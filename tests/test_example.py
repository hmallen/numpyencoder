def test_array_of_int():
    import json
    import numpy as np
    from numpyencoder import NumpyEncoder

    numpy_data = np.array([np.int64(0), np.int32(1), 2, 3])
    baseline_data = [0, 1, 2, 3]

    j_np = json.dumps(numpy_data, sort_keys=True,
                      separators=(', ', ': '), ensure_ascii=False,
                      cls=NumpyEncoder)

    assert json.dumps(baseline_data, sort_keys=True) == j_np
