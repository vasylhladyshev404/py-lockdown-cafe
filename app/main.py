import datetime
from typing import Dict, Any, List


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError

        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"

