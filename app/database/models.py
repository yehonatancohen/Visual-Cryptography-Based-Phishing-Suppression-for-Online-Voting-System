from PIL import Image
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email, f_name, s_name, share_path,
                hashed_password, hashed_server_code) -> None:
        self.id = email
        self.email = email
        self.f_name = f_name
        self.s_name = s_name
        self.share_path = share_path
        self.hashed_password = hashed_password
        self.hashed_server_code = hashed_server_code

    def get_id(self):
        return str(self.id)
    
    def __repr__(self) -> str:
        return f"{self.email}: {self.f_name} {self.s_name}. \
            Share: {self.share_path}.\nPass: {self.hashed_password}\nCode: {self.hashed_server_code}\n"

class Survey:
    def __init__(self, id, name, start_date, end_date, owner_email) -> None:
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.owner_email = owner_email
    
    def __repr__(self) -> str:
        return f"Survey number {self.id}: {self.name} from {self.start_date} to {self.end_date}.\nOwned by {self.owner_email}\n"
    
    def is_active(self):
        from datetime import datetime
        startDateObj = datetime.strptime(self.start_date, '%Y-%m-%d %H:%M')
        endDateObj = datetime.strptime(self.end_date, '%Y-%m-%d %H:%M')
        is_active = (datetime.now() >= startDateObj) and (datetime.now() <= endDateObj)
        return is_active
    
    def has_ended(self):
        from datetime import datetime
        endDateObj = datetime.strptime(self.end_date, '%Y-%m-%d %H:%M')
        has_ended = (datetime.now() <= endDateObj)
        return has_ended
    

        
class Voter:
    def __init__(self, survey_id, email, has_voted) -> None:
        self.survey_id = survey_id
        self.email = email
        self.has_voted = has_voted

    def __repr__(self) -> str:
        return f"voter {self.email} from survey {self.survey_id}.\nVoted = {self.has_voted}\n"
    
class Candidate:
    def __init__(self, cand_id, survey_id, cand_name, cand_desc, image_path: str, votes) -> None:
        self.cand_id = cand_id
        self.survey_id = survey_id
        self.cand_name = cand_name
        self.cand_desc = cand_desc
        if image_path == "":
            image = None
        else:
            image = Image.open(image_path)
        self.image = image
        self.votes = votes

    def __init__(self, cand_id, survey_id, cand_name, cand_desc, image: Image.Image, votes) -> None:
        self.cand_id = cand_id
        self.survey_id = survey_id
        self.cand_name = cand_name
        self.cand_desc = cand_desc
        self.image = image
        self.votes = votes

    def __repr__(self) -> str:
        return f"Candidate {self.cand_name}-{self.cand_id} from survey {self.survey_id}.\n{self.cand_desc}\n{self.image}\nHas {self.votes} votes."