# -*- coding: utf-8 -*-

from .Callback import Callback

from abc import ABC, abstractmethod

__all__ = (
	'Connection'
)


class Connection(ABC):
	"""Connection Interface for Event Broker"""

	@abstractmethod
	def connect(self):
		raise NotImplemented('{} must be implemented connect'.format(self.__class__.__name__))

	@abstractmethod
	def topic(self, topic: str = None):
		raise NotImplemented('{} must be implemented topic'.format(self.__class__.__name__))

	@abstractmethod
	def queue(self, queue: str = None):
		raise NotImplemented('{} must be implemented queue'.format(self.__class__.__name__))

	@abstractmethod
	def consumer(self, callback: Callback, count: int = 1):
		raise NotImplemented('{} must be implemented consumer'.format(self.__class__.__name__))

	@abstractmethod
	def close(self):
		raise NotImplemented('{} must be implemented close'.format(self.__class__.__name__))
