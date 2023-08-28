
class User():
    def __init__(self, email, f_name, s_name, share_path, hashed_password) -> None:
        self.email = email
        self.f_name = f_name
        self.s_name = s_name
        self.share_path = share_path
        self.hashed_password = hashed_password
    
    def __repr__(self) -> str:
        return f"{self.email}: {self.f_name} {self.s_name}. Share: {self.share_path}.\n{self.hashed_password}"

class Survey():
        def __init__(self, id, name, start_date, end_date, owner_email) -> None:
            self.id = id
            self.name = name
            self.start_date = start_date
            self.end_date = end_date
            self.owner_email = owner_email
        
        def __repr__(self) -> str:
            return f"Survey number {self.id}: {self.name} from {self.start_date} to {self.end_date}.\nOwned by {self.owner_email}"
        
