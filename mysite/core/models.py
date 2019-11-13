from django.db import models


class User(models.Model):
    """The custom User model used for authentication and storing user data."""

    user_id = models.IntegerField(primary_key=True)
    can_edit = models.BooleanField()

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation containing the user_id."""
        return (
            'User(user_id={user_id})'
            .format(**self.__dict__)
        )


class Map(models.Model):
    """The custom Map model."""

    map_id = models.IntegerField(primary_key=True, unique=True)
    title = models.TextField()

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation containing the map_id and title."""
        return (
            'Map(map_id={map_id}, title={title})'
            .format(**self.__dict__)
        )


class Layer(models.Model):
    """The custom Layer model."""

    map_id = models.ForeignKey(
        Map,
        on_delete=models.CASCADE,
        related_name="layer",
    )
    layer_id = models.IntegerField(primary_key=True, unique=True)
    title = models.TextField()
    color = models.TextField()

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation containing the map_id and title."""
        return (
            'Layer(layer_id={layer_id}, title={title})'
            .format(**self.__dict__)
        )


class DataPoint(models.Model):
    """The custom data point model."""
    layer_id = models.ForeignKey(
        Layer,
        on_delete=models.CASCADE,
        related_name="data_point",
    )
    data_point_id = models.IntegerField(primary_key=True, unique=True)
    title = models.TextField()
    size = models.IntegerField()
    latitude = models.TextField()
    longitude = models.TextField()

    def __repr__(self) -> str:  # pragma: no cover
        """Return a string representation containing the map_id and title."""
        return (
            'DataPoint(data_point_id={data_point_id}, title={title})'
            .format(**self.__dict__)
        )
