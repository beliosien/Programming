using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary>
/// the slower cube class
///</summary>
public class SlowerCube : CubeScript
{

    #region public method

    ///<summary>
    /// reduce the speed of the opponent 
    /// on touch
    ///<param name="opponentCube"> opponentCube </param>
    ///</summary>
    public override void SpecialPower(GameObject other) 
    {
        other.gameObject.GetComponent<PlayerInfo>().Speed -= GameConstants.FACTOR_SPEED_REDUCE;
    }

    #endregion
}
