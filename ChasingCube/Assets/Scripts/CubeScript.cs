using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
///  Class cube the base of all type of cube in the game 
/// </summary>
public class CubeScript
{
    private float damagePt;
    private float health;  
    private float speed;
    GameConstants.CubeType cubeType; 

    #region  constructor

    ///<summary>
    /// constructor 
    ///</summary>
    CubeScript(float damagePt, float health, GameConstants.CubeType cubeType)
    {
        this.damagePt = damagePt;
        this.health = health;
        this.speed = 10.0f;
        this.cubeType = cubeType;
    }

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
    }

    ///<summary>
    /// Get the speed of the cube
    ///</summary>
    public float Speed
    {
        get {return speed;}
    }

    ///<summary>
    /// Get the cube type
    ///</summary>
    public GameConstants.CubeType CubeType
    {
        get {return cubeType;}
    }

    #endregion

    #region Public methods

    ///<summary>
    /// move the cube in the direction that we want
    ///</summary>
    public void Move()
    {
        float moveHorizontal = -1*Input.GetAxis("Horizontal");
        float moveVertical = -1*Input.GetAxis("Vertical");
        //transform.Translate(moveHorizontal*Time.deltaTime*speed, 0.0f, moveVertical*Time.deltaTime*speed);
    }

    ///<summary>
    /// the hunter chase the hunted
    ///<param name="cube">cube we are chasing after</param>
    ///</summary>
    public void ChaseCube(GameObject cube) {
        
    }

    #endregion
 
}
