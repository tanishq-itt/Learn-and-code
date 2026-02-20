import json


class JsonExporter:
    @staticmethod
    def export(records, file_path: str):
        with open(file_path, "w") as file:
            json.dump([record.to_dict() for record in records], file, indent=4)