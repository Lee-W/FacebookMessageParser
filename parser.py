import json

from bs4 import BeautifulSoup


def parse_single_message_file(filename):
    with open(filename) as message_file:
        soup = BeautifulSoup(message_file.read(), "html5lib")
        title_text = soup.find("title").text
        thread_soup = soup.find("div", class_="thread")
        return {"title": title_text, "thread": parse_thread(thread_soup)}


def parse_thread(thread_soup):
    message_header_soups = thread_soup.find_all("div", class_="message_header")
    content_soups = thread_soup.find_all("p")

    thread = list()
    for message_header_soup, content_soup in zip(message_header_soups, content_soups):
        message_header = parse_message_header(message_header_soup)
        content = content_soup.text

        thread.append({"message_header": message_header, "content": content})
    thread.reverse()
    return thread


def parse_message_header(message_header_soup):
    user = message_header_soup.find("span", class_="user").text
    message_time = message_header_soup.find("span", class_="meta").text.strip()

    return {"user": user, "message_time": message_time}


if __name__ == "__main__":
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input_file")
    arg_parser.add_argument("-o", "--output_file", default=None)
    args = arg_parser.parse_args()

    fb_messages = parse_single_message_file(args.input_file)

    output_filename = args.output_file or fb_messages.get("title") + ".json"
    with open(output_filename, "w") as export_file:
        export_file.write(json.dumps(fb_messages, indent=4, ensure_ascii=False))
