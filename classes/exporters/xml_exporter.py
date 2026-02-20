class XmlExporter:
    @staticmethod
    def export(records, file_path: str):
        lines = ['<?xml version="1.0" encoding="UTF-8"?>', "<records>"]

        for record in records:
            lines.append("  <record>")
            for key, value in record.to_dict().items():
                lines.append(f"    <{key}>{value}</{key}>")
            lines.append("  </record>")

        lines.append("</records>")

        with open(file_path, "w") as file:
            file.write("\n".join(lines))