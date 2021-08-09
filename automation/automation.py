import shutil
import re


def get_data(location):
    with open(location, "r") as file:
        content = file.read()
        return content


def pull_phone_info(data):
    phone_pattern = r"[0-9-+x.()]{7,}"
    phone_numbers = []

    numbers = re.findall(phone_pattern, data)
    for number in numbers:
        number = number.replace(".", "").replace("-", "").replace("(", "").replace(")", "")
        if len(number) == 10:
            number = number[:3] + "-" + number[3:6] + "-" + number[6:]
        phone_numbers.append(number)

    phone_numbers = list(set(phone_numbers))
    phone_numbers.sort()
    return phone_numbers


def pull_email_info(data):
    email_pattern = r"\S+@\S+"
    emails = re.findall(email_pattern, data)
    emails = list(set(emails))
    emails.sort()
    return emails


def write_to_file(data, path):
    with open(path, "w") as new_file:
        for item in data:
            new_file.write(item + "\n")


def main():
    data = get_data("assets/potential-contacts.txt")
    phone_numbers = pull_phone_info(data)
    emails = pull_email_info(data)
    write_to_file(emails, "assets/emails.txt")
    write_to_file(phone_numbers, "assets/phone_numbers.txt")


if __name__ == "__main__":
    main()
