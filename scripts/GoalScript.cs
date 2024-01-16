using UnityEngine;
using UnityEngine.Events;

public class GoalScript : MonoBehaviour
{
   
    public string ballTag = "Ball";
    
    public UnityEvent onTriggerEnter;
  


  
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag(ballTag))
        {
            Debug.Log("GOOAAALLLL");
            other.gameObject.SetActive(false);
            onTriggerEnter.Invoke();
            
        }
    }
}