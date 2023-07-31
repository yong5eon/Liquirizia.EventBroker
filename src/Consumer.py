# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'Consumer'
)


class Consumer(ABC):
	"""Consumer Interface of Event Broker"""

	@abstractmethod
	def qos(self, count: int):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))

	@abstractmethod
	def consume(self, queue: str):
		raise NotImplementedError('{} must be implemented consume'.format(self.__class__.__name__))

	@abstractmethod
	def run(self, interval: int = None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))

	@abstractmethod
	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))
