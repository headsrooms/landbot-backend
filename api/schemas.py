from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class UserInput:
    name: str
    last_name: str
    email: str
    phone: str


@dataclass(frozen=True)
class QuestionInput:
    text: str
    user_id: str


@dataclass(frozen=True)
class UserResponse:
    id: str
    name: str
    last_name: str
    email: str
    phone: str

    def as_dict(self):
        output = asdict(self)
        return {k: str(v) for k, v in output.items()}


@dataclass(frozen=True)
class QuestionResponse:
    id: str
    text: str
    user_id: str

    def as_dict(self):
        output = asdict(self)
        return {k: str(v) for k, v in output.items()}
