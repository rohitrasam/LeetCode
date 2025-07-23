# https://leetcode.com/problems/design-twitter/

import heapq
from typing import Dict, List, Set, Tuple


class Twitter:

    def __init__(self):
       self.posts: Dict[int, Set[Tuple[int, int]]] = {}
       self.followers: Dict[int, Set[int]] = {}
       self.time: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.posts:
          self.posts[userId].add((self.time, tweetId))
        else:
           self.posts[userId] = {(self.time, tweetId)}
        
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        followers = self.followers.get(userId)
        posts: List[Tuple[int, int]] = [post for post in self.posts[userId]]
        recent: List[int] = [] 

        if followers:
            for follower in followers:
                if follower in self.posts:
                    for post in self.posts[follower]:
                        posts.append(post)
        
        if posts:
            recent = list(map(lambda p: p[1], heapq.nsmallest(10, posts)))
        
        return recent    
         

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
          self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
           self.followers[followerId].remove(followeeId) 


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))