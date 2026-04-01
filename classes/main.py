from processor.data_processor import DataProcessor


if __name__ == "__main__":

    DataProcessor.generate_sample_data("input.csv", 50)

    processor = DataProcessor("input.csv", "output.csv")

    processor.validate_data = True
    processor.transform_data = True
    processor.date_format = "%m/%d/%Y"

    processor.process()

    processor.export_json("output.json")
    processor.export_xml("output.xml")

    filtered = processor.filter_by_value(100)

    print("Processing complete.")
    print(f"Records processed: {processor.records_processed}")
    print(f"Errors: {processor.error_count}")
    print(f"Filtered records: {len(filtered)}")