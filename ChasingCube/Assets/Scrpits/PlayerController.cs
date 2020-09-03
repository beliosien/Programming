using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Control the player
public class PlayerController : MonoBehaviour
{
    [HideInInspector]
    PlayerDirection playerDirection = PlayerDirection.STAY;

    [HideInInspector]
    public float step_length = 0.2f;

    List<Vector3> deltaPosition;

    [HideInInspector]
    public float mouvement_frequency = 0.1f;
    private float counter;
    private bool move;



    Rigidbody playerRigidbody;

    void Awake() 
    {
        playerRigidbody = GetComponent<Rigidbody>();
        move = false;

        deltaPosition = new List<Vector3>()
        {
           new Vector3 (-step_length, 0f),   // right
           new Vector3 (step_length, 0f),  // left
           new Vector3 (0f, step_length), // up
           new Vector3 (0f, -step_length) // down
        };
    }

    // Update is called once per frame
    void Update()
    {
        CheckMouvementFrequency();
    }

    void FixedUpdate() {
        if (move)
        {
            move = false;
            Move();
        }
    }

    // move the player 
    public void Move()
    {
        if (playerDirection != PlayerDirection.STAY)
        {
            Vector3 dPosition = deltaPosition[(int)playerDirection];
            playerRigidbody.position = playerRigidbody.position + dPosition; 
        } 
    }

    void CheckMouvementFrequency()
    {
        counter += Time.deltaTime;
        if (counter >= mouvement_frequency)
        {
            counter = 0.0f;
            move = true;
        }
    }

    // set the direction of the player
    public void SetDirection(PlayerDirection direction)
    {
        playerDirection = direction;
        counter = 0;
        move = false;
        Move();
    }

}
