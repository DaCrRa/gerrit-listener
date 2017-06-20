from gerrit.server import GerritServer

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

   def __init__(self, gerrit_server, code_review_score, verified_score):
      self.gerrit_server = gerrit_server
      self.code_review_score = code_review_score
      self.verified_score = verified_score

   def execute_for_event(self, event):
      self.gerrit_server.set_score_labels(event.change.change_id, self.code_review_score, self.verified_score)
