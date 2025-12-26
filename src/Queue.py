# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from typing import Iterable, Any

__all__ = (
	'Queue',
	'Stream',
	'Poppable',
	'Readable',
)


class Queue(metaclass=ABCMeta):
	"""Queue Interface for Event Broker"""
	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))
	

class Stream(metaclass=ABCMeta):
	"""Stream Interface for Event Broker"""
	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))


class Poppable(metaclass=ABCMeta):
	"""Poppable Interface for Queue of Event Broker"""
	@abstractmethod
	def pop(self, timeout: int = None) -> Any:
		raise NotImplementedError('{} must be implemented pop'.format(self.__class__.__name__))


class Readable(metaclass=ABCMeta):
	"""Readable Interface for Queue of Event Broker"""
	@abstractmethod
	def read(self, timeout: int = None) -> Iterable[Any]:
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))
