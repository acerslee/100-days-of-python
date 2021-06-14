auction_track = {}
auction_event = True

while auction_event == True:
  auctioner_name = input("What is your name?: ").lower()
  auctioner_bid = int(input("How much will you bid?: "))
  auction_track[auctioner_name] = auctioner_bid

  ask = input("Will there be another bidder?: ").lower()
  if ask == "no":
    for auctioner in auction_track:
      highest_bidder = max(auction_track, key = lambda k: auction_track[k])
    print (f"The item goes to {highest_bidder}")
    auction_event = False