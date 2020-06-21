using System;
using UnityEngine;


public class PlayerInfo : MonoBehaviour
{
    
    #region fields

    private float damagePt;
    private float health;  
    private float speed;

    #endregion 

    #region properties

    ///<summary>
    /// Get and Set the damagePt of the cube
    ///</summary>
    public float DamagePt
    {
        get { return damagePt; } 
        set { damagePt = value; }
    }

    ///<summary>
    /// Get the health of the cube
    ///</summary>
    public float Health
    {
        get {return health;}
        set {health = value;}
    }

    ///<summary>
    /// Get the speed of the cube
    ///</summary>
    public float Speed
    {
        get {return speed;}
        set {speed = value;}
    }

    #endregion

}