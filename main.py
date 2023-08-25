from robotics import Robot

SCIENTISTS = []
#"Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"

robot = Robot("George Saade")

def introduce_yourself():
    robot.say_hello()

def ask_for_names():
    while True:
        try:
            name = input("Enter a scientist's name (or 'c' to continue) : ")
            if name.lower() == 'c' and not SCIENTISTS:
                print("No new names were added..")
                continue
            if name.lower() == 'c':
                break
            if name.strip(): 
                SCIENTISTS.append(name)
        except ValueError:
            print("Invalid input. Please try again.")
        except Exception as e:
            error_message = str(e).split('\n')[0]
            print(f"Error: {error_message}")
            

def search_wikipedia():
    try:
        robot.open_webpage("https://en.wikipedia.org")
        for person in SCIENTISTS:
            print("Scientist : " + person)
            robot.submit_wiki_search(person)
            robot.get_scientist_age()
            robot.get_wiki_first_paragraph()

    except Exception as e:
        error_message = str(e).split('\n')[0]
        print(f"Error: {error_message}")

    finally:
        input("Press Enter to close the browser...")
        robot.close_all_browsers()


def prompt_save_data():
    try:
        save_option = input("Do you want to save the text to a file? (y/n): ")
        if save_option.lower() == "y":
            robot.save_text_to_file()
        else:
            print("Text not saved to a file.")

    except Exception as e:
        error_message = str(e).split('\n')[0]
        print(f"Error: {error_message}")


def say_goodbye():
    robot.say_goodbye()


def main():
    introduce_yourself()
    ask_for_names()
    search_wikipedia()
    prompt_save_data()
    say_goodbye()


if __name__ == "__main__":
    main()
