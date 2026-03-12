from project.user import User
from project.library import Library
class Registration:
    def add_user(self, user: User, library: Library):
        for curr_user in library.user_records:
            if curr_user.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None
    
    def remove_user(self, user: User, library: Library):
        for i, curr_user in enumerate(library.user_records):
            if curr_user.user_id == user.user_id:
                library.user_records.pop(i)
                if user.username in library.rented_books:
                    del library.rented_books[user.username]
                return None
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    if user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(user.username)
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for userid: {user_id}"
                return "Please check again the provided username - it should be different than the username used so far!"
            return f"There is no user with id = {user_id}!"
