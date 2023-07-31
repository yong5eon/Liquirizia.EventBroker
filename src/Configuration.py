# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'Configuration'
)


class Configuration(ABC):
	"""Configuration Interface for Event Broker"""

	@abstractmethod
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
