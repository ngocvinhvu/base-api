from backend.api.factory.base_logics import BaseLogic


class UserBL(BaseLogic):

    def create(self, email):
        result = dict(
            id='id-created',
            email=email,
            status_code=201
        )
        return result
