a =('she','sells','sea','shells','by','the','sea','shore')
b="selfish shellfish"
c= [1,1,2,3,5,6,13]

def test_list(our_list):
  if (len (our_list) > 2) and (our_list [0] == our_list [-1]):
    return (True)
  else:
    return (False)



def list_match(list_one,list_two):
  newlist = []
  if list_one[0] == list_two [0]:
    newlist.append (list_one [0]) 
  if list_one[1] == list_two [1]:
    newlist.append (list_one [1])
  if list_one[2] == list_two [2]:
      newlist.append (list_one [2])

  return newlist
