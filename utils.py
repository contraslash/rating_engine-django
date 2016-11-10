from django.contrib.contenttypes.models import ContentType

from . import models as calification_engine_models

def get_all_calification_from_object(content_object):
    content_type = ContentType.objects.get_for_model(type(content_object))
    return calification_engine_models.Calification.objects.filter(
        content_type__pk=content_type.id,
        object_id=content_object.id
    )


def get_average_calification(content_object):
    all_califications = get_all_calification_from_object(content_object)
    return sum(x.rating for x in all_califications)/all_califications.count()


