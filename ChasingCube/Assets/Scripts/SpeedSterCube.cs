using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary> 
/// SpeedSterCube class 
///</summary>
public class SpeedSterCube : CubeScript
{
    #region constructor 

    ///<summary>
    /// constructor
    ///<param name="cubeType"> the type of cube </param>
    ///<param name="gameObject"> the game object </parma>
    ///</summary>
    public SpeedSterCube(GameConstants.CubeType cubeType, GameObject gameObject) : base(cubeType, gameObject) {}

    #endregion

    #region Public methods

    ///<summary>
    /// method that increase the speed of the cube
    ///</summary>
    public void IncreaseSpeed() {
        if (this.Speed < GameConstants.MAX_SPEED) 
        {
            this.Speed += GameConstants.INCREASE_VALUE;
        }
    }

    #endregion
}
