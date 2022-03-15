using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent (typeof(PlayerController))]
public class Player : LivingEntity
{
    public float moveSpeed;
    PlayerController playerController;

    float timeInBetweenSuperCalls = 2f;
    protected float superPowerDelay = 1f;
    protected float nextTimeSuperPowerCanBeCalled;


    // Start is called before the first frame update
    protected override void Start()
    {
        base.Start();
        playerController = GetComponent<PlayerController>();
    }

    // Update is called once per frame
    void Update()
    {
        Move();

        if (Time.time > nextTimeSuperPowerCanBeCalled){

            // create an event alerting superpower can be called
            
            if (Input.GetKeyDown(KeyCode.Space)){
                nextTimeSuperPowerCanBeCalled = Time.time + timeInBetweenSuperCalls;
                StartCoroutine(SuperPower());
            }
        }
    }


    public virtual void Move() {
        Vector3 directionPlayer = new Vector3(Input.GetAxisRaw("Horizontal"), 0, Input.GetAxisRaw("Vertical"));
        Vector3 moveVelocity = directionPlayer.normalized * moveSpeed;
        playerController.Move(moveVelocity);

    }

    public virtual IEnumerator SuperPower(){
        print("SuperPower called");
        yield return new WaitForSeconds(superPowerDelay);
    }
}
