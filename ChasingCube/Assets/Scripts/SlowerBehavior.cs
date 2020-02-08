using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SlowerBehavior : MonoBehaviour
{

    #region fields

    SlowerCube cubeSlow;

    #endregion

    #region properties

    public SlowerCube CubeSlow 
    {
        get { return cubeSlow;}
    }

    #endregion

    ///<summary>
    /// Start is called before the first frame update
    ///</summary>
    void Start()
    {
        cubeSlow = new SlowerCube(GameConstants.CubeType.slowerCube, gameObject);
    }

    ///<summary>
    /// Update is called once per frame
    ///</summary>
    void Update()
    {
        cubeSlow.Move();
    }

    ///<summary>
    /// the slower cube will reduce  the speed of the opponent  
    /// by some factor each time on touch
    /// <param name="other"> the other cube </param>
    void OnCollisionEnter(Collision other) 
    {
        if(gameObject.tag == GameConstants.HUNTER && other.gameObject.tag == GameConstants.HUNTED)
        {
            cubeSlow.ReduceSpeed(other.gameObject);
        }
    }
}
