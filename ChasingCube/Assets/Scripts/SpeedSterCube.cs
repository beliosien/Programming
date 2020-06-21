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
    public override void SpecialPower(GameObject other) {
        if (playerInfo.Speed < GameConstants.MAX_SPEED) 
        {
            playerInfo.Speed += (GameConstants.INCREASE_VALUE/other.GetComponent<PlayerInfo>().Speed);
        }
    }

    #endregion
}
