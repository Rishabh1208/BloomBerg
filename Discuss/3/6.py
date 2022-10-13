
# Task was very easy. We have tickers of stocks and many prices.
# We need to add them and then be able to take N oldest by ticker and N params.
# I think I choose right base structure Dictionary<string, XXX>
# To store stock prices per ticker name.
# But then I started to do something wrong. (below will be about XXX)
# I was very nervous becuase of interview and told that we need to use doubly linked list to store 
# prices
# to be able to take oldest N prices with lower complexity. Inteviewer tried to give me advices. 
# But i was in "flow" already:) 
# and did not listen him:(
# Just interview finished I realized that I could use simple List of decimal to store prices i.e. 
# Dictionary<string, List> 
# instead of Dictionary<string, DoublePriceLinkedList>>

# So, the lesson is, stay calm during interview, no difference where are you interviewed, is it 
# small company or giant like Bloomberg.
# Did not get a response, but probably I will be rejected. Interviewer did not look satisfied
