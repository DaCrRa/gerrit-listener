import unittest

from pygerrit.events import PatchsetCreatedEvent

from filters.GerritEventFilter import CompositeAndFilter
from filters.event_type_filters import PatchsetCreatedFilter
from filters.event_attributes_filters import ChangeOwnerFilter

class TestPatchsetCreatedOwnedByFilter(unittest.TestCase):

   def setUp(self):
      self.patchset_created_owned_by_filter = ( CompositeAndFilter()
                       .add_filter(PatchsetCreatedFilter())
                       .add_filter(ChangeOwnerFilter(["owner_of_interest"]))
                    )

   def test_givenPatchsetCreatedOwnedByOwnerOfInterest_whenFiltering_thenReturnsTrue(self):
      owner_of_interest = {}
      owner_of_interest["name"] = ""
      owner_of_interest["email"] = ""
      owner_of_interest["username"] = "owner_of_interest"

      event_data = {}
      event_data["change"] = { "owner":  owner_of_interest }
      event_data["patchSet"] = ""
      event_data["uploader"] = ""

      event = PatchsetCreatedEvent(event_data)

      self.assertTrue(self.patchset_created_owned_by_filter.filter_event(event))

   def test_givenPatchsetCreatedOwnedBySomeoneElseEvent_whenFiltering_thenReturnsFalse(self):
      someone_else = {}
      someone_else["name"] = ""
      someone_else["email"] = ""
      someone_else["username"] = "someone_else"

      event_data = {}
      event_data["change"] = { "owner": someone_else }
      event_data["patchSet"] = ""
      event_data["uploader"] = ""

      event = PatchsetCreatedEvent(event_data)

      self.assertFalse(self.patchset_created_owned_by_filter.filter_event(event))
