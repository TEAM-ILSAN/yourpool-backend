from django.db import models

class Evaluation(models.Model):
    credit = models.IntegerField()
    # target_user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)      // 주석 풀면 에러남
    evaluation_user_id = models.IntegerField()
    content = models.CharField(max_length=300)

    class Meta:
        db_table = 'evaluations'
