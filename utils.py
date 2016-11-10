from django.contrib.contenttypes.models import ContentType

from . import models as calification_engine_models

def get_all_calification_from_object(object):
    content_type = ContentType.objects.get_for_model(type(object))
    return calification_engine_models.Calification.objects.filter(
        content_type__pk=content_type.id,
        object__id=object.id
    )


def get_average_calification(object):
    all_califications = get_all_calification_from_object(object)
    return sum(x.rating for x in all_califications)/all_califications.count()


