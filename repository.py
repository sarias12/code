import abc
import model
from typing import List


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlRepository(AbstractRepository):
    def __init__(self, session):
        breakpoint()
        self.session = session

    def add(self, batch):
        self.session.add(batch)
        
    def get(self, reference) -> model.Batch:
        return self.session.query(model.Batch).filter_by(reference=reference).one()

