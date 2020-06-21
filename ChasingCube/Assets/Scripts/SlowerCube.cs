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
    public void ReduceSpeed(GameObject opponentCube) 
    {
        opponentCube.gameObject.GetComponent<PlayerInfo>().Speed -= GameConstants.FACTOR_SPEED_REDUCE;
    }

    public override void Move()
    {
        print("allo");
    }

    ///<summary>
    /// the slower cube will reduce  the speed of the opponent  
    /// by some factor each time on touch
    /// <param name="other"> the other cube </param>
    void OnCollisionEnter(Collision other) 
    {
        if(gameObject.tag == GameConstants.HUNTER && other.gameObject.tag == GameConstants.HUNTED)
        {
            ReduceSpeed(other.gameObject);
        }
    }

    #endregion
}
