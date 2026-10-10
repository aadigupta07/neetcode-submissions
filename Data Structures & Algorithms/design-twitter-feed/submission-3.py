class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time, tweetId])
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        # need to make combined heap of users tweets and all the heaps the tweets of users they follow
        heap = self.tweets[userId][-10:]
        for user in self.following[userId]:
            for tweet in self.tweets[user][-10:]:
                heap.append(tweet)
        
        heapq.heapify(heap)
        result = []
        count = 0
        while heap and count < 10:
            curr = heapq.heappop(heap)
            result.append(curr[1])
            count+=1
        
        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
