import os

from paramiko.config import SSHConfig
from pygerrit.rest import GerritReview, GerritRestAPI
from pygerrit.rest.auth import HTTPBasicAuthFromNetrc

class GerritServer:

   def __init__(self, gerrit_host_alias):

      ssh_config = SSHConfig()
      user_ssh_config_file = os.path.expanduser("~/.ssh/config")
      if os.path.exists(user_ssh_config_file):
         with open(user_ssh_config_file) as f:
            ssh_config.parse(f)

      gerrit_host_name = ssh_config.lookup(gerrit_host_alias).get("hostname")

      auth = HTTPBasicAuthFromNetrc("https://{}/".format(gerrit_host_alias))

      self.gerrit_api_client = GerritRestAPI("https://{}/".format(gerrit_host_name), auth)

   def set_score_labels(self, change_id, code_review_score, verified_score):
      labels = {}
      labels['Code-Review'] = code_review_score
      labels['Verified']    = verified_score

      review = GerritReview()
      review.add_labels(labels)
      self.gerrit_api_client.review(change_id, "current", review)
