def list_defendants(users, parties, opposing, label):
  if label == "defendant" or label == "respondent":
    return users
  else:
    if opposing == True:
      return parties
    else:
      return ""