using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CountDown : MonoBehaviour
{
    private GameControl gameControl;
    private Animator animator;
    // Start is called before the first frame update
    void Start()
    {
        gameControl = FindObjectOfType<GameControl>();
        animator = GetComponent<Animator>();
    }

    public void StartCountdown()
    {
        animator.SetTrigger("StartCountdown");
    }

    public void StartGame()
    {
        gameControl.StartGame();
    }
}
