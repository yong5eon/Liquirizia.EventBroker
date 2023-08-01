# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'Queue'
)


class Queue(ABC):
	"""Queue Interface for Event Broker"""

	@abstractmethod
	def declare(self, queue, **kwargs):
		raise NotImplementedError('{} must be implemented declare'.format(self.__class__.__name__))

	@abstractmethod
	def bind(self, topic, event):
		raise NotImplementedError('{} must be implemented bind'.format(self.__class__.__name__))

	@abstractmethod
	def send(
		self,
		event,
		body=None,
		format=None,
		charset=None,
		headers=None,
		priority=None,
		expiration=None,
		timestamp=None,
		persistent=True,
		id=None,
	):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))

	@abstractmethod
	def qos(self, count: int):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))

	@abstractmethod
	def receive(self, timeout: int = None):
		raise NotImplementedError('{} must be implemented recv'.format(self.__class__.__name__))

	@abstractmethod
	def unbind(self, topic, event):
		raise NotImplementedError('{} must be implemented unbind'.format(self.__class__.__name__))

	@abstractmethod
	def remove(self):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
