from datetime import datetime
from RPA.Browser.Selenium import Selenium
import re

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name
        self.final_summary = ''

    def say_hello(self):
        print("Hello, my name is " + self.name + "\n")

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def save_text_to_file(self):
        try:
            filename = input("Enter the file name: ")
            if not filename.endswith(".txt"):
                filename += ".txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(self.final_summary)
                print(f"Text saved to '{filename}' successfully!")

        except IOError:
            print(f"An error occurred while saving the text to '{filename}'.")
        except UnicodeEncodeError:
            print(f"UnicodeEncodeError: Unable to encode the text using the specified encoding. Please try a different file name.")


    def close_all_browsers(self):
        print("Closing Browser..")
        br.close_all_browsers()


    def open_webpage(self, webpage):
        try:
            br.open_available_browser(webpage)
            
        except Exception as e:
            error_message = str(e).split('\n')[0]
            print(f"(Error) Could not open browser: {error_message}")

    def submit_wiki_search(self, scientist):
        try:
            br.input_text("name=search", scientist)
            br.wait_and_click_button("//html/body/div[1]/header/div[2]/div/div/div/form/div/button")
            self.final_summary += scientist + "\n"

        except Exception as e:
            error_message = str(e).split('\n')[0]
            print(f"(Error) Could not submit wiki search: {error_message}")


    def get_wiki_first_paragraph(self):
        try:
            first_paragraph_element = br.get_webelement(f"//div[@id='mw-content-text']//p[ string-length(normalize-space()) > 0]")
            summary_text = br.get_text(first_paragraph_element)
            self.final_summary += "\n" + summary_text + "\n"
            print(summary_text + "\n")

        except Exception as e:
            error_message = str(e).split('\n')[0]
            print(f"(Error) Could not get Summary paragraph:  {error_message}")


    def get_scientist_age(self):
        try:
            Born = br.execute_javascript("return document.getElementsByClassName('bday')[0].textContent")
            Birth_date = datetime.strptime(Born, "%Y-%m-%d")

            Died_info_box = br.get_text("//th[contains(text(), 'Died')]/following-sibling::td")
            Date_string = re.search(r"\b(\d{1,2}\s\w+\s\d{4})\b", Died_info_box).group(1)
            # Convert the extracted date to the "1955-04-18" format
            Death_date = datetime.strptime(Date_string, "%d %B %Y")
            Died = Death_date.strftime("%Y-%m-%d")

            Age = Death_date.year - Birth_date.year
            self.final_summary += f"Born  : {Born}\nDied  : {Died}\nAge   : {Age}"
            print(f"Born  : {Born}\nDied  : {Died}\nAge   : {Age}")

        except Exception as e:
            error_message = str(e).split('\n')[0]
            print(f"(Error) Could not get scientist age:  {error_message}")
