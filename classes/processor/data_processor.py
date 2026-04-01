import os
import random
from datetime import datetime, timedelta
from models.record import Record
from utils.logger import Logger
from exporters.json_exporter import JsonExporter
from exporters.xml_exporter import XmlExporter


class DataProcessor:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.logger = Logger("processing.log")

        self.records = []
        self.records_processed = 0
        self.error_count = 0
        self.error_messages = []

        self.validate_data = True
        self.transform_data = True
        self.date_format = "%Y-%m-%d"
        self.batch_size = 100
        self.statistics = {}

        self._initialize_file()

    def process(self):
        self.logger.log("Processing started.")

        try:
            self._read_file()
            if self.validate_data:
                self._validate_records()
            if self.transform_data:
                self._transform_records()

            self._calculate_statistics()
            self._write_output()
            self.logger.save()

        except Exception as exc:
            self.error_count += 1
            self.error_messages.append(str(exc))
            self.logger.log(f"Fatal error: {exc}")

    def _initialize_file(self):
        if not os.path.exists(self.input_file):
            open(self.input_file, "w").close()

    def _read_file(self):
        with open(self.input_file, "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                try:
                    value = float(parts[2])
                    date = parts[3] if len(parts) >= 4 else None
                    record = Record(parts[0], parts[1], value, date)
                    self.records.append(record)
                except ValueError:
                    self.error_count += 1
            else:
                self.error_count += 1

    def _validate_records(self):
        valid_records = []

        for record in self.records:
            if record.id and record.name and isinstance(record.value, float):
                valid_records.append(record)
            else:
                self.error_count += 1
                self.error_messages.append(f"Invalid record {record.id}")

        self.records = valid_records

    def _transform_records(self):
        for record in self.records:
            record.transform(self.date_format)

    def _calculate_statistics(self):
        total_value = sum(record.value for record in self.records)

        self.statistics["total_records"] = len(self.records)
        self.statistics["error_count"] = self.error_count
        self.statistics["total_value"] = int(total_value)
        self.statistics["average_value"] = (
            int(total_value / len(self.records)) if self.records else 0
        )

    def _write_output(self):
        lines = ["ID,NAME,VALUE,DATE,DOUBLED_VALUE,SQUARED_VALUE"]

        for record in self.records:
            r = record.to_dict()
            line = ",".join(str(r.get(field, "")) for field in r)
            lines.append(line)

        with open(self.output_file, "w") as file:
            file.write("\n".join(lines))

        self.records_processed = len(self.records)

    def export_json(self, path: str):
        JsonExporter.export(self.records, path)

    def export_xml(self, path: str):
        XmlExporter.export(self.records, path)

    def filter_by_value(self, min_value: float):
        return [record for record in self.records if record.value >= min_value]

    @staticmethod
    def generate_sample_data(file_path: str, count: int):
        lines = []

        for i in range(1, count + 1):
            record_id = f"ID{i:04d}"
            name = f"Item{i}"
            value = random.randint(10, 1000)
            date = datetime.now() - timedelta(days=random.randint(0, 365))
            lines.append(
                f"{record_id},{name},{value},{date.strftime('%Y-%m-%d')}"
            )

        with open(file_path, "w") as file:
            file.write("\n".join(lines))