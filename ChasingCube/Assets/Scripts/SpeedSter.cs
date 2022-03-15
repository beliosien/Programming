using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpeedSter : Player
{
    public override IEnumerator SuperPower(){
        float originalSpeed = moveSpeed;
        moveSpeed = moveSpeed * GameConstants.ACCELERATION;
        yield return new WaitForSeconds(superPowerDelay);
        moveSpeed = originalSpeed;
    }
}
