using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameControl : MonoBehaviour
{
    public CountDown starter;
        
    public Text scoreTextLeft;
    public Text scoreTextRight;
    private int scoreLeft = 0;
    private int scoreRight = 0;
    public GameObject ball;
    public BallScript ballControl;
    public bool started = false;
    public Vector3 startingPosition;
    // Start is called before the first frame update
    void Start()
    {
        
        
        this.startingPosition = this.ball.transform.position;

    }

    // Update is called once per frame
    void Update()
    {
        if ( this.started )
         return;

      
        if (Input.GetKey(KeyCode.Space))
        {
            this.started = true;
            this.starter.StartCountdown();
        }

    }


    public void StartGame()
    {
        this.ballControl.Go();
    }
    public void ScoreGoalLeft()
    {
        this.scoreRight += 1;
        UpdateUI();
        ResetBall();
    }
    public void ScoreGoalRight()
    {
        this.scoreLeft += 1;
        UpdateUI();
        ResetBall();
    }
    private void UpdateUI()
    {
        this.scoreTextLeft.text = this.scoreLeft.ToString();
        this.scoreTextRight.text = this.scoreRight.ToString();
    }

    private void ResetBall()
    {
        this.ballControl.Stop();
        this.ball.transform.position = this.startingPosition;
        this.starter.StartCountdown();
       
        
        this.ball.SetActive(true);
    }
   

}
