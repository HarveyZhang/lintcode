class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.cluster = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.cluster[server_id] = 1


    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id in self.cluster:
            del self.cluster[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        import random
        server_ids = self.cluster.keys()
        return random.sample(server_ids, 1)[0] if len(server_ids) > 0 else None
