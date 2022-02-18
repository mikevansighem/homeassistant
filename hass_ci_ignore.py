# A basic script to remove any part of the configuration that is described in "hassci"

#Open the file
with open(r'configuration.yaml', 'r') as file:
    data = file.read()

    # Open ignore file
    with open('.hass_ci') as ignore_file:

        # Open ignore file and replace matches line by line
        for search_text in ignore_file:
            data = data.replace(search_text, "#REDACTED")

# Write to file
with open(r'configuration.yaml', 'w') as file:
    file.write(data)

print("configuration.yaml has been redacted.")
