import graphene

from graphene_django.types import DjangoObjectType

from mysite.core.models import DataPoint, Layer, Map, User


class DataPointType(DjangoObjectType):
    class Meta:
        model = DataPoint


class LayerType(DjangoObjectType):
    class Meta:
        model = Layer


class MapType(DjangoObjectType):
    class Meta:
        model = Map


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    # all_users = graphene.Field(UserType, user_id=graphene.Int(
    #   required=False,
    #   default_value=None,
    # ))
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        can_edit=graphene.String(),
    )
    map = graphene.Field(
        MapType,
        id=graphene.Int(),
        title=graphene.String(),
    )
    all_maps = graphene.List(MapType)
    layer = graphene.Field(
        LayerType,
        id=graphene.Int(),
        map_id=graphene.Int(),
        title=graphene.String(),
        color=graphene.String(),
    )
    all_layers = graphene.List(LayerType)
    data_point = graphene.Field(
        DataPointType,
        id=graphene.Int(),
        layer_id=graphene.Int(),
        title=graphene.String(),
        size=graphene.Int(),
        latitude=graphene.Int(),
        longitude=graphene.Int(),
    )
    all_data_points = graphene.List(DataPointType)

    def resolve_all_maps(self, info, **kwargs):
        return Map.objects.all()

    def resolve_all_layers(self, info, **kwargs):
        return Layer.objects.select_realted('map_id').all()

    def resolve_all_data_points(self, info, **kwargs):
        return DataPoint.objects.select_realted('layer_id').all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        can_edit = kwargs.get('can_edit')

        if id is not None:
            return User.objects.get(pk=id)

        if can_edit is not None:
            return User.objects.get(can_edit=can_edit)

        return None

    def resolve_map(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Map.objects.get(pk=id)

        if title is not None:
            return Map.objects.get(title=title)

        return None

    def resolve_layer(self, info, **kwargs):
        id = kwargs.get('id')
        map_id = kwargs.get('map_id')
        title = kwargs.get('title')
        color = kwargs.get('color')

        if id is not None:
            return Layer.objects.get(layer_id=id)

        if map_id is not None:
            return Layer.objects.get(map_id=map_id)

        if title is not None:
            return Layer.objects.get(title=title)

        if color is not None:
            return Layer.objects.get(color=color)

        return None

    def resolve_data_point(self, info, **kwargs):
        id = kwargs.get('id')
        layer_id = kwargs.get('layer_id')
        title = kwargs.get('title')
        size = kwargs.get('size')
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')

        if id is not None:
            return DataPoint.objects.get(data_point_id=id)

        if layer_id is not None:
            return DataPoint.objects.get(map_id=layer_id)

        if title is not None:
            return DataPoint.objects.get(title=title)

        if size is not None:
            return DataPoint.objects.get(size=size)

        if latitude is not None:
            return DataPoint.objects.get(latitude=latitude)

        if longitude is not None:
            return DataPoint.objects.get(longitude=longitude)

        return None


schema = graphene.Schema(query=Query)
