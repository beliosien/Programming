using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jumper : Player
{

    new Rigidbody rigidbody;

    protected override void Start()
    {
        base.Start();

        rigidbody = GetComponent<Rigidbody>();
    }
    public override IEnumerator SuperPower(){

        rigidbody.AddForce(Vector3.up * GameConstants.JUMPER_HEIGHT, ForceMode.Impulse);
        yield return new WaitForSeconds(superPowerDelay);
       
    }

}
