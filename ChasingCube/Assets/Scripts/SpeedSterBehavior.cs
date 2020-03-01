using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary>
/// speedsterBehavior class 
///</summary>
public class SpeedSterBehavior : MonoBehaviour
{
    #region fields

    SpeedSterCube cubeSpeedSter;

    #endregion

    #region properties

    public SpeedSterCube CubeSpeedSter
    {
        get {return cubeSpeedSter;}
    }

    #endregion

    ///<summary>
    /// Start is called before the first frame update
    ///</summary>
    void Start()
    {
        cubeSpeedSter = new SpeedSterCube(GameConstants.CubeType.speedsterCube, gameObject);


    }

    ///<summary>
    /// Update is called once per frame
    ///</summary>
    void Update()
    {
        cubeSpeedSter.Move();
    }

    ///<summary>
    /// the speed of the cube increase by some factor each time 
    /// it touches another cube 
    /// <param name="other"> the other cube </param>
    void OnCollisionEnter(Collision other) 
    {
        if(gameObject.tag == GameConstants.HUNTED && other.gameObject.tag == GameConstants.HUNTER)
        {
            cubeSpeedSter.IncreaseSpeed();
        }
    }
}
