# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod, abstractproperty

__all__ = (
	'Response'
)


class Response(ABC):
	"""Response Interface of Event Broker"""

	@abstractmethod
	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	@abstractmethod
	def header(self, key):
		raise NotImplementedError('{} must be implemented header'.format(self.__class__.__name__))

	@abstractproperty
	def id(self):
		raise NotImplementedError('{} must be implemented id'.format(self.__class__.__name__))

	@abstractproperty
	def type(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@abstractproperty
	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
