from datetime import date


class Doacao():
    def __init__(
        self,
        data: date,
    ):
        self.data = data

    def reprJSON(self):
        return {
            "data": self.data.isoformat()
        }
