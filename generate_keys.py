import pathlib
import pickle

import streamlit_authenticator as stauth

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["123456", "123456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = pathlib.Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
