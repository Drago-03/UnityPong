import UnityEngine

class PlayerControl(UnityEngine.MonoBehaviour):
    speed = 0.0
    up = None
    down = None
    rb = None
    isPlayer = True
    ball = None
    offset = 0.2

    def Start(self):
        self.rb = self.GetComponent(UnityEngine.Rigidbody)

    def Update(self):
        if self.isPlayer:
            self.MoveByPlayer()
        else:
            self.MoveByComputer()

    def MoveByPlayer(self):
        pressedUp = UnityEngine.Input.GetKey(self.up)
        pressedDown = UnityEngine.Input.GetKey(self.down)

        if pressedUp:
            self.rb.velocity = UnityEngine.Vector3.forward * self.speed

        if pressedDown:
            self.rb.velocity = UnityEngine.Vector3.back * self.speed

        if not pressedUp and not pressedDown:
            self.rb.velocity = UnityEngine.Vector3.zero

    def MoveByComputer(self):
        if self.ball.position.z > self.transform.position.z + self.offset:
            self.rb.velocity = UnityEngine.Vector3.forward * self.speed
        elif self.ball.position.z < self.transform.position.z - self.offset:
            self.rb.velocity = UnityEngine.Vector3.back * self.speed
        else:
            self.rb.velocity = UnityEngine.Vector3.zero
