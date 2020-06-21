using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
///  Cube class the base of all type of cube in the game 
/// </summary>
public abstract class CubeScript : MonoBehaviour
{
    #region fields

    ///<summary>
    /// fields
    ///</summary>
    [SerializeField]
    public float damagePt;
    [SerializeField]
    public float health;
    [SerializeField]  
    public float speed;

    protected PlayerInfo playerInfo;

    #endregion 

    private void Start() 
    {
       playerInfo =  gameObject.GetComponent<PlayerInfo>();
       playerInfo.Speed = speed;
       playerInfo.Health = health;
       playerInfo.DamagePt = damagePt;
    }

    private void Update() 
    {
        Move();
    }


    #region Public methods

    ///<summary>
    /// move the cube in the direction that we want
    ///</summary>
    public abstract void Move(); 
   // {
        /*if (gameObject.tag == GameConstants.HUNTED) 
        {
            float translationX = Input.GetAxis("Horizontal") * speed * Time.deltaTime * -1;
            float translationY = Input.GetAxis("Vertical") * speed * Time.deltaTime * -1;
            gameObject.transform.Translate(translationX,0,translationY);  
        } else if (gameObject.tag == GameConstants.HUNTER)
        {
            // we find the hunted cube to chase after it 
            GameObject hunted = GameObject.FindGameObjectWithTag(GameConstants.HUNTED);
            this.ChaseCube(hunted);
        } */
         

    //}
    #endregion


    #region  private methods

    ///<summary>
    /// the hunter chase the hunted
    ///<param name="cube">cube we are chasing after</param>
    ///</summary>
    public void ChaseCube(GameObject cube) 
    {
        float distance = Vector3.Distance(gameObject.transform.position,  cube.gameObject.transform.position);
        if (distance > GameConstants.MINDIST)
        {
            gameObject.transform.position = Vector3.MoveTowards(gameObject.transform.position, 
                                cube.gameObject.transform.position, 2.0f * Time.deltaTime);
        }
        // stop the game object when it reach the hunted
        gameObject.GetComponent<Rigidbody>().velocity = Vector3.zero;
    }

    #endregion
 
}
