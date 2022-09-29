from git import Repo
your_path = str(input("Indiquez le chemin de destination\n"))
Repo.clone_from("https://github.com/KeligMartin/4-SRC.git", your_path)