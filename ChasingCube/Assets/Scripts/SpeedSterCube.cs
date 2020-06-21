using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary> 
/// SpeedSterCube class 
///</summary>
public class SpeedSterCube : CubeScript
{
    #region Public methods

    ///<summary>
    /// method that increase the speed of the cube
    ///</summary>
    public void IncreaseSpeed() {
        if (playerInfo.Speed < GameConstants.MAX_SPEED) 
        {
            playerInfo.Speed += GameConstants.INCREASE_VALUE;
        }
    }

    public override void Move() 
    {
        print (" i am moving speedster cube");
    }

    ///<summary>
    /// the speed of the cube increase by some factor each time 
    /// it touches another cube 
    /// <param name="other"> the other cube </param>
    void OnCollisionEnter(Collision other) 
    {
        if(gameObject.tag == GameConstants.HUNTED && other.gameObject.tag == GameConstants.HUNTER)
        {
            IncreaseSpeed();
        }
    }

    #endregion
}
