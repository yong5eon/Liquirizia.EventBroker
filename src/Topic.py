# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'Topic'
)


class Topic(ABC):
	"""Topic Interface for Event Broker"""

	@abstractmethod
	def declare(self, topic, **kwargs):
		raise NotImplementedError('{} must be implemented declare'.format(self.__class__.__name__))

	@abstractmethod
	def bind(self, topic, event):
		raise NotImplementedError('{} must be implemented bind'.format(self.__class__.__name__))

	@abstractmethod
	def publish(
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
		raise NotImplementedError('{} must be implemented publish'.format(self.__class__.__name__))

	@abstractmethod
	def unbind(self, topic, event):
		raise NotImplementedError('{} must be implemented unbind'.format(self.__class__.__name__))

	@abstractmethod
	def remove(self):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
