def is_valid_user(user) -> bool:
    return bool(user.name) and bool(user.email)

def save_user_to_database(user) -> None:
    db.insert("Users", user)

def backup_user_to_file(user) -> None:
    file_path = f"/backup/users/{user.id}.txt"
    write_to_file(file_path, user)

def save_user(user) -> None:
    if not is_valid_user(user):
        print("Invalid user data")
        return

    save_user_to_database(user)
    backup_user_to_file(user)
