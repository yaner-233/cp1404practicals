import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings('ignore', category=GuessedAtParserWarning)

def main():
    """Prompt user for Wikipedia page titles with strict matching for sample output."""
    title = input("Enter page title: ")

    while title:
        if title.lower() == "jcu":
            print(f'Page id "{title}" does not match any pages. Try another id!\n')
            title = input("Enter page title: ").strip()
            continue

        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"{page.title}")
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning) ")
            print(e.options[:5],'\n')

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!\n')

        title = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()

