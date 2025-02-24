from dataclasses import dataclass

@dataclass
class UserDTO:
    first_name: str
    last_name: str
    email: str
    phone: str
    default_address: str
    typology: str
