import random
import math
import numpy as np

class BallScript:
    def __init__(self):
        self.speed = 0.0
        self.direction = np.array([0.0, 0.0, 0.0])
        self.rb = None
        self.minDirection = 0.5
        self.stopped = True
        self.sparksVFX = None

    def start(self):
        self.rb = Rigidbody()
    
    def update(self):
        pass

    def fixed_update(self):
        if self.stopped:
            return
        self.rb.position += self.direction * self.speed * Time.fixedDeltaTime

    def on_trigger_enter(self, other):
        hit = False
        if other.CompareTag("Wall"):
            self.direction[2] = -self.direction[2]
            hit = True

        if other.CompareTag("Racket"):
            newDirection = (self.transform.position - other.transform.position).normalized
            newDirection[0] = math.copysign(max(abs(newDirection[0]), self.minDirection), newDirection[0])
            newDirection[2] = math.copysign(max(abs(newDirection[2]), self.minDirection), newDirection[2])
            self.direction = newDirection
            hit = True

        if hit:
            sparks = Instantiate(self.sparksVFX, self.transform.position, self.transform.rotation)
            Destroy(sparks, 6.0)

    def choose_direction(self):
        signX = math.copysign(1, random.uniform(-1, 1))
        signZ = math.copysign(1, random.uniform(-1, 1))
        self.direction = np.array([0.5 * signX, 0.0, 0.5 * signZ])

    def stop(self):
        self.stopped = True

    def go(self):
        self.choose_direction()
        self.stopped = False
