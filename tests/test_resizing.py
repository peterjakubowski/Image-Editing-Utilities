import pytest

from src.image_utils.resizing import rescale_width_height


class TestRescaleWidthHeight:
    def test_rescale_width_height_returns_tuple(self):

        test_data = {"width": 200, "height": 300, "size": 100}

        results = rescale_width_height(**test_data)

        assert isinstance(results, tuple)

    def test_rescale_width_height_returns_two_values(self):

        test_data = {"width": 200, "height": 300, "size": 100}

        results = rescale_width_height(**test_data)

        assert len(results) == 2

    def test_rescale_width_height_returns_integer_values(self):

        test_data = {"width": 200, "height": 300, "size": 100}

        results = rescale_width_height(**test_data)

        assert isinstance(results[0], int)
        assert isinstance(results[1], int)

    def test_rescale_width_height_calculates_height_when_width_longest(self):

        test_data = {"width": 200, "height": 100, "size": 100}

        results = rescale_width_height(**test_data)

        assert results == (100, 50)

    def test_rescale_width_height_calculates_width_when_height_longest(self):

        test_data = {"width": 100, "height": 200, "size": 100}

        results = rescale_width_height(**test_data)

        assert results == (50, 100)

    def test_rescale_width_height_calculates_width_and_height_when_equal(self):

        test_data = {"width": 300, "height": 300, "size": 100}

        results = rescale_width_height(**test_data)

        assert results == (100, 100)

    def test_rescale_width_height_raises_type_error_when_width_is_string(self):

        test_data = {"width": "300", "height": 300, "size": 100}

        with pytest.raises(TypeError, match="Width cannot be str"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_type_error_when_height_is_string(self):

        test_data = {"width": 300, "height": "300", "size": 100}

        with pytest.raises(TypeError, match="Height cannot be str"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_type_error_when_size_is_string(self):

        test_data = {"width": 300, "height": 300, "size": "100"}

        with pytest.raises(TypeError, match="Size cannot be str"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_type_error_when_width_is_float(self):

        test_data = {"width": 300.0, "height": 300, "size": 100}

        with pytest.raises(TypeError, match="Width cannot be float"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_type_error_when_height_is_float(self):

        test_data = {"width": 300, "height": 300.0, "size": 100}

        with pytest.raises(TypeError, match="Height cannot be float"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_type_error_when_size_is_float(self):

        test_data = {"width": 300, "height": 300, "size": 100.0}

        with pytest.raises(TypeError, match="Size cannot be float"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_width_is_negative(self):

        test_data = {"width": -300, "height": 300, "size": 100}

        with pytest.raises(ValueError, match="Width cannot be negative"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_height_is_negative(self):

        test_data = {"width": 300, "height": -300, "size": 100}

        with pytest.raises(ValueError, match="Height cannot be negative"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_size_is_negative(self):

        test_data = {"width": 300, "height": 300, "size": -100}

        with pytest.raises(ValueError, match="Size cannot be negative"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_width_is_zero(self):

        test_data = {"width": 0, "height": 300, "size": 100}

        with pytest.raises(ValueError, match="Width cannot be 0"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_height_is_zero(self):

        test_data = {"width": 300, "height": 0, "size": 100}

        with pytest.raises(ValueError, match="Height cannot be 0"):
            rescale_width_height(**test_data)

    def test_rescale_width_height_raises_value_error_when_size_is_zero(self):

        test_data = {"width": 300, "height": 300, "size": 0}

        with pytest.raises(ValueError, match="Size cannot be 0"):
            rescale_width_height(**test_data)
