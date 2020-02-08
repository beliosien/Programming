using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary>
/// the slower cube class
///</summary>
public class SlowerCube : CubeScript
{
    #region constructor

    ///<summary>
    /// constructor
    ///<param name="cubeType"> the type of cube </param>
    ///<param name="gameObject"> the game object </param>
    ///</summary>
    public SlowerCube(GameConstants.CubeType cubeType, GameObject gameObject) : base(cubeType, gameObject) {}

    #endregion

    #region public method

    ///<summary>
    /// reduce the speed of the opponent 
    /// on touch
    ///<param name="opponentCube"> opponentCube </param>
    ///</summary>
    public void ReduceSpeed(GameObject opponentCube) 
    {
        string cubeName = opponentCube.gameObject.name;
        Debug.Log(cubeName);
        Debug.Log("reduce function called");
                
        switch (cubeName)
        {
            case GameConstants.slowerCube: 
                opponentCube.gameObject.GetComponent<SlowerBehavior>().CubeSlow.Speed 
                                                    -= GameConstants.FACTOR_SPEED_REDUCE;
                break;
            
            case GameConstants.speedsterCube:
                opponentCube.gameObject.GetComponent<SpeedSterBehavior>().CubeSpeedSter.Speed 
                                                    -= GameConstants.FACTOR_SPEED_REDUCE;
                Debug.Log("reducing the speed of the speedSter cube");
                break;

            default:
                Debug.Log("in the default case");
                break;
        }
    }

    #endregion
}
