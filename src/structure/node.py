from math import sqrt

class network_node:

    #List with 'connection-tuple'. First element of the tuple is a network_node object
    #the second object is the euclidian distance of the object to the object in the tuple

    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value
        self.connections = []

    def get_position(self):
        return self.x, self.y

    def set_position(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def add_connection(self, node, distance):
        self.connections.append((node, distance))
        node.connections.append((self, distance))

    def get_connections(self):
        return self.connections


    def is_connected_to(self, node):
        for connection in self.connections:
            if connection[0] == node:
                return True
        return False

    def distance(self, node):
        dx = self.x - node.x
        dy = self.y - node.y

        return sqrt(dx**2 + dy**2)
    
    
