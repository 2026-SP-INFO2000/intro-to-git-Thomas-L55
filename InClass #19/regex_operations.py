import re
import pandas as pd

#1a
s1 = "The codes we use are 1Ff1 and 1Ff5"
s2 = "We sometimes use only 1Ff0"
pattern = r"1Ff0"
print("s1 contains 1Ff0:", bool(re.search(pattern, s1)))
print("s2 contains 1Ff0:", bool(re.search(pattern, s2)))

#1b
def find_digits(text):
    return re.findall(r"\d", text)
print(find_digits("Order 45 items on 12/09"))

#1c
def replace_nine(text):
    return re.sub(r"9", "nine", text)
print(replace_nine("I have 9 apples and 99 oranges"))

#1d
def get_username(email):
    match = re.match(r"([^@]+)", email)
    return match.group(1) if match else None
print(get_username("jack@protonmail.com"))

#1e
def four_letter_words(text):
    return re.findall(r"\b\w{4}\b", text)
text = """Download the data into your own tools and systems
to analyze the virus’s spread or decline, investigate COVID-related deaths, study the
effects of different vaccines, and more in 20,000-plus locations worldwide."""
print(four_letter_words(text))

#2a
df = pd.read_csv("report.csv")
df.columns = df.columns.str.replace(r"\W", "", regex=True)
print(df.head())
print(df.columns)

#2b
n_countries = df[df["Countryregion"].str.match(r"^N")]
print(n_countries["Countryregion"])
print(len(n_countries))

#2c
df["country code"] = df["Countryregion"].str[:3]
print(df[["Countryregion", "country code"]].head())

#2d
a_countries = df[df["Countryregion"].str.match(r"^A")]
print(a_countries)