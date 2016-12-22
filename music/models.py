# Create your models here.

import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.backends.postgresql.base import IntegrityError

logger = logging.getLogger(__name__)


class Feedback(models.Model):

    id = models.BigIntegerField(primary_key=True)
    feedback = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.id) + " " + self.feedback

    @staticmethod
    def select(id_):
        obj = None
        try:
            logger.debug("Get Feedback for id %s", id_)
            obj = Feedback.objects.get(pk=int(id_))
            logger.debug("Got Feedback %s", obj)
        except ObjectDoesNotExist as e:
            logger.debug("No Feedback object found for id %s", id_)
            logger.exception(e, "No Feedback object found for id " + id_)
            raise e
        return obj

    @staticmethod
    def insert(id_, desc_):
        obj = None
        try:
            obj = Feedback.objects.create(id=int(id_), feedback=desc_)
            obj.save()

        except (IntegrityError, Exception) as e:
            msg = "Object already exist for id : " + id_
            logging.error(msg, e)
            Feedback.update(id_, desc_)

    @staticmethod
    def update(id_, desc_):
        obj = None
        try:
            obj = Feedback.select(id_)
            obj.feedback = desc_
            obj.save(update_fields=['feedback'])

        except (IntegrityError, Exception) as e:
            msg = "Update failed for id : " + id_
            logging.error(msg, e)

    class Meta:
        db_table = 'feedback_form'

