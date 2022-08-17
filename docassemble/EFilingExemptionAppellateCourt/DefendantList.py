def list_defendants(users, other_parties, any_opposing, user_party_label):
  if user_party_label == "defendant" or user_party_label == "respondent":
    return users
  else:
    if any_opposing == True:
      return other_parties
    else:
      return ""