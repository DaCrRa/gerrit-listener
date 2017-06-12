import os

from paramiko.config import SSHConfig
from pygerrit.rest import GerritReview, GerritRestAPI
from pygerrit.rest.auth import HTTPBasicAuthFromNetrc

from ActionForGerritEvent import ActionForGerritEvent

class ScoreLabelSetter:

   def __init__(self, gerrit_api_client, code_review_label, verified_label):
      self.gerrit_api_client     = gerrit_api_client
      self.labels = {}
      self.labels['Code-Review'] = code_review_label
      self.labels['Verified']    = verified_label

   def set_score_labels(self, change_id):
      review = GerritReview()
      review.add_labels(self.labels)
      self.gerrit_api_client.review(change_id, "current", review)


class SetScoreLabels(ActionForGerritEvent):

   def __init__(self, gerrit_host_alias, code_review_label, verified_label):

      ssh_config = SSHConfig()
      user_ssh_config_file = os.path.expanduser("~/.ssh/config")
      if os.path.exists(user_ssh_config_file):
         with open(user_ssh_config_file) as f:
            ssh_config.parse(f)

      gerrit_host_name = ssh_config.lookup(gerrit_host_alias).get("hostname")

      auth = HTTPBasicAuthFromNetrc("https://{}/".format(gerrit_host_alias))
      rest_client = GerritRestAPI("https://{}/".format(gerrit_host_name), auth)

      self.score_label_setter = ScoreLabelSetter(rest_client, code_review_label, verified_label)


   def execute_for_event(self, event):
      self.score_label_setter.set_score_labels(event.change.change_id)

