
class User():
    def __init__(self, email, f_name, s_name, share_path, hashed_password) -> None:
        self.email = email
        self.f_name = f_name
        self.s_name = s_name
        self.share_path = share_path
        self.hashed_password = hashed_password
    
    def __repr__(self) -> str:
        return f"{self.email}: {self.f_name} {self.s_name}. Share: {self.share_path}.\n{self.hashed_password}"
