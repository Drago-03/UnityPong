import UnityEngine

class CountDown(UnityEngine.MonoBehaviour):
    def Start(self):
        self.gameControl = UnityEngine.Object.FindObjectOfType(GameControl)
        self.animator = self.GetComponent(UnityEngine.Animator)

    def StartCountdown(self):
        self.animator.SetTrigger("StartCountdown")

    def StartGame(self):
        self.gameControl.StartGame()
