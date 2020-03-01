using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class SlowerBehavior : MonoBehaviour
{

    #region fields

    SlowerCube cubeSlow;
    ReduceSpeedEvent reduceSpeed = new ReduceSpeedEvent();

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
        EventsManager.AddReduceSpeedInvoker(this);
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


    /// <summary>
    /// Adds the given listener for the ReduceSpeedEvent
    /// </summary>
    /// <param name="listener">listener</param>
    public void AddReduceSpeedListener(UnityAction<CubeScript> listener)
    {
        reduceSpeed.AddListener(listener);
    }
}
