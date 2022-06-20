from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def create_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_client(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_document(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_client(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_rm(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_document(self, *args, **kwargs):
        pass

    # @abstractmethod
    # def get_requests(self, *args, **kwargs):
    #     pass

    @abstractmethod
    def get_clients(self, *args, **kwargs):
        pass

    # @abstractmethod
    # def get_rms(self, *args, **kwargs):
    #     pass
