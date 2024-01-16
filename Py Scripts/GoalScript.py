import UnityEngine
import UnityEngine.Events

class GoalScript(UnityEngine.MonoBehaviour):
    ballTag = "Ball"
    onTriggerEnter = UnityEngine.Events.UnityEvent()

    def OnTriggerEnter(self, other):
        if other.CompareTag(self.ballTag):
            print("GOOAAALLLL")
            other.gameObject.SetActive(False)
            self.onTriggerEnter.Invoke()
