# -*- coding: utf-8 -*-

from .Event import Event

from abc import ABC, abstractmethod

__all__ = (
	'Callback'
)


class Callback(ABC):
	"""Callback Interface of Event Broker"""

	@abstractmethod
	def __call__(self, event: Event):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))