from collections import OrderedDict

def create_html_with_vimeo_links(input_file, output_file):
    # Open the input file for reading with utf-8 encoding and read all content at once
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Create an OrderedDict to preserve order and remove duplicates
    links = list(OrderedDict.fromkeys(
        [line.strip().removeprefix('href=').strip('"') for line in content.split() if "https://vimeo.com/user98867147" in line]
    ))

    # Define a function to generate the lecture labels in the desired order (88a, 88b, 87a, 87b, etc.)
    def generate_lecture_labels(num_links):
        labels = []
        base_number = 88  # Start from 88
        suffixes = ['a', 'b', 'a', 'b']  # Suffix pattern for lecture numbers

        for i in range(num_links):
            if i % 4 == 0 and i > 0:
                base_number -= 1  # Decrease the base number after every 4 items
            labels.append(f"{base_number}{suffixes[i % 4]}")

        return labels

    # Generate the lecture labels based on the number of links
    lecture_labels = generate_lecture_labels(len(links))

    # Create the HTML structure
    html_content = "<html>\n<head>\n<title>Vimeo Links</title>\n</head>\n<body>\n"
    html_content += "<h1>List of Vimeo Links</h1>\n"
    html_content += "<ul>\n"

    # Add each unique link as a clickable hyperlink, with the corresponding lecture label
    for label, link in zip(lecture_labels, links):
        html_content += f"<li>{label}: <a href=\"{link}\">{link}</a></li>\n"

    html_content += "</ul>\n</body>\n</html>"

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(html_content)

# Define the input and output file paths
input_file = 'links.txt'  # Adjust this path if necessary
output_file = 'vimeo_links.html'

# Create an HTML file with the Vimeo links and numbered lectures
create_html_with_vimeo_links(input_file, output_file)

print(f"HTML file created with Vimeo links: {output_file}")
