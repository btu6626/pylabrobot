from .coordinate import Coordinate
from .resource import Resource


class Well(Resource):
  """ Base class for Well resources.

  Note that in regular use these will be automatically generated by the
  :class:`pylabrobot.liquid_handling.resources.abstract.Plate` class.
  """

  def __init__(self, name, location: Coordinate = Coordinate(None, None, None)):
    # TODO: max_volume: float,
    super().__init__(name, size_x=9, size_y=9, size_z=9, location=location, category="well")
    # self.max_volume = max_volume