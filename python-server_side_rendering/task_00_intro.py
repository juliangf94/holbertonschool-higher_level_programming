import logging
import os

def generate_invitations(template, attendees):
    # Input validation
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return
    # Verify they are not empty
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    # Process every attendees
    for index, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", str(attendee.get("name") or "N/A"))
        output = output.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        output = output.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        output = output.replace("{event_location}", str(attendee.get("event_location") or "N/A"))
        
        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            logging.warning("File {} already exists, overwriting.".format(filename))

        try:
            with open(filename, 'w') as f:
                f.write(output)
        except Exception as e:
            logging.error("Failed to write file {}: {}".format(filename, e))
