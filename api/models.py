from tortoise import fields, models


class User(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=20)
    last_name = fields.CharField(max_length=30)
    email = fields.CharField(max_length=30)
    phone = fields.CharField(max_length=10)
    questions: fields.ReverseRelation["Question"]

    def __str__(self) -> str:
        return f"User {self.id}: {self.name} {self.last_name}"


class Question(models.Model):
    id = fields.UUIDField(pk=True)
    text = fields.TextField()
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="questions"
    )

    def __str__(self) -> str:
        return f"Question {self.id}: {self.text} from user with id {self.user}"
