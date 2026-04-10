def format_results(results):
    formatted_output = []

    for idx, result in enumerate(results, start=1):
        formatted_output.append(
            f"""
Result {idx}:
  Address   : {result['formatted_address']}
  Latitude  : {result['latitude']}
  Longitude : {result['longitude']}
            """.strip()
        )

    return "\n\n".join(formatted_output)