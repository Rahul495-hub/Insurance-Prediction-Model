from pydantic import BaseModel, Field, validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated[Literal[
        'retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'
    ], Field(..., description='Occupation of the user')]

    @validator('city')
    def normalize_city(cls, v: str) -> str:
        return v.strip().title()

    # Computed fields moved outside the model
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    def lifestyle_risk(self) -> str:
        bmi_val = self.bmi()
        if self.smoker and bmi_val > 30:
            return "high"
        elif self.smoker or bmi_val > 27:
            return "medium"
        else:
            return "low"

    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
