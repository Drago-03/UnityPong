import UnityEngine
import UnityEngine.UI

class GameControl(UnityEngine.MonoBehaviour):
    def Start(self):
        self.starter = self.GetComponent(CountDown)
        self.scoreTextLeft = UnityEngine.UI.Text()
        self.scoreTextRight = UnityEngine.UI.Text()
        self.scoreLeft = 0
        self.scoreRight = 0
        self.ball = UnityEngine.GameObject()
        self.ballControl = self.ball.GetComponent(BallScript)
        self.started = False
        self.startingPosition = UnityEngine.Vector3()

    def Update(self):
        if self.started:
            return
        
        if UnityEngine.Input.GetKey(UnityEngine.KeyCode.Space):
            self.started = True
            self.starter.StartCountdown()

    def StartGame(self):
        self.ballControl.Go()

    def ScoreGoalLeft(self):
        self.scoreRight += 1
        self.UpdateUI()
        self.ResetBall()

    def ScoreGoalRight(self):
        self.scoreLeft += 1
        self.UpdateUI()
        self.ResetBall()

    def UpdateUI(self):
        self.scoreTextLeft.text = str(self.scoreLeft)
        self.scoreTextRight.text = str(self.scoreRight)

    def ResetBall(self):
        self.ballControl.Stop()
        self.ball.transform.position = self.startingPosition
        self.starter.StartCountdown()
        self.ball.SetActive(True)
