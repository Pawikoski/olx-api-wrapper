from .olx import Olx
from .models import Thread, Message
from dacite import from_dict
from typing import List, Literal


class ThreadsMessages(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_threads(
        self,
        advert_id: int = None,
        interlocutor_id: int = None,
        offset: int = None,
        limit: int = None,
    ) -> List[Thread]:
        endpoint = self.endpoints["threads_messages"]["get_threads"]
        params = dict()
        if advert_id:
            params["advert_id"] = advert_id
        if interlocutor_id:
            params["interlocutor_id"] = interlocutor_id
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit

        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(Thread, obj) for obj in data]

    def get_thread(self, thread_id) -> Thread:
        endpoint = self.endpoints["threads_messages"]["get_thread"].format(id=thread_id)
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(Thread, data)

    def get_messages(
        self, thread_id: int, offset: int = None, limit: int = None
    ) -> List[Message]:
        endpoint = self.endpoints["threads_messages"]["get_messages"].format(
            id=thread_id
        )
        params = dict()
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit

        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(Message, obj) for obj in data]

    def post_message(self, thread_id: int, text: str, attachments: List[str] = None):
        endpoint = self.endpoints["threads_messages"]["post_message"].format(
            id=thread_id
        )
        payload = {"text": text}
        if attachments:
            payload["attachments"] = attachments
        response = self.post(endpoint, json=payload)
        data = response.json()["data"]
        return from_dict(Message, data)

    def get_message(self, thread_id: int, message_id: int):
        endpoint = self.endpoints["threads_messages"]["get_message"].format(
            thread_id=thread_id, message_id=message_id
        )
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(Message, data)

    def action_on_thread(
        self,
        thread_id: int,
        action: Literal["set-favourite", "mark-as-read"],
        is_favourite: bool = None,
    ):
        endpoint = self.endpoints["threads_messages"]["take_action_on_thread"].format(
            id=thread_id
        )
        payload = {"command": action}
        if action == "set-favourite":
            payload["is_favourite"] = is_favourite
        self.post(endpoint, json=payload, wanted_status=204)

    def mark_thread_as_read(self, thread_id: int):
        return self.action_on_thread(thread_id, "mark-as-read")

    def set_favourite(self, thread_id: int, action: bool):
        return self.action_on_thread(thread_id, "set-favourite", is_favourite=action)
