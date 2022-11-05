from django.db import models


class Evaluation(models.Model):
    credit = models.IntegerField()
    target_user_id = models.ForeignKey(
        "users.YourPoolUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="target_user",
    )
    evaluation_user_id = models.ForeignKey(
        "users.YourPoolUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="evaluation_user",
    )
    content = models.CharField(max_length=300)

    class Meta:
        db_table = "evaluations"
