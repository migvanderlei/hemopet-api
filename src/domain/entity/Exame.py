from datetime import date


class Exame():
    def __init__(
        self,
        data: date,
        url: str
    ):
        self.data = data
        self.url = url

    def reprJSON(self):
        return {
            "data": self.data.isoformat(),
            "url": self.url
        }
