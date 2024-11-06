import xml.etree.ElementTree as ET
import argparse

def convert_to_xml(input_file_path):
    """
    Converts line-based fileformat to xml-format. See README for more info.
    The scripts expects the lines to be filled in correctly.

    Args: /path/to/file

    Output: /output/file.xml
    """
    try:
        # Read the input file contents
        with open(input_file_path, 'r') as f:
            lines = f.readlines()

        # Create the root XML element
        root = ET.Element("persons")

        # Generate the XML structure
        for line in lines:
            lines_list = line.strip().split("|")
            if lines_list[0]=="P":
                person = ET.SubElement(root, "person")
                firstname = ET.SubElement(person, "firstname")
                firstname.text = lines_list[1]
                lastname = ET.SubElement(person, "lastname")
                lastname.text = lines_list[2]
                # Required for linking following A or T correctly.
                prev_person = person
            elif lines_list[0]=="F":
                family = ET.SubElement(person, "family")
                name = ET.SubElement(family, "name")
                name.text = lines_list[1]
                born = ET.SubElement(family, "born")
                born.text = lines_list[2]
                if len(lines_list)==4:
                    address = ET.SubElement(family, "address")
                    address.text = lines_list[3]  
                # Required for linking following A or T correctly.  
                prev_person = family
            elif lines_list[0]=="T":
                phone = ET.SubElement(prev_person, "phone")
                mobile = ET.SubElement(phone, "mobile")
                mobile.text = lines_list[1]
                landline = ET.SubElement(phone, "landline")
                landline.text = lines_list[2]  
            elif lines_list[0]=="A":
                address = ET.SubElement(prev_person, "address")
                street = ET.SubElement(address, "street")
                street.text = lines_list[1]
                city = ET.SubElement(address, "city")
                city.text = lines_list[2]
                if len(lines_list)==4:
                    postalcode = ET.SubElement(address, "postalcode")
                    postalcode.text = lines_list[3]
            else:
                print(f"Ignoring line: {line}")

        # Create an ElementTree object
        tree = ET.ElementTree(root)

        # Write the output XML file
        
        output_file_name = "output/" + input_file_path.split("/")[-1].strip(".") + ".xml"
        tree.write(output_file_name)

        print(f"XML file generated: {output_file_name}")

    except FileNotFoundError:
        print(f"Input file not found: {input_file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}.")

def main():
    parser = argparse.ArgumentParser(description="A simple command line based XML-converter")
    parser.add_argument("-i", "--input_file", help="The input file path.")

    args = parser.parse_args() 

    # Print help if no input argument.
    if args.input_file == None:
        parser.print_help()  
    else:
        input_file_name = args.input_file
        convert_to_xml(input_file_name)


if __name__ == "__main__":
    main()